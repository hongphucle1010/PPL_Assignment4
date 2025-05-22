import logging
from typing import Any, Optional, Tuple
from Utils import *

# from StaticCheck import *
# from StaticError import *
import CodeGenerator as cgen
from MachineCode import JasminCode
from AST import *
from CodeGenError import *


class MType:
    def __init__(self, partype, rettype):
        self.partype = partype
        self.rettype = rettype

    def __str__(self):
        return (
            "MType(["
            + ",".join(str(x) for x in self.partype)
            + "],"
            + str(self.rettype)
            + ")"
        )


class Val(ABC):
    pass


class Index(Val):
    def __init__(self, value):
        # value: Int

        self.value = value


class CName(Val):
    def __init__(self, value, isStatic=True):
        # value: String
        self.isStatic = isStatic
        self.value = value


class ClassType:
    def __init__(self, name):
        # value: Id
        self.name = name


class Interface:
    def __init__(self, interface: InterfaceType, struct: StructType = None):
        self.interface: InterfaceType = interface
        self.struct: StructType = struct


class Symbol:
    def __init__(self, name, mtype, value=None):
        self.name = name
        self.mtype = mtype
        self.value = value

    def __str__(self):
        return (
            "Symbol("
            + str(self.name)
            + ","
            + str(self.mtype)
            + ("" if self.value is None else "," + str(self.value))
            + ")"
        )


