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


    # Visit a parse tree produced by MPParser#variable_decalation.
    def visitVariable_decalation(self, ctx:MPParser.Variable_decalationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#list_of_declaration.
    def visitList_of_declaration(self, ctx:MPParser.List_of_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#type_data.
    def visitType_data(self, ctx:MPParser.Type_dataContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#primitive_type.
    def visitPrimitive_type(self, ctx:MPParser.Primitive_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#compound_type.
    def visitCompound_type(self, ctx:MPParser.Compound_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#list_of_id.
    def visitList_of_id(self, ctx:MPParser.List_of_idContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#function_declaration.
    def visitFunction_declaration(self, ctx:MPParser.Function_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#procedure_declaration.
    def visitProcedure_declaration(self, ctx:MPParser.Procedure_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#stat.
    def visitStat(self, ctx:MPParser.StatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#match_stat.
    def visitMatch_stat(self, ctx:MPParser.Match_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#other_stat.
    def visitOther_stat(self, ctx:MPParser.Other_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#unmatch_stat.
    def visitUnmatch_stat(self, ctx:MPParser.Unmatch_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#assign_stat.
    def visitAssign_stat(self, ctx:MPParser.Assign_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#while_stat.
    def visitWhile_stat(self, ctx:MPParser.While_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#for_stat.
    def visitFor_stat(self, ctx:MPParser.For_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#break_stat.
    def visitBreak_stat(self, ctx:MPParser.Break_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#continue_stat.
    def visitContinue_stat(self, ctx:MPParser.Continue_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#return_stat.
    def visitReturn_stat(self, ctx:MPParser.Return_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#with_stat.
    def visitWith_stat(self, ctx:MPParser.With_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#call_stat.
    def visitCall_stat(self, ctx:MPParser.Call_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#compound_stat.
    def visitCompound_stat(self, ctx:MPParser.Compound_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#exp.
    def visitExp(self, ctx:MPParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#exp1.
    def visitExp1(self, ctx:MPParser.Exp1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#exp2.
    def visitExp2(self, ctx:MPParser.Exp2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#exp3.
    def visitExp3(self, ctx:MPParser.Exp3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#exp4.
    def visitExp4(self, ctx:MPParser.Exp4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#exp5.
    def visitExp5(self, ctx:MPParser.Exp5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#exp6.
    def visitExp6(self, ctx:MPParser.Exp6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#literals.
    def visitLiterals(self, ctx:MPParser.LiteralsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#call_exp.
    def visitCall_exp(self, ctx:MPParser.Call_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#index_exp.
    def visitIndex_exp(self, ctx:MPParser.Index_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#list_of_exp.
    def visitList_of_exp(self, ctx:MPParser.List_of_expContext):
        return self.visitChildren(ctx)



del MPParser