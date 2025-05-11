from Utils import *
from typing import List, Dict, Any, Tuple, Optional, TypedDict, Union

# from StaticCheck import *
# from StaticError import *
from Emitter import *
from Frame import Frame
from abc import ABC, abstractmethod
from functools import reduce
from Visitor import *
from AST import *
import logging


class OType(TypedDict):
    frame: Frame
    env: List[List[Symbol]]
    stmt: bool
    isLeft: bool

class Constant(Val):
    def __init__(self, value: Any):
        self.value = value

class CodeGenerator(BaseVisitor, Utils):
    def __init__(self) -> None:
        self.className = "MiniGoClass"
        self.astTree = None
        self.path = None
        self.emit = None
        self.function = None
        self.list_function = []
        self.logger = logging.getLogger(__name__)

    def init(self) -> List[Symbol]:
        logger = logging.getLogger(f"{'init':<20}")
        logger.debug("=" * 60)
        logger.debug("Initializing CodeGenerator")
        mem = [
            Symbol("getInt", MType([], IntType()), CName("io", True)),
            Symbol("putInt", MType([IntType()], VoidType()), CName("io", True)),
            Symbol("putIntLn", MType([IntType()], VoidType()), CName("io", True)),
            Symbol("getFloat", MType([], FloatType()), CName("io", True)),
            Symbol("putFloat", MType([FloatType()], VoidType()), CName("io", True)),
            Symbol("putFloatLn", MType([FloatType()], VoidType()), CName("io", True)),
            Symbol("getBool", MType([], BoolType()), CName("io", True)),
            Symbol("putBool", MType([BoolType()], VoidType()), CName("io", True)),
            Symbol("putBoolLn", MType([BoolType()], VoidType()), CName("io", True)),
            Symbol("getString", MType([], StringType()), CName("io", True)),
            Symbol("putString", MType([StringType()], VoidType()), CName("io", True)),
            Symbol("putStringLn", MType([StringType()], VoidType()), CName("io", True)),
            Symbol("putLn", MType([], VoidType()), CName("io", True)),
        ]
        return mem

    def gen(self, ast: Program, dir_: str) -> None:
        logger = logging.getLogger(f"{'gen':<20}")
        logger.debug("=" * 60)
        logger.debug(f"Generating code for program in directory: {dir_}")
        gl = self.init()
        self.astTree = ast
        self.path = dir_
        self.emit = Emitter(dir_ + "/" + self.className + ".j")
        self.visit(ast, gl)

    def emitObjectInit(self) -> None:
        logger = logging.getLogger(f"{'emitObjectInit':<20}")
        logger.debug("=" * 60)
        logger.debug("Emitting object initialization")
        frame = Frame("<init>", VoidType())
        self.emit.printout(
            self.emit.emitMETHOD("<init>", MType([], VoidType()), False, frame)
        )  # Bắt đầu định nghĩa phương thức <init>
        frame.enterScope(True)
        self.emit.printout(
            self.emit.emitVAR(
                frame.getNewIndex(),
                "this",
                ClassType(self.className),
                frame.getStartLabel(),
                frame.getEndLabel(),
                frame,
            )
        )  # Tạo biến "this" trong phương thức <init>

        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        self.emit.printout(
            self.emit.emitREADVAR("this", ClassType(self.className), 0, frame)
        )
        self.emit.printout(self.emit.emitINVOKESPECIAL(frame))

        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()

    def emitObjectCInit(self, ast: Program, env: OType) -> None:
        logger = logging.getLogger(f"{'emitObjectCInit':<20}")
        logger.debug("=" * 60)
        logger.debug("Emitting static variables initialization")
        frame = Frame("<clinit>", VoidType())
        self.emit.printout(
            self.emit.emitMETHOD("<clinit>", MType([], VoidType()), True, frame)
        )
        frame.enterScope(True)
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))

        env["frame"] = frame
        # self.visit(Block([
        #     ## TODO implement for item in ast.decl if isinstance(item, VarDecl) and item.varInit]),env)
        # ]))
        globalInit = ""
        for decl in ast.decl:
            if isinstance(decl, VarDecl):
                rhsCode, rhsType = self.visit(decl.varInit, env)
                if not decl.varType:
                    decl.varType = rhsType
                globalInit += rhsCode
                if type(decl.varType) is FloatType and type(rhsType) is IntType:
                    globalInit += self.emit.emitI2F(frame)
                globalInit += self.emit.emitPUTSTATIC(
                    CodeGenerator.classMemberName(self.className, decl.varName),
                    decl.varType,
                    frame,
                )

        self.emit.printout(globalInit)
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()

    def visitProgram(self, ast: Program, c: List[Symbol]) -> OType:
        logger = logging.getLogger(f"{'visitProgram':<20}")
        logger.debug("=" * 60)
        logger.debug(f"Visiting Program with {len(ast.decl)} declarations")
        self.list_function = c + [
            Symbol(
                item.name,
                MType(list(map(lambda x: x.parType, item.params)), item.retType),
                CName(self.className),
            )
            for item in ast.decl
            if isinstance(item, FuncDecl)
        ]
        env: OType = {}
        env["env"] = [c]
        env["isLeft"] = False
        env["stmt"] = True
        self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))
        env = reduce(
            lambda a, x: self.visit(x, a) if isinstance(x, (VarDecl, ConstDecl)) else a,
            ast.decl,
            env,
        )
        reduce(
            lambda a, x: self.visit(x, a) if isinstance(x, FuncDecl) else a,
            ast.decl,
            env,
        )
        self.emitObjectInit()
        self.emitObjectCInit(ast, env)
        self.emit.printout(self.emit.emitEPILOG())
        return env

    # ! ================== DECLARATION =========================
    def visitFuncDecl(self, ast: FuncDecl, o: OType) -> OType:
        logger = logging.getLogger(f"{'visitFuncDecl':<20}")
        logger.debug("=" * 60)
        logger.debug(f"Visiting Function Declaration: {ast.name}")
        self.function = ast
        frame = Frame(ast.name, ast.retType)
        isMain = ast.name == "main"
        if isMain:
            mtype = MType([ArrayType([None], StringType())], VoidType())
        else:
            mtype = MType(list(map(lambda x: x.parType, ast.params)), ast.retType)

        env = o.copy()
        env["frame"] = frame
        self.emit.printout(self.emit.emitMETHOD(ast.name, mtype, True, frame))
        frame.enterScope(True)
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        env["env"] = [[]] + env["env"]
        if isMain:
            self.emit.printout(
                self.emit.emitVAR(
                    frame.getNewIndex(),
                    "args",
                    ArrayType([None], StringType()),
                    frame.getStartLabel(),
                    frame.getEndLabel(),
                    frame,
                )
            )
        else:
            env = reduce(lambda acc, e: self.visit(e, acc), ast.params, env)
        self.visit(ast.body, env)
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        if type(ast.retType) is VoidType:
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()
        return o

    def visitParamDecl(self, ast: ParamDecl, o: OType) -> OType:
        logger = logging.getLogger(f"{'visitParamDecl':<20}")
        logger.debug("=" * 60)
        logger.debug(
            f"Visiting Parameter Declaration: {ast.parName} of type {ast.parType}"
        )
        frame = o["frame"]
        index = frame.getNewIndex()
        o["env"][0].append(Symbol(ast.parName, ast.parType, Index(index)))
        self.emit.printout(
            self.emit.emitVAR(
                index,
                ast.parName,
                ast.parType,
                frame.getStartLabel(),
                frame.getEndLabel(),
                frame,
            )
        )
        return o

    def visitVarDecl(self, ast: VarDecl, o: OType) -> OType:
        logger = logging.getLogger(f"{'visitVarDecl':<20}")
        logger.debug("=" * 60)
        logger.debug(
            f"Visiting Variable Declaration: {ast.varName} of type {ast.varType} and init {ast.varInit}"
        )
        varInit = ast.varInit
        varType = ast.varType
        if not varInit:
            varInit = self.initValue(varType, o)
            if type(ast.varType) is ArrayType:
                varInit = ArrayLiteral(ast.varType.dimens, ast.varType.eleType, varInit)
            ast.varInit = varInit
        env = o.copy()
        env["frame"] = Frame("<dumb>", VoidType())
        rhsCode, rhsType = self.visit(varInit, env)
        if not varType:
            varType = rhsType

        if "frame" not in o:  # global var
            o["env"][0].append(Symbol(ast.varName, varType, CName(self.className)))
            self.emit.printout(
                self.emit.emitATTRIBUTE(ast.varName, varType, True, False, None)
            )
        else:
            frame: Frame = o["frame"]
            index = frame.getNewIndex()
            o["env"][0].append(Symbol(ast.varName, varType, Index(index)))
            emitCode = self.emit.emitVAR(
                index,
                ast.varName,
                varType,
                frame.getStartLabel(),
                frame.getEndLabel(),
                frame,
            )
            self.emit.printout(emitCode)
            rhsCode, rhsType = self.visit(varInit, o)
            if type(varType) is FloatType and type(rhsType) is IntType:
                rhsCode += self.emit.emitI2F(frame)
            self.emit.printout(rhsCode)
            logger.debug(f"Writing variable {ast.varName} of type {varType} at index {index}")
            self.emit.printout(
                self.emit.emitWRITEVAR(ast.varName, varType, index, frame)
            )
        return o
    
    def visitConstDecl(self, ast: ConstDecl, o: OType) -> OType:
        logger = logging.getLogger(f"{'visitConstDecl':<20}")
        logger.debug("=" * 60)
        logger.debug(f"Visiting Constant Declaration: {ast.conName} of type {ast.conType}")
        

        if "frame" in o:
            # Local constant
            init = self.evaluate(ast.iniExpr, o)
            conType = self.valueToAstType(init)
            o["env"][0].append(Symbol(ast.conName, conType, Constant(init)))
            return o
        value = self.evaluate(ast.iniExpr, o)
        astType = self.valueToAstType(value)

        if not astType:
            raise ValueError(f"Invalid constant value: {value}")
        o["env"][0].append(Symbol(ast.conName, astType, CName(self.className)))
        self.emit.printout(
            self.emit.emitATTRIBUTE(ast.conName, astType, True, True, str(value))
        )
        return o

    # ! ================== FUNCTION CALL =========================
    def visitFuncCall(self, ast: FuncCall, o: OType) -> Union[OType, str]:
        logger = logging.getLogger(f"{'visitFuncCall':<20}")
        logger.debug("=" * 60)
        logger.debug(
            f"Visiting Function Call: {ast.funName} with {len(ast.args)} arguments"
        )
        sym: Symbol = next(filter(lambda x: x.name == ast.funName, self.list_function), None)
        env = o.copy()
        env["stmt"] = False

        logger.debug(f"stmt: {o.get('stmt')}")

        if o.get("stmt"):
            logger.debug(f"ast.args: {ast.args}")
            argCode = "".join([self.visit(arg, env)[0] for arg in ast.args])
            logger.debug(f"argCode: {argCode}")
            self.emit.printout(argCode)
            self.emit.printout(
                self.emit.emitINVOKESTATIC(
                    CodeGenerator.classMemberName(sym.value.value, ast.funName),
                    sym.mtype,
                    o["frame"],
                )
            )
            return o
        output = "".join([str(self.visit(x, env)[0]) for x in ast.args])
        output += self.emit.emitINVOKESTATIC(
            CodeGenerator.classMemberName(sym.value.value, ast.funName),
            sym.mtype,
            o["frame"],
        )
        return output, sym.mtype

    # ! ================== STATEMENT =========================
    def visitBlock(self, ast: Block, o: OType) -> OType:
        logger = logging.getLogger(f"{'visitBlock':<20}")
        logger.debug("=" * 60)
        logger.debug(f"Visiting Block with {len(ast.member)} statements")
        env = o.copy()  
        env["env"] = [[]] + env["env"]  # Create a new scope
        env["frame"].enterScope(False)
        self.emit.printout(
            self.emit.emitLABEL(env["frame"].getStartLabel(), env["frame"])
        )

        for item in ast.member:
            if type(item) is FuncCall:
                env["stmt"] = True
            env = self.visit(item, env)

        self.emit.printout(
            self.emit.emitLABEL(env["frame"].getEndLabel(), env["frame"])
        )
        env["frame"].exitScope()
        return o
    
    def visitAssign(self, ast: Assign, o: OType) -> OType:
        logger = logging.getLogger(f"{'visitAssign':<20}")
        logger.debug("=" * 60)
        logger.debug(
            f"Visiting Assignment: {ast.lhs.name if isinstance(ast.lhs, Id) else 'complex expression'}"
        )
        if type(ast.lhs) is Id:
            sym = None
            for scope in o["env"]:
                sym = next(filter(lambda x: x.name == ast.lhs.name, scope), None)
                if sym:
                    break
            if not sym:
                # Implicit declaration, call visitVarDecl
                return self.visitVarDecl(VarDecl(ast.lhs.name, None, ast.rhs), o)
        elif type(ast.lhs) is ArrayCell:
            o["isLeft"] = True
            lhsCode, lhsType = self.visit(ast.lhs, o)
            o["isLeft"] = False
            rhsCode, rhsType = self.visit(ast.rhs, o)
            self.emit.printout(lhsCode)
            self.emit.printout(rhsCode)
            if type(lhsType) is FloatType and type(rhsType) is IntType:
                rhsCode += self.emit.emitI2F(o["frame"])
            self.emit.printout(self.emit.emitASTORE(lhsType, o["frame"]))
            return o
        rhsCode, rhsType = self.visit(ast.rhs, o)
        o["isLeft"] = True
        lhsCode, lhsType = self.visit(ast.lhs, o)
        o["isLeft"] = False

        self.emit.printout(rhsCode)
        if type(lhsType) is FloatType and type(rhsType) is IntType:
            rhsCode += self.emit.emitI2F(o["frame"])
        self.emit.printout(lhsCode)
        return o

    def visitReturn(self, ast: Return, o: OType) -> OType:
        logger = logging.getLogger(f"{'visitReturn':<20}")
        logger.debug("=" * 60)
        logger.debug(f"Visiting Return with expression: {ast.expr is not None}")
        exprCode, exprType = None, VoidType()
        if ast.expr:
            exprCode, exprType = self.visit(ast.expr, o)
            self.emit.printout(exprCode)
        self.emit.printout(
            self.emit.emitRETURN(exprType, o["frame"])
        )
        return o

    ## TODO END decl ------------------------------

    # ! ================== EXPRESSION =========================
    def visitId(self, ast: Id, o: OType) -> Tuple[str, Type]:
        logger = logging.getLogger(f"{'visitId':<20}")
        logger.debug("-" * 60)
        logger.debug(f"Visiting Identifier: {ast.name}")
        sym: Symbol = next(
            filter(lambda x: x.name == ast.name, [j for i in o["env"] for j in i]), None
        )
        if o.get("isLeft"):
            if type(sym.value) is Index:
                return (
                    self.emit.emitWRITEVAR(
                        ast.name, sym.mtype, sym.value.value, o["frame"]
                    ),
                    sym.mtype,
                )
            else:
                return (
                    self.emit.emitPUTSTATIC(
                        CodeGenerator.classMemberName(self.className, sym.name),
                        sym.mtype,
                        o["frame"],
                    ),
                    sym.mtype,
                )
        if type(sym.value) is Index:
            return (
                self.emit.emitREADVAR(
                    ast.name,
                    sym.mtype,
                    sym.value.value,
                    o["frame"],
                ),
                sym.mtype,
            )
        elif type(sym.value) is Constant:
            return self.emit.emitPUSHCONST(sym.value.value, sym.mtype, o["frame"]), sym.mtype
        else:
            return (
                self.emit.emitGETSTATIC(
                    CodeGenerator.classMemberName(self.className, sym.name),
                    sym.mtype,
                    o["frame"],
                ),
                sym.mtype,
            )

    def visitArrayCell(self, ast: ArrayCell, o: OType) -> Tuple[str, Type]:
        logger = logging.getLogger(f"{'visitArrayCell':<20}")
        logger.debug("=" * 60)
        logger.debug(f"Visiting Array Cell:")

        tmp = o["isLeft"]
        o["isLeft"] = False
        code, type = self.visit(ast.arr, o)
        o["isLeft"] = tmp
        logger.debug(f"Type: {type}")

        for i in range(len(ast.idx) - 1):
            exprCode, exprType = self.visit(ast.idx[i], o)
            code += exprCode
            code += self.emit.emitALOAD(ArrayType(type.dimens[1:], type.eleType), o["frame"])

        logger.debug(f"Last index: {ast.idx[-1]}")
        code += self.visit(ast.idx[-1], o)[0]
        logger.debug(f"isLeft: {o.get('isLeft')}")
        if not o.get("isLeft"):
            code += self.emit.emitALOAD(type.eleType, o["frame"])
        return code, type.eleType

    def visitBinaryOp(self, ast: BinaryOp, o: dict) -> tuple[str, Type]:
        op = ast.op
        frame = o['frame']
        codeLeft, typeLeft = self.visit(ast.left, o)
        codeRight, typeRight = self.visit(ast.right, o) if op not in ['||', '&&'] else (None, None)
        if op in ['+', '-', '*', '/'] and type(typeLeft) in [FloatType, IntType]:
            typeReturn = IntType() if type(typeLeft) is IntType and type(typeRight) is IntType else FloatType()
            if type(typeReturn) is FloatType:
                if type(typeLeft) is IntType:
                    codeLeft += self.emit.emitI2F(frame)
                elif type(typeRight) is IntType:
                    codeRight += self.emit.emitI2F(frame)
            if op in ['+', '-']:
                return codeLeft + codeRight + self.emit.emitADDOP(op, typeReturn, frame), typeReturn
            elif op in ['*', '/']:
                return codeLeft + codeRight + self.emit.emitMULOP(op, typeReturn, frame), typeReturn
            else:
                raise SyntaxError(f"Binary operation {op} is not supported")
        elif op == "+" and type(typeLeft) is StringType:
            return codeLeft + codeRight + self.emit.emitINVOKEVIRTUAL("java/lang/String/concat", MType([StringType()], StringType()), frame), StringType()
        elif op in ['%']:
            return codeLeft + codeRight + self.emit.emitMOD(frame), IntType()
        elif op in ['==', '!=', '<', '>', '>=', '<='] and type(typeLeft) in [FloatType, IntType]:
            return codeLeft + codeRight + self.emit.emitREOP(op, typeLeft, frame), IntType()
        elif op in ['||', '&&']:
            code = codeLeft
            label1 = frame.getNewLabel()
            label2 = frame.getNewLabel()
            code += self.emit.emitIFFALSE(label1, frame) if op == '||' else self.emit.emitIFTRUE(label1, frame)
            code += self.emit.emitPUSHCONST("true" if op == '||' else "false", BoolType(), frame)
            code += self.emit.emitGOTO(label2, frame)
            code += self.emit.emitLABEL(label1, frame)
            codeRight, typeRight = self.visit(ast.right, o)
            code += codeRight
            code += self.emit.emitLABEL(label2, frame)
            return code, BoolType()

        elif op in ['==', '!=', '<', '>', '>=', '<='] and type(typeLeft) in [StringType]:
            # compareTo method
            code = codeLeft + codeRight + self.emit.emitINVOKEVIRTUAL("java/lang/String/compareTo", MType([StringType()], IntType()), frame)
            code += self.emit.emitPUSHCONST("0", IntType(), frame)
            code = code + self.emit.emitREOP(op, IntType(), frame)
            return code, BoolType()
        else:
            raise SyntaxError(f"Binary operation {op} is not supported")

    def visitUnaryOp(self, ast: UnaryOp, o: OType) -> Tuple[str, Type]:
        logger = logging.getLogger(f"{'visitUnaryOp':<20}")
        logger.debug("-" * 60)
        logger.debug(f"Visiting Unary Operation: {ast.op}")
        if ast.op == "!":
            code, type_return = self.visit(ast.body, o)
            return code + self.emit.emitNOT(BoolType(), o["frame"]), BoolType()
        elif ast.op == "-":
            code, type_return = self.visit(ast.body, o)
            return code + self.emit.emitNEGOP(type_return, o["frame"]), type_return
        raise SyntaxError(f"Unary operation {ast.op} is not supported")

    def visitIntLiteral(self, ast: IntLiteral, o: OType) -> Tuple[str, Type]:
        logger = logging.getLogger(f"{'visitIntLiteral':<20}")
        logger.debug("-" * 60)
        logger.debug(f"Visiting Integer Literal: {ast.value}")
        return self.emit.emitPUSHICONST(ast.value, o["frame"]), IntType()

    def visitFloatLiteral(self, ast: FloatLiteral, o: OType) -> Tuple[str, Type]:
        logger = logging.getLogger(f"{'visitFloatLiteral':<20}")
        logger.debug("-" * 60)
        logger.debug(f"Visiting Float Literal: {ast.value}")
        return self.emit.emitPUSHFCONST(ast.value, o["frame"]), FloatType()

    def visitBooleanLiteral(self, ast: BooleanLiteral, o: OType) -> Tuple[str, Type]:
        logger = logging.getLogger(f"{'visitBooleanLiteral':<20}")
        logger.debug("-" * 60)
        logger.debug(f"Visiting Boolean Literal: {ast.value}")
        return self.emit.emitPUSHICONST(ast.value, o["frame"]), BoolType()

    def visitStringLiteral(self, ast: StringLiteral, o: OType) -> Tuple[str, Type]:
        logger = logging.getLogger(f"{'visitStringLiteral':<20}")
        logger.debug("-" * 60)
        logger.debug(f"Visiting String Literal: {ast.value}")
        return (
            self.emit.emitPUSHCONST(ast.value, StringType(), o["frame"]),
            StringType(),
        )

    def visitArrayLiteral(self, ast: ArrayLiteral, o: OType) -> Tuple[str, Type]:
        logger = logging.getLogger(f"{'visitArrayLiteral':<20}")
        logger.debug("-" * 60)
        logger.debug(f"Visiting Array Literal with {len(ast.dimens)} dimensions, {ast.eleType} type, values {ast.value}")
        value = self.evaluate(ast.value, o)
        logger.debug(f"Value: {value}")
        dimens = self.evaluate(ast.dimens, o)
        logger.debug(f"Type: {dimens}")   
        code = self.emit.emitNEWARRAY(dimens, ast.eleType, value, o["frame"])
        return code, ArrayType(dimens, ast.eleType)

    def visitStructLiteral(self, ast: StructLiteral, o: OType) -> Tuple[str, Type]:
        logger = logging.getLogger(f"{'visitStructLiteral':<20}")
        logger.debug("-" * 60)
        logger.debug(f"Visiting Struct Literal with {len(ast.elems)} fields")
        pass

    def visitNilLiteral(self, ast: NilLiteral, o: OType) -> Tuple[str, Type]:
        logger = logging.getLogger(f"{'visitNilLiteral':<20}")
        logger.debug("-" * 60)
        logger.debug("Visiting Nil Literal")
        pass

    ## TODO END basic expression ------------------------------

    # ! ================== TYPE VISITOR =========================
    def visitIntType(self, ast: IntType, o: OType):
        return IntType()
    
    def visitFloatType(self, ast: FloatType, o: OType):
        return FloatType()
    
    def visitBoolType(self, ast: BoolType, o: OType):
        return BoolType()
    
    def visitStringType(self, ast: StringType, o: OType):
        return StringType()
    
    def visitVoidType(self, ast: VoidType, o: OType):
        return VoidType()
    
    def visitArrayType(self, ast: ArrayType, o: OType):
        return ArrayType()
    
    def visitStructType(self, ast: StructType, o: OType):
        return StructType()

    def visitInterfaceType(self, ast: InterfaceType, o: OType):
        return InterfaceType()


    # ! ================== HELPER =========================
    @staticmethod
    def classMemberName(className: str, memberName: str) -> str:
        return f"{className}/{memberName}"

    def valueToAstType(self, value: Any) -> Type:
        if isinstance(value, int):
            return IntType()
        elif isinstance(value, float):
            return FloatType()
        elif isinstance(value, bool):
            return BoolType()
        elif isinstance(value, str):
            return StringType()
        return None

    def initValue(self, valueType: Type, o: OType) -> Literal:
        if type(valueType) is IntType:
            return IntLiteral(0)
        elif type(valueType) is FloatType:
            return FloatLiteral(0.0)
        elif type(valueType) is BoolType:
            return BooleanLiteral(False)
        elif type(valueType) is StringType:
            return StringLiteral("")
        elif type(valueType) is ArrayType:
            if len(valueType.dimens) == 0:
                return self.initValue(valueType.eleType, o)
            else:
                value = []
                length = self.evaluate(valueType.dimens[0], o)
                for i in range(length):
                    value.append(self.initValue(ArrayType(valueType.dimens[1:], valueType.eleType), o))
                logging.debug(f"Value: {value}")
                return value
        else:
            return NilLiteral()

    def evaluate(self, ast: AST, o: OType):
        logger = logging.getLogger(f"{'evaluate':<20}")
        logger.debug("=" * 60)
        logger.debug(f"Evaluating: {ast}")
        logger.debug(f"Evaluating type: {type(ast)}")
        if isinstance(ast, (IntLiteral, FloatLiteral, BooleanLiteral, StringLiteral)):
            return ast.value
        elif isinstance(ast, list):
            return [self.evaluate(i, o) for i in ast]
        elif isinstance(ast, Id):
            sym: Symbol = None
            for scope in o["env"]:
                sym = next(filter(lambda x: x.name == ast.name, scope), None)
                if sym:
                    break
            if sym:
                return sym.value.value
        elif isinstance(ast, UnaryOp):
            if ast.op == "-":
                body = self.evaluate(ast.body, o)
                if isinstance(body, (int, float)):
                    return -body
                else:
                    return None
            elif ast.op == "!":
                body = self.evaluate(ast.body, o)
                if isinstance(body, bool):
                    return not body
                else:
                    return None
        elif isinstance(ast, BinaryOp):
            left = self.evaluate(ast.left, o)
            right = self.evaluate(ast.right, o)
            if ast.op == "+":
                if isinstance(left, (int, float)) and isinstance(right, (int, float)):
                    return left + right
                elif isinstance(left, str) and isinstance(right, str):
                    return left + right
                else:
                    return None
            elif ast.op in ["-", "*", "/"]:
                if isinstance(left, (int, float)) and isinstance(right, (int, float)):
                    if ast.op == "-":
                        return left - right
                    elif ast.op == "*":
                        return left * right
                    else:
                        if right != 0:
                            return left / right
                else:
                    return None
            elif ast.op == "%":
                if isinstance(left, int) and isinstance(right, int):
                    return left % right
                else:
                    return None
            elif ast.op in ["==", ">", "<", ">=", "<=", "!="]:
                if type(left) == type(right):
                    if ast.op == "==":
                        return left == right
                    elif ast.op == ">":
                        return left > right
                    elif ast.op == "<":
                        return left < right
                    elif ast.op == ">=":
                        return left >= right
                    elif ast.op == "<=":
                        return left <= right
                    else:
                        return left != right
                else:
                    return None
            elif ast.op in ["&&", "||"]:
                if isinstance(left, bool) and isinstance(right, bool):
                    if ast.op == "&&":
                        return left and right
                    else:
                        return left or right
                else:
                    return None
            return None
        else:
            return None