class Emitter:
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.buff = list()
        self.jvm = JasminCode()

    def getJVMType(self, inType) -> str:
        typeIn = type(inType)
        if typeIn is IntType:
            return "I"
        if typeIn is FloatType:
            return "F"
        if typeIn is BoolType:
            return "Z"
        elif typeIn is StringType:
            return "Ljava/lang/String;"
        elif typeIn is VoidType:
            return "V"
        elif typeIn is ArrayType:
            return "[" * len(inType.dimens) + self.getJVMType(inType.eleType)
        elif typeIn is MType:
            return (
                "("
                + "".join(list(map(lambda x: self.getJVMType(x), inType.partype)))
                + ")"
                + self.getJVMType(inType.rettype)
            )
        elif typeIn is cgen.ClassType:
            return "L" + inType.name + ";"
        elif typeIn is StructType:
            return "L" + inType.name + ";"
        elif typeIn is InterfaceType:
            return "L" + inType.name + ";"
        elif typeIn is Interface:
            return (
                self.getJVMType(inType.interface)
                if not inType.struct
                else self.getJVMType(inType.struct)
            )
        else:
            return str(typeIn)

    def getFullType(self, inType) -> str:
        typeIn = type(inType)
        if typeIn is IntType:
            return "int"
        elif typeIn is FloatType:
            return "float"
        elif typeIn is BoolType:
            return "boolean"
        elif typeIn is cgen.StringType:
            return "java/lang/String"
        elif typeIn is InterfaceType:
            return "L" + inType.name + ";"
        elif typeIn is StructType:
            return "L" + inType.name + ";"
        elif typeIn is Interface:
            return (
                self.getFullType(inType.interface)
                if not inType.struct
                else self.getFullType(inType.struct)
            )
        elif typeIn is VoidType:
            return "void"

    def emitPUSHICONST(self, in_: Union[int, str], frame) -> str:
        # in: Int or Sring
        # frame: Frame
        if type(in_) is int:
            frame.push()
            i = in_
            if i >= -1 and i <= 5:
                return self.jvm.emitICONST(i)
            elif i >= -128 and i <= 127:
                return self.jvm.emitBIPUSH(i)
            elif i >= -32768 and i <= 32767:
                return self.jvm.emitSIPUSH(i)
        elif type(in_) is bool:
            if in_:
                return self.emitPUSHICONST(1, frame)
            else:
                return self.emitPUSHICONST(0, frame)
        elif type(in_) is str:
            if in_ == "true":
                return self.emitPUSHICONST(1, frame)
            elif in_ == "false":
                return self.emitPUSHICONST(0, frame)
            else:
                return self.emitPUSHICONST(int(in_), frame)

    def emitPUSHFCONST(self, in_: str, frame) -> str:
        # in_: String
        # frame: Frame

        f = float(in_)
        frame.push()
        if f == 0.0 or f == 1.0 or f == 2.0:
            return self.jvm.emitFCONST("{0:.1f}".format(f))
        else:
            return self.jvm.emitLDC(str(f))

    """ 
    *    generate code to push a constant onto the operand stack.
    *    @param in the lexeme of the constant
    *    @param typ the type of the constant
    """

    def emitPUSHCONST(self, in_: str, typ, frame) -> str:
        # in_: String
        # typ: Type
        # frame: Frame
        if type(typ) is IntType or type(typ) is BoolType:
            return self.emitPUSHICONST(in_, frame)
        elif type(typ) is FloatType:
            return self.emitPUSHFCONST(in_, frame)
        elif type(typ) is StringType:
            frame.push()
            return self.jvm.emitLDC(in_)
        else:
            raise IllegalOperandException(in_)

    ##############################################################

    def emitALOAD(self, in_, frame) -> str:
        # in_: Type
        # frame: Frame
        # ..., arrayref, index, value -> ...

        frame.pop()  # index
        frame.pop()  # arrayref
        frame.push()  # value
        if type(in_) is IntType:
            return self.jvm.emitIALOAD()
        elif type(in_) is FloatType:
            return self.jvm.emitFALOAD()
        elif type(in_) is BoolType:
            return self.jvm.emitBALOAD()
        elif (
            type(in_) is cgen.ArrayType
            or type(in_) is cgen.ClassType
            or type(in_) is StringType
            or type(in_) is StructType
            or type(in_) is InterfaceType
            or type(in_) is Interface
        ):
            return self.jvm.emitAALOAD()
        else:
            raise IllegalOperandException(str(in_))

    def emitASTORE(self, in_, frame) -> str:
        # in_: Type
        # frame: Frame
        # ..., arrayref, index, value -> ...

        frame.pop()  # value
        frame.pop()  # index
        frame.pop()  # arrayref
        if type(in_) is IntType:
            return self.jvm.emitIASTORE()
        elif type(in_) is FloatType:
            return self.jvm.emitFASTORE()
        elif type(in_) is BoolType:
            return self.jvm.emitBASTORE()
        elif (
            type(in_) is cgen.ArrayType
            or type(in_) is cgen.ClassType
            or type(in_) is StringType
            or type(in_) is StructType
            or type(in_) is InterfaceType
            or type(in_) is Interface
        ):
            return self.jvm.emitAASTORE()
        else:
            raise IllegalOperandException(str(in_))

    """    generate the var directive for a local variable.
    *   @param in the index of the local variable.
    *   @param varName the name of the local variable.
    *   @param inType the type of the local variable.
    *   @param fromLabel the starting label of the scope where the variable is active.
    *   @param toLabel the ending label  of the scope where the variable is active.
    """

    def emitVAR(
        self, in_: int, varName: str, inType, fromLabel: int, toLabel: int, frame
    ) -> str:
        # in_: Int
        # varName: String
        # inType: Type
        # fromLabel: Int
        # toLabel: Int
        # frame: Frame
        return self.jvm.emitVAR(
            in_, varName, self.getJVMType(inType), fromLabel, toLabel
        )

    def emitREADVAR(self, name: str, inType, index: int, frame) -> str:
        # name: String
        # inType: Type
        # index: Int
        # frame: Frame
        # ... -> ..., value

        frame.push()  # value
        if type(inType) is IntType or type(inType) is BoolType:
            return self.jvm.emitILOAD(index)
        elif type(inType) is FloatType:
            return self.jvm.emitFLOAD(index)
        elif (
            type(inType) is cgen.ArrayType
            or type(inType) is cgen.ClassType
            or type(inType) is StringType
            or type(inType) is StructType
            or type(inType) is InterfaceType
            or type(inType) is Interface
        ):
            return self.jvm.emitALOAD(index)
        else:
            logging.debug(f"name: {name}, inType: {inType}, index: {index}")
            raise IllegalOperandException(name)

    """ generate the second instruction for array cell access
    *
    """

    def emitREADVAR2(self, name: str, typ, frame) -> str:
        # name: String
        # typ: Type
        # frame: Frame
        # ... -> ..., value

        # frame.push()
        raise IllegalOperandException(name)

    """
    *   generate code to pop a value on top of the operand stack and store it to a block-scoped variable.
    *   @param name the symbol entry of the variable.
    """

    def emitWRITEVAR(self, name: str, inType, index: int, frame) -> str:
        # name: String
        # inType: Type
        # index: Int
        # frame: Frame
        # ..., value -> ...

        frame.pop()  # value

        if type(inType) is IntType or type(inType) is BoolType:
            return self.jvm.emitISTORE(index)
        elif type(inType) is FloatType:
            return self.jvm.emitFSTORE(index)
        elif (
            type(inType) is cgen.ArrayType
            or type(inType) is cgen.ClassType
            or type(inType) is StringType
            or type(inType) is StructType
            or type(inType) is InterfaceType
            or type(inType) is Interface
        ):
            return self.jvm.emitASTORE(index)
        else:
            logging.debug(f"InType: {inType}")
            raise IllegalOperandException(name)

    """ generate the second instruction for array cell access
    *
    """

    def emitWRITEVAR2(self, name: str, typ, frame) -> str:
        # name: String
        # typ: Type
        # frame: Frame
        # ..., value -> ...

        # frame.push()
        raise IllegalOperandException(name)

    """ generate the field (static) directive for a class mutable or immutable attribute.
    *   @param lexeme the name of the attribute.
    *   @param in the type of the attribute.
    *   @param isFinal true in case of constant; false otherwise
    """

    def emitATTRIBUTE(
        self, lexeme: str, in_, isStatic: bool, isFinal: bool, value: str
    ) -> str:
        # lexeme: String
        # in_: Type
        # isFinal: Boolean
        # value: String
        if isStatic:
            return self.jvm.emitSTATICFIELD(
                lexeme, self.getJVMType(in_), isFinal, value
            )
        else:
            return self.jvm.emitINSTANCEFIELD(
                lexeme, self.getJVMType(in_), isFinal, value
            )

    def emitGETSTATIC(self, lexeme: str, in_, frame) -> str:
        # lexeme: String
        # in_: Type
        # frame: Frame

        frame.push()  # value
        return self.jvm.emitGETSTATIC(lexeme, self.getJVMType(in_))

    def emitPUTSTATIC(self, lexeme: str, in_, frame) -> str:
        # lexeme: String
        # in_: Type
        # frame: Frame

        frame.pop()  # value
        return self.jvm.emitPUTSTATIC(lexeme, self.getJVMType(in_))

    def emitGETFIELD(self, lexeme: str, in_, frame) -> str:
        # lexeme: String
        # in_: Type
        # frame: Frame

        return self.jvm.emitGETFIELD(lexeme, self.getJVMType(in_))

    def emitPUTFIELD(self, lexeme: str, in_, frame) -> str:
        # lexeme: String
        # in_: Type
        # frame: Frame

        frame.pop()  # value
        frame.pop()  # objectref
        return self.jvm.emitPUTFIELD(lexeme, self.getJVMType(in_))

    """ generate code to invoke a static method
    *   @param lexeme the qualified name of the method(i.e., class-name/method-name)
    *   @param in the type descriptor of the method.
    """

    def emitINVOKESTATIC(self, lexeme: str, in_, frame) -> str:
        # lexeme: String
        # in_: Type
        # frame: Frame

        typ = in_
        list(map(lambda x: frame.pop(), typ.partype))
        if not type(typ.rettype) is VoidType:
            frame.push()
        return self.jvm.emitINVOKESTATIC(lexeme, self.getJVMType(in_))

    """ generate code to invoke a special method
    *   @param lexeme the qualified name of the method(i.e., class-name/method-name)
    *   @param in the type descriptor of the method.
    """

    def emitINVOKESPECIAL(
        self, frame, lexeme: Optional[str] = None, in_: Optional[Any] = None
    ) -> str:
        # lexeme: String
        # in_: Type
        # frame: Frame

        if not lexeme is None and not in_ is None:
            typ = in_
            list(map(lambda x: frame.pop(), typ.partype))
            frame.pop()
            if not type(typ.rettype) is VoidType:
                frame.push()
            return self.jvm.emitINVOKESPECIAL(lexeme, self.getJVMType(in_))
        elif lexeme is None and in_ is None:
            frame.pop()
            return self.jvm.emitINVOKESPECIAL()

    """ generate code to invoke a virtual method
    * @param lexeme the qualified name of the method(i.e., class-name/method-name)
    * @param in the type descriptor of the method.
    """

    def emitINVOKEVIRTUAL(self, lexeme: str, in_, frame) -> str:
        # lexeme: String
        # in_: Type
        # frame: Frame

        typ: MType = in_
        list(map(lambda x: frame.pop(), typ.partype))
        frame.pop()  # objectref
        if not type(typ) is VoidType:
            frame.push()
        return self.jvm.emitINVOKEVIRTUAL(lexeme, self.getJVMType(in_))

    """
    *   generate ineg, fneg.
    *   @param in the type of the operands.
    """

    def emitNEGOP(self, in_, frame) -> str:
        # in_: Type
        # frame: Frame
        # ..., value -> ..., result

        if type(in_) is IntType:
            return self.jvm.emitINEG()
        else:
            return self.jvm.emitFNEG()

    def emitNOT(self, in_, frame) -> str:
        # in_: Type
        # frame: Frame

        label1 = frame.getNewLabel()
        label2 = frame.getNewLabel()
        result = list()
        result.append(self.emitIFTRUE(label1, frame))
        result.append(self.emitPUSHCONST("true", in_, frame))
        result.append(self.emitGOTO(label2, frame))
        result.append(self.emitLABEL(label1, frame))
        result.append(self.emitPUSHCONST("false", in_, frame))
        result.append(self.emitLABEL(label2, frame))
        return "".join(result)

    """
    *   generate iadd, isub, fadd or fsub.
    *   @param lexeme the lexeme of the operator.
    *   @param in the type of the operands.
    """

    def emitADDOP(self, lexeme: str, in_, frame) -> str:
        # lexeme: String
        # in_: Type
        # frame: Frame
        # ..., value1, value2 -> ..., result

        frame.pop()  # value2
        frame.pop()  # value1
        frame.push()  # result
        if lexeme == "+":
            if type(in_) is IntType:
                return self.jvm.emitIADD()
            else:
                return self.jvm.emitFADD()
        else:
            if type(in_) is IntType:
                return self.jvm.emitISUB()
            else:
                return self.jvm.emitFSUB()

    """
    *   generate imul, idiv, fmul or fdiv.
    *   @param lexeme the lexeme of the operator.
    *   @param in the type of the operands.
    """

    def emitMULOP(self, lexeme: str, in_, frame) -> str:
        # lexeme: String
        # in_: Type
        # frame: Frame
        # ..., value1, value2 -> ..., result

        frame.pop()  # value2
        frame.pop()  # value1
        frame.push()  # result
        if lexeme == "*":
            if type(in_) is IntType:
                return self.jvm.emitIMUL()
            else:
                return self.jvm.emitFMUL()
        else:
            if type(in_) is IntType:
                return self.jvm.emitIDIV()
            else:
                return self.jvm.emitFDIV()

    def emitDIV(self, frame) -> str:
        # frame: Frame

        frame.pop()  # value2
        frame.pop()  # value1
        frame.push()  # result
        return self.jvm.emitIDIV()

    def emitMOD(self, frame) -> str:
        # frame: Frame

        frame.pop()  # value2
        frame.pop()  # value1
        frame.push()  # result
        # return "\tirem\n"
        return self.jvm.emitIREM()

    """
    *   generate iand
    """

    def emitANDOP(self, frame) -> str:
        # frame: Frame

        frame.pop()  # value2
        frame.pop()  # value1
        frame.push()  # result
        return self.jvm.emitIAND()

    """
    *   generate ior
    """

    def emitOROP(self, frame) -> str:
        # frame: Frame

        frame.pop()  # value2
        frame.pop()  # value1
        frame.push()  # result
        return self.jvm.emitIOR()

    def emitShortCircuitOROP(self, frame, operand2: AST, codeGen) -> str:
        # frame: Frame
        result = ""
        label1 = frame.getNewLabel()
        label2 = frame.getNewLabel()
        result += self.emitIFFALSE(label1, frame)
        result += self.emitPUSHCONST("true", BoolType(), frame)
        result += self.emitGOTO(label2)

        result += self.emitLABEL(label1)
        result += codeGen.visit(operand2, frame)
        result += self.emitLABEL(label2)
        return result

    def emitREOP(self, op: str, in_, frame) -> str:
        # op: String
        # in_: Type
        # frame: Frame
        # ..., value1, value2 -> ..., result

        result = list()
        labelF = frame.getNewLabel()
        labelO = frame.getNewLabel()

        frame.pop()  # value2
        frame.pop()  # value1
        if type(in_) is FloatType:
            result.append(self.jvm.emitFCMPL())
            frame.push()  # result
            result.append(self.jvm.emitICONST(0))
            frame.push()  # result
            frame.pop()  # value2
            frame.pop()  # value1

        if op == ">":
            result.append(self.jvm.emitIFICMPLE(labelF))
        elif op == ">=":
            result.append(self.jvm.emitIFICMPLT(labelF))
        elif op == "<":
            result.append(self.jvm.emitIFICMPGE(labelF))
        elif op == "<=":
            result.append(self.jvm.emitIFICMPGT(labelF))
        elif op == "!=":
            result.append(self.jvm.emitIFICMPEQ(labelF))
        elif op == "==":
            result.append(self.jvm.emitIFICMPNE(labelF))

        result.append(self.emitPUSHCONST("1", IntType(), frame))

        result.append(self.emitGOTO(labelO, frame))
        result.append(
            self.emitLABEL(labelF, frame)
        )  # False. Whenever a code jumps to labelF, it means the result is 0
        result.append(self.emitPUSHCONST("0", IntType(), frame))
        result.append(self.emitLABEL(labelO, frame))
        return "".join(result)

    def emitRELOP(self, op: str, in_, trueLabel: int, falseLabel: int, frame) -> str:
        # op: String
        # in_: Type
        # trueLabel: Int
        # falseLabel: Int
        # frame: Frame
        # ..., value1, value2 -> ..., result

        result = list()

        frame.pop()  # value2
        frame.pop()  # value1
        if op == ">":
            result.append(self.jvm.emitIFICMPLE(falseLabel))
            result.append(self.emitGOTO(trueLabel))
        elif op == ">=":
            result.append(self.jvm.emitIFICMPLT(falseLabel))
        elif op == "<":
            result.append(self.jvm.emitIFICMPGE(falseLabel))
        elif op == "<=":
            result.append(self.jvm.emitIFICMPGT(falseLabel))
        elif op == "!=":
            result.append(self.jvm.emitIFICMPEQ(falseLabel))
        elif op == "==":
            result.append(self.jvm.emitIFICMPNE(falseLabel))
        result.append(self.jvm.emitGOTO(trueLabel))
        return "".join(result)

    """   generate the method directive for a function.
    *   @param lexeme the qualified name of the method(i.e., class-name/method-name).
    *   @param in the type descriptor of the method.
    *   @param isStatic <code>true</code> if the method is static; <code>false</code> otherwise.
    """

    def emitMETHOD(self, lexeme: str, in_, isStatic: bool, frame) -> str:
        # lexeme: String
        # in_: Type
        # isStatic: Boolean
        # frame: Frame

        return self.jvm.emitMETHOD(lexeme, self.getJVMType(in_), isStatic)

    """   generate the end directive for a function.
    """

    def emitENDMETHOD(self, frame) -> str:
        # frame: Frame

        buffer = list()
        buffer.append(self.jvm.emitLIMITSTACK(frame.getMaxOpStackSize()))
        buffer.append(self.jvm.emitLIMITLOCAL(frame.getMaxIndex()))
        buffer.append(self.jvm.emitENDMETHOD())
        return "".join(buffer)

    def getConst(self, ast) -> Tuple[str, Any]:
        # ast: Literal
        if type(ast) is IntLiteral:
            return (str(ast.value), IntType())

    """   generate code to initialize a local array variable.<p>
    *   @param index the index of the local variable.
    *   @param in the type of the local array variable.
    """

    """   generate code to initialize local array variables.
    *   @param in the list of symbol entries corresponding to local array variable.    
    """

    """   generate code to jump to label if the value on top of operand stack is true.<p>
    *   ifgt label
    *   @param label the label where the execution continues if the value on top of stack is true.
    """

    def emitIFTRUE(self, label: int, frame) -> str:
        # label: Int
        # frame: Frame

        frame.pop()  # value
        return self.jvm.emitIFGT(label)

    """
    *   generate code to jump to label if the value on top of operand stack is false.<p>
    *   ifle label
    *   @param label the label where the execution continues if the value on top of stack is false.
    """

    def emitIFFALSE(self, label: int, frame) -> str:
        # label: Int
        # frame: Frame

        frame.pop()  # value
        return self.jvm.emitIFLE(label)

    def emitIFICMPGT(self, label: int, frame) -> str:
        # label: Int
        # frame: Frame

        frame.pop()  # value2
        frame.pop()  # value1
        return self.jvm.emitIFICMPGT(label)

    def emitIFICMPLT(self, label: int, frame) -> str:
        # label: Int
        # frame: Frame

        frame.pop()  # value2
        frame.pop()  # value1
        return self.jvm.emitIFICMPLT(label)

    """   generate code to duplicate the value on the top of the operand stack.<p>
    *   Stack:<p>
    *   Before: ...,value1<p>
    *   After:  ...,value1,value1<p>
    """

    def emitDUP(self, frame) -> str:
        # frame: Frame

        frame.push()
        return self.jvm.emitDUP()

    def emitPOP(self, frame) -> str:
        # frame: Frame

        frame.pop()
        return self.jvm.emitPOP()

    """   generate code to exchange an integer on top of stack to a floating-point number.
    """

    def emitI2F(self, frame) -> str:
        # frame: Frame

        frame.pop()  # value
        frame.push()  # result
        return self.jvm.emitI2F()

    """ generate code to return.
    *   <ul>
    *   <li>ireturn if the type is IntegerType or BooleanType
    *   <li>freturn if the type is RealType
    *   <li>return if the type is null
    *   </ul>
    *   @param in the type of the returned expression.
    """

    def emitRETURN(self, in_, frame) -> str:
        # in_: Type
        # frame: Frame

        if type(in_) is IntType or type(in_) is BoolType:
            frame.pop()
            return self.jvm.emitIRETURN()
        elif type(in_) is FloatType:
            frame.pop()
            return self.jvm.emitFRETURN()
        elif type(in_) is StringType:
            frame.pop()
            return self.jvm.emitARETURN()
        elif type(in_) is VoidType:
            return self.jvm.emitRETURN()

    """ generate code that represents a label	
    *   @param label the label
    *   @return code Label<label>:
    """

    def emitLABEL(self, label: int, frame) -> str:
        # label: Int
        # frame: Frame

        return self.jvm.emitLABEL(label)

    """ generate code to jump to a label	
    *   @param label the label
    *   @return code goto Label<label>
    """

    def emitGOTO(self, label: int, frame) -> str:
        # label: Int
        # frame: Frame

        return self.jvm.emitGOTO(str(label))

    """ generate some starting directives for a class.<p>
    *   .source MPC.CLASSNAME.java<p>
    *   .class public MPC.CLASSNAME<p>
    *   .super java/lang/Object<p>
    """

    def emitPROLOG(self, name: str, parent: str) -> str:
        # name: String
        # parent: String

        result = list()
        result.append(self.jvm.emitSOURCE(name + ".java"))
        result.append(self.jvm.emitCLASS("public " + name))
        result.append(
            self.jvm.emitSUPER("java/lang/Object" if parent == "" else parent)
        )
        return "".join(result)

    def emitLIMITSTACK(self, num: int) -> str:
        # num: Int

        return self.jvm.emitLIMITSTACK(num)

    def emitLIMITLOCAL(self, num: int) -> str:
        # num: Int

        return self.jvm.emitLIMITLOCAL(num)

    def emitEPILOG(self) -> None:
        file = open(self.filename, "w")
        file.write("".join(self.buff))
        file.close()

    """ print out the code to screen
    *   @param in the code to be printed out
    """

    def emitNEWARRAY(self, dimens: list, eleType: Type, value: NestedList, frame):
        logger = logging.getLogger(f"{'emitNEWARRAY':<20}")
        logger.debug("-" * 60)
        logger.debug(
            f"Emitting NEWARRAY with {dimens} dimensions, {eleType} type, values {value}"
        )

        result = list()
        result.append(self.emitPUSHCONST(str(dimens[0]), IntType(), frame))
        if len(dimens) == 1:
            frame.pop()  # dim
            frame.push()  # arrayref
            result.append(self.jvm.emitNEWARRAY(self.getFullType(eleType)))
            logger.debug(f"Pushing newarray {self.getJVMType(eleType)}")
        else:
            result.append(self.emitANEWARRAY(ArrayType(dimens[1:], eleType), frame))
        for i in range(len(value)):
            result.append(self.emitDUP(frame))
            result.append(self.emitPUSHCONST(str(i), IntType(), frame))
            if len(dimens) == 1:
                result.append(self.emitPUSHCONST(str(value[i]), eleType, frame))
                logger.debug(f"Pushing constant {value[i]} of type {type(value[i])}")
                result.append(self.emitASTORE(eleType, frame))
            else:
                result.append(self.emitNEWARRAY(dimens[1:], eleType, value[i], frame))
                result.append(self.emitASTORE(ArrayType(dimens[1:], eleType), frame))
        return "".join(result)

    def emitANEWARRAY(self, in_: ArrayType, frame):
        frame.pop()  # dim
        frame.push()  # objectref
        return self.jvm.emitANEWARRAY(self.getJVMType(in_))

    def emitMULTIANEWARRAY(self, in_, dimens, frame):
        result = list()
        for dim in dimens:
            result.append(self.emitPUSHCONST(str(dim), IntType(), frame))
            frame.pop()
        frame.push()
        result.append(self.jvm.emitMULTIANEWARRAY(self.getJVMType(in_), len(dimens)))
        return "".join(result)

    def emitNEW(self, name: str, frame):
        frame.push()  # objectref
        return self.jvm.emitNEW(name)

    def emitPUSHNULL(self, frame):
        frame.push()  # objectref
        return self.jvm.emitPUSHNULL()

    def emitINTERFACE(self, name, methods: List[Prototype], parent: str = ""):
        # name: String
        result = list()
        result.append(self.jvm.emitSOURCE(name + ".java"))
        result.append(self.jvm.emitINTERFACE(name))
        result.append(
            self.jvm.emitSUPER("java/lang/Object" if parent == "" else parent)
        )
        result.append("\n")
        for method in methods:
            result.append(
                ".method public abstract "
                + method.name
                + "("
                + "".join(list(map(lambda x: self.getJVMType(x), method.params)))
                + ")"
                + self.getJVMType(method.retType)
                + "\n"
            )
            result.append(".end method\n")
            result.append("\n")

        return "".join(result)

    def emitIMPLEMENTS(self, lexeme: str):
        return self.jvm.emitIMPLEMENTS(lexeme)

    def printout(self, in_: str) -> None:
        # in_: String

        self.buff.append(in_)

    def clearBuff(self) -> None:
        self.buff.clear()
