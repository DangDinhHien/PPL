# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BKOOLParser import BKOOLParser
else:
    from BKOOLParser import BKOOLParser

# This class defines a complete generic visitor for a parse tree produced by BKOOLParser.

class BKOOLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BKOOLParser#program.
    def visitProgram(self, ctx:BKOOLParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#class_decl.
    def visitClass_decl(self, ctx:BKOOLParser.Class_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#list_of_members.
    def visitList_of_members(self, ctx:BKOOLParser.List_of_membersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#attribute.
    def visitAttribute(self, ctx:BKOOLParser.AttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#constant_decl.
    def visitConstant_decl(self, ctx:BKOOLParser.Constant_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#variable_decl.
    def visitVariable_decl(self, ctx:BKOOLParser.Variable_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#id_list.
    def visitId_list(self, ctx:BKOOLParser.Id_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#method.
    def visitMethod(self, ctx:BKOOLParser.MethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#list_of_para.
    def visitList_of_para(self, ctx:BKOOLParser.List_of_paraContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#para.
    def visitPara(self, ctx:BKOOLParser.ParaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#type_lit.
    def visitType_lit(self, ctx:BKOOLParser.Type_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#primitive_type.
    def visitPrimitive_type(self, ctx:BKOOLParser.Primitive_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#array_type.
    def visitArray_type(self, ctx:BKOOLParser.Array_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#class_type.
    def visitClass_type(self, ctx:BKOOLParser.Class_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp.
    def visitExp(self, ctx:BKOOLParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp1.
    def visitExp1(self, ctx:BKOOLParser.Exp1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp2.
    def visitExp2(self, ctx:BKOOLParser.Exp2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp3.
    def visitExp3(self, ctx:BKOOLParser.Exp3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp4.
    def visitExp4(self, ctx:BKOOLParser.Exp4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp5.
    def visitExp5(self, ctx:BKOOLParser.Exp5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp6.
    def visitExp6(self, ctx:BKOOLParser.Exp6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp7.
    def visitExp7(self, ctx:BKOOLParser.Exp7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp8.
    def visitExp8(self, ctx:BKOOLParser.Exp8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp9.
    def visitExp9(self, ctx:BKOOLParser.Exp9Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp10.
    def visitExp10(self, ctx:BKOOLParser.Exp10Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp11.
    def visitExp11(self, ctx:BKOOLParser.Exp11Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#literals.
    def visitLiterals(self, ctx:BKOOLParser.LiteralsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#index_exp.
    def visitIndex_exp(self, ctx:BKOOLParser.Index_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#member_access.
    def visitMember_access(self, ctx:BKOOLParser.Member_accessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#instance_attribute.
    def visitInstance_attribute(self, ctx:BKOOLParser.Instance_attributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#static_attribute.
    def visitStatic_attribute(self, ctx:BKOOLParser.Static_attributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#object_creation.
    def visitObject_creation(self, ctx:BKOOLParser.Object_creationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#statement.
    def visitStatement(self, ctx:BKOOLParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#match_state.
    def visitMatch_state(self, ctx:BKOOLParser.Match_stateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#unmatch_state.
    def visitUnmatch_state(self, ctx:BKOOLParser.Unmatch_stateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#other_state.
    def visitOther_state(self, ctx:BKOOLParser.Other_stateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#block_state.
    def visitBlock_state(self, ctx:BKOOLParser.Block_stateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#assign_state.
    def visitAssign_state(self, ctx:BKOOLParser.Assign_stateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#lhs.
    def visitLhs(self, ctx:BKOOLParser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#local_variable.
    def visitLocal_variable(self, ctx:BKOOLParser.Local_variableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#for_state.
    def visitFor_state(self, ctx:BKOOLParser.For_stateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#scalar_variable.
    def visitScalar_variable(self, ctx:BKOOLParser.Scalar_variableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#break_state.
    def visitBreak_state(self, ctx:BKOOLParser.Break_stateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#continue_state.
    def visitContinue_state(self, ctx:BKOOLParser.Continue_stateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#return_state.
    def visitReturn_state(self, ctx:BKOOLParser.Return_stateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#method_invo_state.
    def visitMethod_invo_state(self, ctx:BKOOLParser.Method_invo_stateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#instance_method.
    def visitInstance_method(self, ctx:BKOOLParser.Instance_methodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#static_method.
    def visitStatic_method(self, ctx:BKOOLParser.Static_methodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#list_exp.
    def visitList_exp(self, ctx:BKOOLParser.List_expContext):
        return self.visitChildren(ctx)



del BKOOLParser