# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MiniGoParser import MiniGoParser
else:
    from MiniGoParser import MiniGoParser

# This class defines a complete generic visitor for a parse tree produced by MiniGoParser.

class MiniGoVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MiniGoParser#program.
    def visitProgram(self, ctx:MiniGoParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#many_declarations.
    def visitMany_declarations(self, ctx:MiniGoParser.Many_declarationsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#declaration.
    def visitDeclaration(self, ctx:MiniGoParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#varDeclaration.
    def visitVarDeclaration(self, ctx:MiniGoParser.VarDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#constDeclaration.
    def visitConstDeclaration(self, ctx:MiniGoParser.ConstDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#funcDeclaration.
    def visitFuncDeclaration(self, ctx:MiniGoParser.FuncDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#paramList.
    def visitParamList(self, ctx:MiniGoParser.ParamListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#param.
    def visitParam(self, ctx:MiniGoParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#multiID.
    def visitMultiID(self, ctx:MiniGoParser.MultiIDContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#methodDeclaration.
    def visitMethodDeclaration(self, ctx:MiniGoParser.MethodDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#methodReceiver.
    def visitMethodReceiver(self, ctx:MiniGoParser.MethodReceiverContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#structDeclaration.
    def visitStructDeclaration(self, ctx:MiniGoParser.StructDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#structFields.
    def visitStructFields(self, ctx:MiniGoParser.StructFieldsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#field.
    def visitField(self, ctx:MiniGoParser.FieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#interfaceDeclaration.
    def visitInterfaceDeclaration(self, ctx:MiniGoParser.InterfaceDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#methodSignatures.
    def visitMethodSignatures(self, ctx:MiniGoParser.MethodSignaturesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#methodSignature.
    def visitMethodSignature(self, ctx:MiniGoParser.MethodSignatureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#block.
    def visitBlock(self, ctx:MiniGoParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#stmtList.
    def visitStmtList(self, ctx:MiniGoParser.StmtListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#statement.
    def visitStatement(self, ctx:MiniGoParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#assignStmt.
    def visitAssignStmt(self, ctx:MiniGoParser.AssignStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#lhs.
    def visitLhs(self, ctx:MiniGoParser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#assignmentOp.
    def visitAssignmentOp(self, ctx:MiniGoParser.AssignmentOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#ifStmt.
    def visitIfStmt(self, ctx:MiniGoParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#ifElseStmt.
    def visitIfElseStmt(self, ctx:MiniGoParser.IfElseStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#forStmt.
    def visitForStmt(self, ctx:MiniGoParser.ForStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#forExpr.
    def visitForExpr(self, ctx:MiniGoParser.ForExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#forLoop.
    def visitForLoop(self, ctx:MiniGoParser.ForLoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#forRange.
    def visitForRange(self, ctx:MiniGoParser.ForRangeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#scalarDecl.
    def visitScalarDecl(self, ctx:MiniGoParser.ScalarDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#scalarAssign.
    def visitScalarAssign(self, ctx:MiniGoParser.ScalarAssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#breakStmt.
    def visitBreakStmt(self, ctx:MiniGoParser.BreakStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#continueStmt.
    def visitContinueStmt(self, ctx:MiniGoParser.ContinueStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#callStmt.
    def visitCallStmt(self, ctx:MiniGoParser.CallStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#returnStmt.
    def visitReturnStmt(self, ctx:MiniGoParser.ReturnStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#primitiveType.
    def visitPrimitiveType(self, ctx:MiniGoParser.PrimitiveTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#baseType.
    def visitBaseType(self, ctx:MiniGoParser.BaseTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#typeSpec.
    def visitTypeSpec(self, ctx:MiniGoParser.TypeSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#literal.
    def visitLiteral(self, ctx:MiniGoParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#notArrayLiteral.
    def visitNotArrayLiteral(self, ctx:MiniGoParser.NotArrayLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arrayLiteral.
    def visitArrayLiteral(self, ctx:MiniGoParser.ArrayLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arrayBody.
    def visitArrayBody(self, ctx:MiniGoParser.ArrayBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arrayType.
    def visitArrayType(self, ctx:MiniGoParser.ArrayTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arrayDim.
    def visitArrayDim(self, ctx:MiniGoParser.ArrayDimContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arrayList.
    def visitArrayList(self, ctx:MiniGoParser.ArrayListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arrayMember.
    def visitArrayMember(self, ctx:MiniGoParser.ArrayMemberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#structLiteral.
    def visitStructLiteral(self, ctx:MiniGoParser.StructLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#structElements.
    def visitStructElements(self, ctx:MiniGoParser.StructElementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#structElement.
    def visitStructElement(self, ctx:MiniGoParser.StructElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#exprList.
    def visitExprList(self, ctx:MiniGoParser.ExprListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expression.
    def visitExpression(self, ctx:MiniGoParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr1.
    def visitExpr1(self, ctx:MiniGoParser.Expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr2.
    def visitExpr2(self, ctx:MiniGoParser.Expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#compOp.
    def visitCompOp(self, ctx:MiniGoParser.CompOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr3.
    def visitExpr3(self, ctx:MiniGoParser.Expr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#addOp.
    def visitAddOp(self, ctx:MiniGoParser.AddOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr4.
    def visitExpr4(self, ctx:MiniGoParser.Expr4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#mulOp.
    def visitMulOp(self, ctx:MiniGoParser.MulOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr5.
    def visitExpr5(self, ctx:MiniGoParser.Expr5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr6.
    def visitExpr6(self, ctx:MiniGoParser.Expr6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr7.
    def visitExpr7(self, ctx:MiniGoParser.Expr7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#funcCall.
    def visitFuncCall(self, ctx:MiniGoParser.FuncCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#methodCall.
    def visitMethodCall(self, ctx:MiniGoParser.MethodCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#integer.
    def visitInteger(self, ctx:MiniGoParser.IntegerContext):
        return self.visitChildren(ctx)



del MiniGoParser