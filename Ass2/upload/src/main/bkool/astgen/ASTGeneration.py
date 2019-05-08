from BKOOLVisitor import BKOOLVisitor
from BKOOLParser import BKOOLParser
from AST import *

class ASTGeneration(BKOOLVisitor):

    def visitProgram(self, ctx:BKOOLParser.ProgramContext):
    	return Program([self.visit(x) for x in ctx.class_decl()])

    def visitClass_decl(self, ctx:BKOOLParser.Class_declContext):
    	#class_decl: CLASS ID (EXTENDS ID)? LP list_of_members? RP ;
    	temp = Id(ctx.ID(1).getText()) if ctx.ID(1) else None
    	param = self.visit(ctx.list_of_members()) if ctx.list_of_members() else []
    	return ClassDecl(Id(ctx.ID(0).getText()), param, temp)

    def visitList_of_members(self,ctx:BKOOLParser.List_of_membersContext):
    	#list_of_members: (attribute | method)+ ;
    	lst = []
    	for i in range(0, ctx.getChildCount()):
    		if ctx.attribute(i):
    			temp = self.visit(ctx.attribute(i))
    			if not isinstance(temp,list):
    				temp = [temp]
    			lst += temp
    		elif ctx.method(i): 	
    			temp = self.visit(ctx.method(i))
    			if not isinstance(temp,list):
    				temp = [temp]
    			lst += temp

    	return lst

    def visitAttribute(self, ctx:BKOOLParser.AttributeContext):
    	#attribute: variable_decl | constant_decl ;
    	return self.visit(ctx.variable_decl()) if ctx.variable_decl() else self.visit(ctx.constant_decl())

    def visitConstant_decl(self, ctx:BKOOLParser.Constant_declContext):
    	#constant_decl: STATIC? FINAL type_lit ID OP_BANG exp SEMICOLONE;
    	temp = Static() if ctx.STATIC() else Instance()
    	return AttributeDecl(temp, ConstDecl(Id(ctx.ID().getText()), self.visit(ctx.type_lit()), self.visit(ctx.exp())))

    def visitVariable_decl(self, ctx:BKOOLParser.Variable_declContext):
    	#variable_decl: STATIC? id_list COLON type_lit SEMICOLONE ;
    	temp = Static() if ctx.STATIC() else Instance()
    	kq = [AttributeDecl(temp, VarDecl(Id(x.getText()), self.visit(ctx.type_lit()))) for x in self.visit(ctx.id_list())]
    	
    			
    	return kq

    def visitId_list(self, ctx:BKOOLParser.Id_listContext):
    	#id_list: ID (COMMA ID)* ;
    	return [x for x in ctx.ID()]

    def visitMethod(self, ctx:BKOOLParser.MethodContext):
    	#method: (type_lit | VOID)? STATIC? ID LB list_of_para? RB block_state ;
    	#list_of_para: para (SEMICOLONE para)* ;
		#para: id_list COLON type_lit;
    	temp = Static() if ctx.STATIC() else Instance()   
    	############# param = list(VarDecl)
    	paramTemp = self.visit(ctx.list_of_para()) if ctx.list_of_para() else []
    	if ctx.list_of_para() and isinstance(paramTemp[0], list):
    		param = paramTemp[0]
    	else:
    		param = paramTemp
    	####################
    	returnType = self.visit(ctx.type_lit()) if ctx.type_lit() else VoidType()
    	return MethodDecl(temp, Id(ctx.ID().getText()), param, returnType, self.visit(ctx.block_state()))

    def visitList_of_para(self, ctx:BKOOLParser.List_of_paraContext):
    	#list_of_para: para (SEMICOLONE para)* ;
    	return [self.visit(x) for x in ctx.para()]

    def visitPara(self, ctx:BKOOLParser.ParaContext):
    	#para: id_list COLON type_lit;
    	return [VarDecl(Id(x.getText()), self.visit(ctx.type_lit())) for x in self.visit(ctx.id_list())]

    def visitType_lit(self, ctx:BKOOLParser.Type_litContext):
    	#type_lit: primitive_type | array_type | class_type ;
    	return self.visit(ctx.getChild(0))

    def visitPrimitive_type(self, ctx:BKOOLParser.Primitive_typeContext):
    	#primitive_type: INT | FLOAT | BOOLEAN | STRING ;
    	if ctx.INT():
    		return IntType()
    	elif ctx.FLOAT():
    		return FloatType()
    	elif ctx.BOOLEAN():
    		return BoolType()
    	elif ctx.STRING():
    		return StringType()

    def visitArray_type(self, ctx:BKOOLParser.Array_typeContext):
    	#array_type: (ID | primitive_type) LSB (INTEGERLIT | ID) RSB ;
    	eleType = self.visit(ctx.primitive_type()) if ctx.primitive_type() else ClassType(ctx.ID(0).getText())
    	######## ID xem xet lai bi thieu
    	size = IntLiteral(int(ctx.INTEGERLIT().getText())) if ctx.INTEGERLIT() else Id(ctx.ID(0).getText()) if ctx.primitive_type() else Id(ctx.ID(1).getText())
    	return ArrayType(size, eleType)

    def visitClass_type(self, ctx:BKOOLParser.Class_typeContext):
    	#class_type: ID | NIL; 
    	return ClassType(ctx.getChild(0).getText())

    def visitExp(self, ctx:BKOOLParser.ExpContext):
       	#exp:exp1 LESS exp1| exp1 GREATER exp1| exp1 LESSEQ exp1| exp1 GREATEREQ exp1| exp1;
    	if ctx.getChildCount() == 3:
    		return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.getChild(0)), self.visit(ctx.getChild(2)))
    	else:
    		return self.visit(ctx.getChild(0))

    def visitExp1(self, ctx:BKOOLParser.Exp1Context):
       	#exp1:exp2 EQ exp2| exp2 NOTEQ exp2| exp2;
    	if ctx.getChildCount() == 3:
    		return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.getChild(0)), self.visit(ctx.getChild(2)))
    	else:
    		return self.visit(ctx.getChild(0))

    def visitExp2(self, ctx:BKOOLParser.Exp2Context):
    	if ctx.getChildCount() == 3:
    		return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.getChild(0)), self.visit(ctx.getChild(2)))
    	else:
    		return self.visit(ctx.getChild(0))



    def visitExp3(self, ctx:BKOOLParser.Exp3Context):
    	if ctx.getChildCount() == 3:
    		return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.getChild(0)), self.visit(ctx.getChild(2)))
    	else:
    		return self.visit(ctx.getChild(0))

    def visitExp4(self, ctx:BKOOLParser.Exp4Context):
    	if ctx.getChildCount() == 3:
    		return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.getChild(0)), self.visit(ctx.getChild(2)))
    	else:
    		return self.visit(ctx.getChild(0))  

    def visitExp5(self, ctx:BKOOLParser.Exp5Context):
    	if ctx.getChildCount() == 3:
    		return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.getChild(0)), self.visit(ctx.getChild(2)))
    	else:
    		return self.visit(ctx.getChild(0)) 

    def visitExp6(self, ctx:BKOOLParser.Exp6Context):
    	if ctx.getChildCount() == 2:
    		return UnaryOp(ctx.getChild(0).getText(), self.visit(ctx.getChild(1)))
    	else:
    		return self.visit(ctx.getChild(0))

    def visitExp7(self, ctx:BKOOLParser.Exp7Context):
    	if ctx.getChildCount() == 2:
    		return UnaryOp(ctx.getChild(0).getText(), self.visit(ctx.getChild(1)))
    	else:
    		return self.visit(ctx.getChild(0))

    def visitExp8(self, ctx:BKOOLParser.Exp8Context):
    	if ctx.getChildCount() == 3:
    		return self.visit(ctx.getChild(1))
    	else:
    		return self.visit(ctx.getChild(0))

    def visitExp9(self, ctx:BKOOLParser.Exp9Context):
    	if ctx.getChildCount() == 3:
    		return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.getChild(0)), self.visit(ctx.getChild(2)))
    	else:
    		return self.visit(ctx.getChild(0)) 

    def visitExp10(self, ctx:BKOOLParser.Exp10Context):
    	if ctx.getChildCount() == 2:
    		return UnaryOp(ctx.getChild(0).getText(), self.visit(ctx.getChild(1)))
    	else:
    		return self.visit(ctx.getChild(0))

    def visitExp11(self, ctx:BKOOLParser.Exp11Context):
    	#ID| literals| index_exp| member_access| object_creation| THIS| LB exp? RB
    	if ctx.ID():
    		return Id(ctx.ID().getText())
    	elif ctx.literals():
    		return self.visit(ctx.literals())
    	elif ctx.index_exp():
    		return self.visit(ctx.index_exp())
    	elif ctx.member_access():
    		return self.visit(ctx.member_access())
    	elif ctx.object_creation():
    		return self.visit(ctx.object_creation())
    	elif ctx.THIS():
    		return SelfLiteral(ctx.THIS().getText())
    	else:
    		return self.visit(ctx.exp()) if ctx.exp() else []

    def visitLiterals(self, ctx:BKOOLParser.LiteralsContext):
    	#literals: INTEGERLIT| FLOATLIT| BOOLLIT| STRINGLIT
    	if ctx.INTEGERLIT():
    		return IntLiteral(int(ctx.INTEGERLIT().getText()))
    	elif ctx.FLOATLIT():
    		return FloatLiteral(float(ctx.FLOATLIT().getText()))
    	elif ctx.BOOLLIT():
    		return BooleanLiteral(bool(ctx.BOOLLIT().getText()))
    	elif ctx.STRINGLIT():
    		return StringLiteral(str(ctx.STRINGLIT().getText()))

    def visitIndex_exp(self, ctx:BKOOLParser.Index_expContext):
    	#index_exp: (ID | member_access) LSB exp RSB;
    	if ctx.ID():
    		arr = Id(ctx.ID().getText())
    	else:
    		arr = self.visit(ctx.member_access())

    	idx = self.visit(ctx.exp())
    	return ArrayCell(arr, idx)

    def visitMember_access(self, ctx:BKOOLParser.Member_accessContext):
    	#member_access:instance_attribute| static_attribute| instance_method| static_method
    	return self.visit(ctx.getChild(0))

    def visitInstance_attribute(self, ctx:BKOOLParser.Instance_attributeContext):
    	#instance_attribute: (ID | THIS) DOT ID LB list_exp? RB DOT ID ;
    	###### return FieldAccess()
    	obj = SelfLiteral() if ctx.THIS() else Id(ctx.ID(0).getText())
    	tempId = Id(ctx.ID(0).getText()) if ctx.THIS() else Id(ctx.ID(1).getText()) 
    	param = self.visit(ctx.list_exp()) if ctx.list_exp() else []
    	tempId1 = Id(ctx.ID(1).getText()) if ctx.THIS() else Id(ctx.ID(2).getText()) 
    	#return CallExpr(obj, tempId, param)

    	return FieldAccess(CallExpr(obj, tempId, param), tempId1)

    def visitStatic_attribute(self, ctx:BKOOLParser.Static_attributeContext):
    	obj = SelfLiteral() if ctx.THIS() else Id(ctx.ID(0).getText())
    	tempId = Id(ctx.ID(0).getText()) if ctx.THIS() else Id(ctx.ID(1).getText()) 
    	
    	return FieldAccess(obj, tempId)

    def visitInstance_method(self, ctx:BKOOLParser.Instance_methodContext):
    	#instance_method: (ID | THIS) DOT ID LB list_exp? RB DOT ID LB list_exp? RB; // Them DOT ID
    	obj = SelfLiteral() if ctx.THIS() else Id(ctx.ID(0).getText())
    	tempId = Id(ctx.ID(0).getText()) if ctx.THIS() else Id(ctx.ID(1).getText()) 
    	#param = self.visit(ctx.list_exp(0)) if ctx.list_exp(1) else []
    	if ctx.getChild(4) == ctx.RB(0):
    		param = []
    		if ctx.getChild(8) == ctx.RB(1):
    			param2 = []
    		else:
    			param2 = self.visit(ctx.list_exp(0))
    	else:
    		param = self.visit(ctx.list_exp(0))
    		if ctx.getChild(9) == ctx.RB(1):
    			param2 = []
    		else:
    			param2 = self.visit(ctx.list_exp(1))
    	######
    	tempId1 = Id(ctx.ID(1).getText()) if ctx.THIS() else Id(ctx.ID(2).getText())
    	###param2 = self.visit(ctx.list_exp(1)) if ctx.list_exp(1) else []
    	return CallExpr(CallExpr(obj, tempId, param), tempId1, param2)

    def visitStatic_method(self, ctx:BKOOLParser.Static_methodContext):
    	#static_method: (ID | THIS) DOT ID LB list_exp? RB ;
    	obj = SelfLiteral() if ctx.THIS() else Id(ctx.ID(0).getText())
    	tempId = Id(ctx.ID(0).getText()) if ctx.THIS() else Id(ctx.ID(1).getText()) 
    	param = self.visit(ctx.list_exp()) if ctx.list_exp() else []

    	return CallExpr(obj, tempId, param)

    def visitInstance_method_state(self, ctx:BKOOLParser.Instance_method_stateContext):
    	#instance_method: (ID | THIS) DOT ID LB list_exp? RB DOT ID LB list_exp? RB; // Them DOT ID
    	obj = SelfLiteral() if ctx.THIS() else Id(ctx.ID(0).getText())
    	tempId = Id(ctx.ID(0).getText()) if ctx.THIS() else Id(ctx.ID(1).getText()) 
    	#param = self.visit(ctx.list_exp(0)) if ctx.list_exp(1) else []
    	if ctx.getChild(4) == ctx.RB(0):
    		param = []
    		if ctx.getChild(8) == ctx.RB(1):
    			param2 = []
    		else:
    			param2 = self.visit(ctx.list_exp(0))
    	else:
    		param = self.visit(ctx.list_exp(0))
    		if ctx.getChild(9) == ctx.RB(1):
    			param2 = []
    		else:
    			param2 = self.visit(ctx.list_exp(1))
    	######
    	tempId1 = Id(ctx.ID(1).getText()) if ctx.THIS() else Id(ctx.ID(2).getText())
    	###param2 = self.visit(ctx.list_exp(1)) if ctx.list_exp(1) else []
    	return CallStmt(CallExpr(obj, tempId, param), tempId1, param2)

    def visitStatic_method_state(self, ctx:BKOOLParser.Static_method_stateContext):
    	#static_method_state: (ID | THIS) DOT ID LB list_exp? RB ;
    	obj = SelfLiteral() if ctx.THIS() else Id(ctx.ID(0).getText())
    	tempId = Id(ctx.ID(0).getText()) if ctx.THIS() else Id(ctx.ID(1).getText()) 
    	param = self.visit(ctx.list_exp()) if ctx.list_exp() else []

    	return CallStmt(obj, tempId, param)


    def visitObject_creation(self, ctx:BKOOLParser.Object_creationContext):
    	#object_creation: NEW ID LB list_exp? RB ;

    	return NewExpr(Id(ctx.ID().getText()), self.visit(ctx.list_exp()) if ctx.list_exp() else [])

    def visitList_exp(self, ctx:BKOOLParser.List_expContext):
    	#list_exp: exp (COMMA exp)* ;

    	return [self.visit(x) for x in ctx.exp()]

    def visitStatement(self, ctx:BKOOLParser.StatementContext):
    	return self.visit(ctx.getChild(0))

    def visitMatch_state(self, ctx:BKOOLParser.Match_stateContext):
    	#match_state:IF exp THEN match_state ELSE match_state| other_state
    	if ctx.getChildCount() == 1:
    		return self.visit(ctx.getChild(0))
    	else:
    		return If(self.visit(ctx.exp()), self.visit(ctx.match_state(0)), self.visit(ctx.match_state(1)))

    def visitUnmatch_state(self, ctx:BKOOLParser.Unmatch_stateContext):
    	#unmatch_state:IF exp THEN statement| IF exp THEN match_state ELSE unmatch_state
    	if ctx.getChildCount() == 4:
    		return If(self.visit(ctx.exp()), self.visit(ctx.statement()), [])
    	else:
    		return If(self.visit(ctx.exp()), self.visit(ctx.match_state()), self.visit(ctx.unmatch_state()))

    def visitOther_state(self, ctx:BKOOLParser.Other_stateContext):
    	return self.visit(ctx.getChild(0))

    def visitBlock_state(self, ctx:BKOOLParser.Block_stateContext):
    	#block_state: LP attribute* statement* RP ;
    	att = [self.visit(x) for x in ctx.attribute()]
    	## Chu y xet cho nay
    	temp = []
    	for i in range(0,len(att)):
    		if isinstance(att[i],list):
    			for j in range(0,len(att[i])):
    				temp.append(att[i][j])
    	state = [self.visit(x) for x in ctx.statement()]
    	return Block(temp, state)

    def visitAssign_state(self, ctx:BKOOLParser.Assign_stateContext):
    	#assign_state: lhs ASSIGN exp SEMICOLONE ;
    	return Assign(self.visit(ctx.lhs()), self.visit(ctx.exp()))

    def visitLhs(self, ctx:BKOOLParser.LhsContext):
    	#lhs: local_variable | variable_decl | array_type ;
    	return self.visit(ctx.getChild(0))

    def visitLocal_variable(self, ctx:BKOOLParser.Local_variableContext):
    	#local_variable: THIS DOT ID | ID;
    	if ctx.getChildCount() == 1:
    		return Id(ctx.ID().getText())
    	else:
    		return FieldAccess(SelfLiteral(), Id(ctx.ID().getText())) 

    def visitFor_state(self, ctx:BKOOLParser.For_stateContext):
    	#for_state: FOR scalar_variable ASSIGN exp (TO|DOWNTO) exp DO statement
    	up = "True" if ctx.TO() else "False"
    	return For(self.visit(ctx.scalar_variable()), self.visit(ctx.exp(0)), self.visit(ctx.exp(1)), up, self.visit(ctx.statement()))

    def visitScalar_variable(self, ctx:BKOOLParser.Scalar_variableContext):
    	return Id(ctx.ID().getText())

    def visitBreak_state(self, ctx:BKOOLParser.Break_stateContext):
    	return Break()

    def visitContinue_state(self, ctx:BKOOLParser.Continue_stateContext):
    	return Continue()

    def visitReturn_state(self, ctx:BKOOLParser.Return_stateContext):
    	return Return(self.visit(ctx.exp()))

    def visitMethod_invo_state(self, ctx:BKOOLParser.Method_invo_stateContext):
    	return self.visit(ctx.getChild(0))
