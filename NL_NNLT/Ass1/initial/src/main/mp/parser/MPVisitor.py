# Generated from main/mp/parser/MP.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MPParser import MPParser
else:
    from MPParser import MPParser

# This class defines a complete generic visitor for a parse tree produced by MPParser.

class MPVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MPParser#program.
    def visitProgram(self, ctx:MPParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#decl_pro.
    def visitDecl_pro(self, ctx:MPParser.Decl_proContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#var_decl.
    def visitVar_decl(self, ctx:MPParser.Var_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#list_vardecl.
    def visitList_vardecl(self, ctx:MPParser.List_vardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#type_a.
    def visitType_a(self, ctx:MPParser.Type_aContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#primitive_type.
    def visitPrimitive_type(self, ctx:MPParser.Primitive_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#compound_type.
    def visitCompound_type(self, ctx:MPParser.Compound_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#func_decl.
    def visitFunc_decl(self, ctx:MPParser.Func_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#listpara.
    def visitListpara(self, ctx:MPParser.ListparaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#proc_decl.
    def visitProc_decl(self, ctx:MPParser.Proc_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#comp_statement.
    def visitComp_statement(self, ctx:MPParser.Comp_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#statement.
    def visitStatement(self, ctx:MPParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#match_statement.
    def visitMatch_statement(self, ctx:MPParser.Match_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#other.
    def visitOther(self, ctx:MPParser.OtherContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#assignment_state.
    def visitAssignment_state(self, ctx:MPParser.Assignment_stateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#while_state.
    def visitWhile_state(self, ctx:MPParser.While_stateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#for_state.
    def visitFor_state(self, ctx:MPParser.For_stateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#break_state.
    def visitBreak_state(self, ctx:MPParser.Break_stateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#continue_state.
    def visitContinue_state(self, ctx:MPParser.Continue_stateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#return_state.
    def visitReturn_state(self, ctx:MPParser.Return_stateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#with_state.
    def visitWith_state(self, ctx:MPParser.With_stateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#call_state.
    def visitCall_state(self, ctx:MPParser.Call_stateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#unmatch_statement.
    def visitUnmatch_statement(self, ctx:MPParser.Unmatch_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#expression.
    def visitExpression(self, ctx:MPParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#expression1.
    def visitExpression1(self, ctx:MPParser.Expression1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#expression2.
    def visitExpression2(self, ctx:MPParser.Expression2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#expression3.
    def visitExpression3(self, ctx:MPParser.Expression3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#expression4.
    def visitExpression4(self, ctx:MPParser.Expression4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#expression5.
    def visitExpression5(self, ctx:MPParser.Expression5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#literal.
    def visitLiteral(self, ctx:MPParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#index_expression.
    def visitIndex_expression(self, ctx:MPParser.Index_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#list_expression.
    def visitList_expression(self, ctx:MPParser.List_expressionContext):
        return self.visitChildren(ctx)



del MPParser