#TRAN QUANG NHAT - 1612402
from MPVisitor import MPVisitor
from MPParser import MPParser
from AST import *
from functools import reduce

class ASTGeneration(MPVisitor):

	def visitProgram(self, ctx:MPParser.ProgramContext):
		lst=[]
		vlst=list(map(self.visit,ctx.variableDeclaration()))
		flst=list(map(self.visit,ctx.functionDeclaration()))
		plst=list(map(self.visit,ctx.procedureDeclaration()))
		for i in range(0,ctx.getChildCount()):
			if isinstance(ctx.getChild(i),MPParser.VariableDeclarationContext) and vlst:
				lst+=vlst.pop(0)
			elif isinstance(ctx.getChild(i),MPParser.FunctionDeclarationContext) and flst:
				lst.append(flst.pop(0))
			elif isinstance(ctx.getChild(i),MPParser.ProcedureDeclarationContext) and plst:
				lst.append(plst.pop(0))			
		return Program(lst)

	def visitVariableDeclaration(self, ctx:MPParser.VariableDeclarationContext):
		#VAR varList+
		lst = []
		for x in ctx.varList():
		 	sublst = self.visit(x)
		 	lst+=sublst
		return lst

	def visitVarList(self, ctx:MPParser.VarListContext):
		#IDENT (COMMA IDENT)* COLON types SEMI
		lst =  [VarDecl(Id(x.getText()),self.visit(ctx.types())) for x in ctx.IDENT()]
		return lst

	def visitFunctionDeclaration(self, ctx:MPParser.FunctionDeclarationContext):
		#FUNCTION IDENT LB formalParameterList? RB COLON types SEMI variableDeclaration? BEGIN compoundStatement END
		local = self.visit(ctx.variableDeclaration()) if ctx.variableDeclaration() else []
		param = self.visit(ctx.formalParameterList()) if ctx.formalParameterList() else []
		body = self.visit(ctx.compoundStatement())
		return FuncDecl(Id(ctx.IDENT().getText()),param,local,body,self.visit(ctx.types()))
	
	def visitFormalParameterList(self, ctx:MPParser.FormalParameterListContext):
		#listParam (SEMI listParam)*
		lst = []
		for x in ctx.listParam():
			sublst = self.visit(x)
			lst += sublst
		return lst

	def visitListParam(self, ctx:MPParser.ListParamContext):
		#IDENT (COMMA IDENT)* COLON types
		lst = [VarDecl(Id(x.getText()),self.visit(ctx.types())) for x in ctx.IDENT()]
		return lst

	def visitTypes(self, ctx:MPParser.TypesContext):
		if ctx.primitiveTypes():
			return self.visit(ctx.primitiveTypes())
		else:
			return self.visit(ctx.compoundTypes())
	
	def visitPrimitiveTypes(self, ctx:MPParser.PrimitiveTypesContext):
		if ctx.BOOLEAN():
			return BoolType()
		elif ctx.INTEGER():
			return IntType()
		elif ctx.REAL():
			return FloatType()
		else:
			return StringType()
	
	def visitCompoundTypes(self, ctx:MPParser.CompoundTypesContext):
		#ARRAY LSB (SUB? unsignedInteger) DDOT (SUB? unsignedInteger) RSB OF primitiveTypes
		lower = ctx.unsignedInteger(0).getText() if ctx.SUB(0) is None else "-" + ctx.unsignedInteger(0).getText()
		upper = ctx.unsignedInteger(1).getText() if ctx.SUB(1) is None else "-" + ctx.unsignedInteger(1).getText()
		return ArrayType(lower,upper,self.visit(ctx.primitiveTypes()))
	
	def visitUnsignedInteger(self, ctx:MPParser.UnsignedIntegerContext):
		return IntLiteral(int(ctx.NUM_INT().getText()))

	def visitExpression(self, ctx:MPParser.ExpressionContext):
		if(ctx.getChildCount() == 3):
			if ctx.andthen():
				return BinaryOp("andthen",self.visit(ctx.expression()),self.visit(ctx.expression1()))
			else:
				return BinaryOp("orelse",self.visit(ctx.expression()),self.visit(ctx.expression1()))
		else:
			return self.visit(ctx.expression1())
	
	def visitExpression1(self, ctx:MPParser.Expression1Context):
		if(ctx.getChildCount() == 3):
			if ctx.EQ():
				return BinaryOp("=",self.visit(ctx.simpleExpression1(0)),self.visit(ctx.simpleExpression1(1)))
			elif ctx.NOTEQ():
				return BinaryOp("<>",self.visit(ctx.simpleExpression1(0)),self.visit(ctx.simpleExpression1(1)))
			elif ctx.LESS():
				return BinaryOp("<",self.visit(ctx.simpleExpression1(0)),self.visit(ctx.simpleExpression1(1)))
			elif ctx.GREATER():
				return BinaryOp(">",self.visit(ctx.simpleExpression1(0)),self.visit(ctx.simpleExpression1(1)))
			elif ctx.LEQ():
				return BinaryOp("<=",self.visit(ctx.simpleExpression1(0)),self.visit(ctx.simpleExpression1(1)))
			else:
				return BinaryOp(">=",self.visit(ctx.simpleExpression1(0)),self.visit(ctx.simpleExpression1(1)))
		else:
			return self.visit(ctx.simpleExpression1(0))
	
	def visitSimpleExpression1(self, ctx:MPParser.SimpleExpression1Context):
		if(ctx.getChildCount() == 3):
			if ctx.PLUS():
				return BinaryOp("+",self.visit(ctx.simpleExpression1()),self.visit(ctx.simpleExpression2()))
			elif ctx.SUB():	
				return BinaryOp("-",self.visit(ctx.simpleExpression1()),self.visit(ctx.simpleExpression2()))
			else:
				return BinaryOp("or",self.visit(ctx.simpleExpression1()),self.visit(ctx.simpleExpression2()))
		else:
			return self.visit(ctx.simpleExpression2())
	
	def visitSimpleExpression2(self, ctx:MPParser.SimpleExpression2Context):
		if(ctx.getChildCount() == 3):
			if ctx.DI():
				return BinaryOp("/",self.visit(ctx.simpleExpression2()),self.visit(ctx.prefixExpression()))
			elif ctx.MUL():
				return BinaryOp("*",self.visit(ctx.simpleExpression2()),self.visit(ctx.prefixExpression()))
			elif ctx.DIV():
				return BinaryOp("div",self.visit(ctx.simpleExpression2()),self.visit(ctx.prefixExpression()))
			elif ctx.MOD():
				return BinaryOp("mod",self.visit(ctx.simpleExpression2()),self.visit(ctx.prefixExpression()))
			elif ctx.AND():
				return BinaryOp("and",self.visit(ctx.simpleExpression2()),self.visit(ctx.prefixExpression()))
		else:
			return self.visit(ctx.prefixExpression())

	def visitPrefixExpression(self, ctx:MPParser.PrefixExpressionContext):
		if(ctx.SUB()):
			return UnaryOp("-",self.visit(ctx.prefixExpression()))
		elif(ctx.NOT()):
			return UnaryOp("not",self.visit(ctx.prefixExpression()))
		else:
			return self.visit(ctx.factor())
	
	def visitFactor(self, ctx:MPParser.FactorContext):
		if(ctx.identifier()):
			return self.visit(ctx.identifier())
		elif(ctx.literals()):
			return self.visit(ctx.literals())
		elif(ctx.indexExpression()):
			return self.visit(ctx.indexExpression())
		elif(ctx.boolean()):
			return self.visit(ctx.boolean())
		elif(ctx.invocationExpression()):
			return self.visit(ctx.invocationExpression())
		else:
			return self.visit(ctx.expression())

		
	def visitLiterals(self, ctx:MPParser.LiteralsContext):
		if(ctx.unsignedInteger()):
			return self.visit(ctx.unsignedInteger())
		elif(ctx.unsignedReal()):
			return self.visit(ctx.unsignedReal())
		else:
			return self.visit(ctx.string())
	
	def visitUnsignedInteger(self, ctx:MPParser.UnsignedIntegerContext):
		return IntLiteral(ctx.NUM_INT().getText())
	
	def visitStatements(self, ctx:MPParser.StatementsContext):
		if(ctx.ifStatement()):
			return self.visit(ctx.ifStatement())
		if(ctx.assignment()):
			return self.visit(ctx.assignment())
		if(ctx.whileStatement()):
			return self.visit(ctx.whileStatement())
		if(ctx.forStatement()):
			return self.visit(ctx.forStatement())
		if(ctx.callStatement()):
			return self.visit(ctx.callStatement())
		if(ctx.compoundStatement()):
			return self.visit(ctx.compoundStatement())
		if(ctx.returnStatement()):
			return self.visit(ctx.returnStatement())
		if(ctx.withdoStatement()):
			return self.visit(ctx.withdoStatement())
		if(ctx.continueandbreak()):
			return self.visit(ctx.continueandbreak())
	
	def visitCallStatement(self, ctx:MPParser.CallStatementContext):
		lst = [self.visit(x) for x in ctx.expression()]
		return [CallStmt(self.visit(ctx.identifier()),lst)]
		

	def visitContinueandbreak(self, ctx:MPParser.ContinueandbreakContext):
		if(ctx.continueStatement()):
			return [Continue()]
		else:
			return [Break()]

	def visitWithdoStatement(self, ctx:MPParser.WithdoStatementContext):
		#WITH formalParameterList SEMI DO statements
		return [With(self.visit(ctx.formalParameterList()),self.visit(ctx.statements()))]

	def visitAssignment(self, ctx:MPParser.AssignmentContext):
		#(leftHandSides Assign)+ rightHandSides SEMI
		lst = [self.visit(x) for x in ctx.leftHandSides()]
		lst = lst + [self.visit(ctx.rightHandSides())]
		n = lst.__len__() - 1
		return [Assign(lst[x-1],lst[x]) for x in range(n,0,-1)] 
		#lhsleft = [self.visit(x) for x in ctx.leftHandSides()][::-1]
		#return [reduce(lambda x,y: Assign(y,x), lhsleft, self.visit(ctx.rightHandSides()))]
		

	def visitIfStatement(self, ctx:MPParser.IfStatementContext):
		#IF expression THEN statements (ELSE statements)?
		thenstm = self.visit(ctx.statements(0))
		if(ctx.statements(1)):
			elstm = self.visit(ctx.statements(1))
		else:
			elstm = []
		return [If(self.visit(ctx.expression()),thenstm,elstm)]
	
	def visitWhileStatement(self, ctx:MPParser.WhileStatementContext):
		#WHILE expression DO statements
		return [While(self.visit(ctx.expression()),self.visit(ctx.statements()))]
	
	def visitForStatement(self, ctx:MPParser.ForStatementContext):
		#FOR identifier Assign expression (TO|DOWNTO) expression DO statements
		if (ctx.TO()):
			up = "True"
		else:
			up = "False"
		return [For(self.visit(ctx.identifier()),self.visit(ctx.expression(0)),self.visit(ctx.expression(1)),up,self.visit(ctx.statements()))]
	
	
	def visitReturnStatement(self, ctx:MPParser.ReturnStatementContext):
		if(ctx.getChildCount()==2):
			return [Return()]
		else:
			return [Return(self.visit(ctx.expression()))]

	def visitRightHandSides(self, ctx:MPParser.RightHandSidesContext):
		return self.visit(ctx.expression())

	def visitLeftHandSides(self, ctx:MPParser.LeftHandSidesContext):
		if(ctx.identifier()):
			return self.visit(ctx.identifier())
		if(ctx.indexExpression()):
			return self.visit(ctx.indexExpression())
		
	
	def visitCompoundStatement(self, ctx:MPParser.CompoundStatementContext):
		lst = []
		for x in ctx.statements():
			lst = lst + self.visit(x)
		return lst	
		#return [self.visit(x) for x in ctx.statements()]

	def visitIdentifier(self, ctx:MPParser.IdentifierContext):
		return Id(ctx.IDENT().getText())
	
	def visitProcedureDeclaration(self, ctx:MPParser.ProcedureDeclarationContext):
		#PROCEDURE identifier LB formalParameterList? RB SEMI variableDeclaration? compoundStatement
		local = self.visit(ctx.variableDeclaration()) if ctx.variableDeclaration() else []
		param = self.visit(ctx.formalParameterList()) if ctx.formalParameterList() else []
		body = self.visit(ctx.compoundStatement())
		return FuncDecl(Id(ctx.IDENT().getText()),param,local,body,VoidType())
	
	def visitIndexExpression(self, ctx:MPParser.IndexExpressionContext):
		if(ctx.indexArray()):
			return self.visit(ctx.indexArray())
		if(ctx.indexFunctionArray()):
			return self.visit(ctx.indexFunctionArray())

	def visitIndexFunctionArray(self, ctx:MPParser.IndexFunctionArrayContext):
		#functionCall LSB index RSB
		return ArrayCell(self.visit(ctx.functionCall()),self.visit(ctx.index()))
	
	def visitIndexArray(self, ctx:MPParser.IndexArrayContext):
		#identifier LSB index RSB
		return ArrayCell(self.visit(ctx.identifier()),self.visit(ctx.index()))

	def visitIndex(self, ctx:MPParser.IndexContext):
		if(ctx.expression()):
			return self.visit(ctx.expression())
		if(ctx.unsignedInteger()):
			return self.visit(ctx.unsignedInteger())
		if(ctx.indexExpression()):
			return self.visit(ctx.indexExpression())

	def visitBoolean(self, ctx:MPParser.BooleanContext):
		if(ctx.TRUE()):
			return BooleanLiteral(True)
		else:
			return BooleanLiteral(False)
	
	def visitInvocationExpression(self, ctx:MPParser.InvocationExpressionContext):
		lst = [self.visit(x) for x in ctx.expression()]
		return CallExpr(self.visit(ctx.identifier()),lst)
	
	def visitFunctionCall(self, ctx:MPParser.FunctionCallContext):
		#identifier LB (expression (COMMA expression)*)? RB
		lst = [self.visit(x) for x in ctx.expression()]
		return CallExpr(self.visit(ctx.identifier()),lst)
	
	def visitString(self, ctx:MPParser.StringContext):
		return StringLiteral(ctx.STRING_LITERAL().getText())

	def visitUnsignedReal(self, ctx:MPParser.UnsignedRealContext):
		return FloatLiteral(float(ctx.NUM_REAL().getText()))
	
		








		
		
				
			
        
	