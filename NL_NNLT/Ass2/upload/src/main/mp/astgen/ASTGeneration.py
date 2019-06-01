from MPVisitor import MPVisitor
from MPParser import MPParser
from AST import *

class ASTGeneration(MPVisitor):
    
    def visitProgram(self, ctx:MPParser.ProgramContext):
        #program: (var_decl | func_decl | proc_decl)+ EOF; OK
        lst=[]
        vlst=list(map(self.visit,ctx.var_decl()))
        flst=list(map(self.visit,ctx.func_decl()))
        plst=list(map(self.visit,ctx.proc_decl()))
        for i in range(0,ctx.getChildCount()):
            if isinstance(ctx.getChild(i),MPParser.Var_declContext) and vlst:
                lst+=vlst.pop(0)
            elif isinstance(ctx.getChild(i),MPParser.Func_declContext) and flst:
                lst.append(flst.pop(0))
            elif isinstance(ctx.getChild(i),MPParser.Proc_declContext) and plst:
                lst.append(plst.pop(0))         
        return Program(lst)

    def visitVar_decl(self, ctx:MPParser.Var_declContext):
        #var_decl: VAR (list_vardecl SEMI)+ ; OKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK
        lst = []
        for x in ctx.list_vardecl():
            sublst = self.visit(x)
            lst +=sublst
        return lst;
        #return self.visit(x) for x in ctx.list_vardecl()

    def visitList_vardecl(self, ctx:MPParser.List_vardeclContext):
        #list_vardecl: IDENTIFIER (COMMA IDENTIFIER)* COLON type_a ; OKKKKKKKKKKKKKKKKKKK
        lst_ret = []
        for x in ctx.IDENTIFIER():
            lst_ret.append(VarDecl(Id(x.getText()),self.visit(ctx.type_a())))
        return lst_ret
        
        #return [VarDecl(Id(x.getText()), self.visit(ctx.type_a())) for x in ctx.IDENTIFIER()]

    def visitType_a(self, ctx:MPParser.Type_aContext):
        #type_a: primitive_type | compound_type ; OKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK
        return self.visit(ctx.primitive_type()) if ctx.primitive_type() else self.visit(ctx.compound_type())

    def visitPrimitive_type(self, ctx:MPParser.Primitive_typeContext):
        #primitive_type: STRING | BOOLEAN | INTEGER | REAL ; OKKKKKKKKKKKKKKKKK

        if ctx.STRING():
            return StringType()
        elif ctx.BOOLEAN():
            return BoolType()
        elif ctx.INTEGER():
            return IntType()
        else:
            return FloatType()

    def visitCompound_type(self, ctx:MPParser.Compound_typeContext):
        #compound_type: ARRAY LSB SUB? INT_LIT DD SUB? INT_LIT RSB OF primitive_type ; OKKKKKKKKKKKKKKKKK
        lower = ctx.INT_LIT(0).getText()
        upper = ctx.INT_LIT(1).getText()
        if ctx.SUB(0):
            lower = '-' + lower
        if ctx.SUB(1):
            upper = '-' + upper

        return ArrayType(int(lower),int(upper),self.visit(ctx.primitive_type()))

    def visitFunc_decl(self, ctx:MPParser.Func_declContext):
        #func_decl: FUNCTION IDENTIFIER LB listpara? RB COLON type_a SEMI var_decl? comp_statement? ;
        param = self.visit(ctx.listpara()) if ctx.listpara() else []
        local = self.visit(ctx.var_decl()) if ctx.var_decl() else []
        body = self.visit(ctx.comp_statement())

        return FuncDecl(Id(ctx.IDENTIFIER().getText()), param, local, body, self.visit(ctx.type_a()))

    def visitListpara(self, ctx:MPParser.ListparaContext):
        #listpara: list_vardecl (SEMI list_vardecl)* ;
        lst = []
        for x in ctx.list_vardecl():
            lst += self.visit(x)

        return lst

    def visitProc_decl(self, ctx:MPParser.Proc_declContext):
        #proc_decl: PROCEDURE IDENTIFIER LB listpara? RB SEMI var_decl? comp_statement? ;
        param = self.visit(ctx.listpara()) if ctx.listpara() else []
        local = self.visit(ctx.var_decl()) if ctx.var_decl() else []
        body = self.visit(ctx.comp_statement()) if ctx.comp_statement() else []

        return FuncDecl(Id(ctx.IDENTIFIER().getText()), param, local, body)

    def visitComp_statement(self, ctx:MPParser.Comp_statementContext):
        #comp_statement: BEGIN (statement)* END ;
        '''lst = []
        for x in ctx.statement():
            lst += self.visit(x)

        return lst'''

        lst = []
        for x in ctx.statement():
            sublst = self.visit(x)

            if not isinstance(sublst,list):
                sublst = [sublst]
            lst+=sublst

        for x in lst:
            if isinstance(x,list):
                if(len(x)==0):
                    lst.remove(x) 
        return lst 

    def visitStatement(self, ctx:MPParser.StatementContext):
        #statement:  match_statement | unmatch_statement ;
        if ctx.match_statement():
            return self.visit(ctx.match_statement())
        elif ctx.unmatch_statement():
            return self.visit(ctx.unmatch_statement())

    def visitMatch_statement(self, ctx:MPParser.Match_statementContext):
        #match_statement: IF expression THEN match_statement ELSE match_statement | other ;
        if ctx.getChildCount()==6:
            exp_ = self.visit(ctx.expression())
            thenStmt_ = self.visit(ctx.match_statement(0))
            elseStmt_ = self.visit(ctx.match_statement(1))

            if not isinstance(thenStmt_,list):
                thenStmt_=[thenStmt_]
            if not isinstance(elseStmt_,list):
                elseStmt_=[elseStmt_]

            return If(exp_,thenStmt_,elseStmt_)
       
        else: return self.visit(ctx.other())

    def visitOther(self, ctx:MPParser.OtherContext):
        #other: assignment_state|while_state|for_state|break_state|continue_state|return_state|comp_statement|with_state|call_state SEMI
        return self.visit(ctx.getChild(0))

    def visitAssignment_state(self, ctx:MPParser.Assignment_stateContext):
        #assignment_state: (lhs ASSIGN)+ expression SEMI
        lst = [self.visit(x) for x in ctx.lhs()]
        lst = lst + [self.visit(ctx.expression())]
        n = lst.__len__() - 1
        return [Assign(lst[x-1],lst[x]) for x in range(n,0,-1)]

        #[Assign(lst[x], lst[x-1]) for x in range(lst.__len__() - 1, 0, -1)]
    
    def visitLhs(self, ctx:MPParser.LhsContext):
        #lhs: (IDENTIFIER|index_expression) ;
        if ctx.IDENTIFIER():
            return Id(ctx.IDENTIFIER().getText())
        else:
            print("M muon gi")
            return self.visit(ctx.index_expression())

        #return Id(ctx.IDENTIFIER().getText()) if ctx.IDENTIFIER() else self.visit(ctx.index_expression())

    def visitWhile_state(self, ctx:MPParser.While_stateContext):
        #while_state: WHILE expression DO statement
        return While(self.visit(ctx.expression()), self.visit(ctx.statement()))

    def visitFor_state(self, ctx:MPParser.For_stateContext):
        #for_state: FOR IDENTIFIER ASSIGN expression (TO|DOWNTO) expression DO statement
        if ctx.TO():
            up = True
        else:
            up = False

        return For(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.expression(0)), self.visit(ctx.expression(1)), up, self.visit(ctx.statement()))

    def visitBreak_state(self, ctx:MPParser.Break_stateContext):
        #break_state: BREAK SEMI;
        return Break()

    def visitContinue_state(self, ctx:MPParser.Continue_stateContext):
        #continue_state: CONTINUE SEMI;
        return Continue()

    def visitReturn_state(self, ctx:MPParser.Return_stateContext):
        #return_state: RETURN expression? SEMI;
        return Return(self.visit(ctx.expression()) if ctx.expression() else [])

    def visitWith_state(self, ctx:MPParser.With_stateContext):
        #with_state: WITH listpara SEMI DO statement ;
        return With(self.visit(ctx.listpara()), self.visit(ctx.statement()))

    def visitCall_state(self, ctx:MPParser.Call_stateContext):
        #call_state: IDENTIFIER LB list_expression? RB ;
        return CallStmt(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.list_expression()) if ctx.list_expression() else [])

    def visitUnmatch_statement(self, ctx:MPParser.Unmatch_statementContext):
        #unmatch_statement: IF expression THEN statement| IF expression THEN match_statement ELSE unmatch_statement
        if ctx.getChildCount() == 4:
            return If(self.visit(ctx.expression()), self.visit(ctx.statement()))
        else:
            return If(self.visit(ctx.expression()), self.visit(ctx.match_statement()), self.visit(ctx.unmatch_statement()))

    def visitExpression(self, ctx:MPParser.ExpressionContext):
        #expression: expression AND THEN expression1| expression OR ELSE expression1| expression1

        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression1())
        elif ctx.AND():
            return BinaryOp("andthen", self.visit(ctx.expression()), self.visit(ctx.expression1()))
        elif ctx.OR():
            return BinaryOp("orelse", self.visit(ctx.expression()), self.visit(ctx.expression1()))

    def visitExpression1(self, ctx:MPParser.Expression1Context):
        #expression1:expression2 EQ expression2| expression2 NOTEQ expression2| expression2 LESS expression2
        #| expression2 GREATER expression2| expression2 LEQ expression2| expression2 GEQ expression2 | expression2
        if ctx.EQ():
            return BinaryOp("=", self.visit(ctx.expression2(0)), self.visit(ctx.expression2(1)))
        elif ctx.NOTEQ():
            return BinaryOp("<>", self.visit(ctx.expression2(0)), self.visit(ctx.expression2(1)))
        elif ctx.LESS():
            return BinaryOp("<", self.visit(ctx.expression2(0)), self.visit(ctx.expression2(1)))
        elif ctx.GREATER():
            return BinaryOp(">", self.visit(ctx.expression2(0)), self.visit(ctx.expression2(1)))
        elif ctx.LEQ():
            return BinaryOp("<=", self.visit(ctx.expression2(0)), self.visit(ctx.expression2(1)))
        elif ctx.GEQ():
            return BinaryOp(">=", self.visit(ctx.expression2(0)), self.visit(ctx.expression2(1)))
        else:
            return self.visit(ctx.expression2(0)) #ctx.expression2() thì error


    def visitExpression2(self, ctx:MPParser.Expression2Context):
        #expression2:expression2 ADD expression3| expression2 SUB expression3| expression2 OR expression3| expression3
        
        if ctx.ADD():
            return BinaryOp("+", self.visit(ctx.expression2()), self.visit(ctx.expression3()))
        elif ctx.SUB():
            return BinaryOp("-", self.visit(ctx.expression2()), self.visit(ctx.expression3()))
        elif ctx.OR():
            return BinaryOp("or", self.visit(ctx.expression2()), self.visit(ctx.expression3()))
        else:

            return self.visit(ctx.expression3())

    def visitExpression3(self, ctx:MPParser.Expression3Context):
        #expression3:expression3 DIVISION expression4| expression3 MUL expression4| expression3 DIV expression4 
        #| expression3 MOD expression4| expression3 AND expression4| expression4
        if ctx.DIVISION():
            return BinaryOp("/", self.visit(ctx.expression3()), self.visit(ctx.expression4()))
        elif ctx.MUL():
            return BinaryOp("*", self.visit(ctx.expression3()), self.visit(ctx.expression4()))
        elif ctx.DIV():
            return BinaryOp("div", self.visit(ctx.expression3()), self.visit(ctx.expression4()))
        elif ctx.MOD():
            return BinaryOp("mod", self.visit(ctx.expression3()), self.visit(ctx.expression4()))
        elif ctx.AND():
            return BinaryOp("and", self.visit(ctx.expression3()), self.visit(ctx.expression4()))
        else:
            return self.visit(ctx.expression4())

    def visitExpression4(self, ctx:MPParser.Expression4Context):
        #expression4:SUB expression4| NOT expression4| expression5
        if ctx.SUB():
            return UnaryOp("-", self.visit(ctx.expression4()))
        elif ctx.NOT():
            return UnaryOp("not", self.visit(ctx.expression4()))
        else:
            return self.visit(ctx.expression5())

    def visitExpression5(self, ctx:MPParser.Expression5Context):
        #expression5: expression6 LSB expression RSB| expression6

        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression6())
        else:
            return ArrayCell(self.visit(ctx.expression6()), self.visit(ctx.expression()))
        

    def visitExpression6(self, ctx:MPParser.Expression6Context):
        #expression6: IDENTIFIER| literal| call_state| LB expression RB
        if ctx.IDENTIFIER():
            return Id(ctx.IDENTIFIER().getText())
        elif ctx.literal():
            return self.visit(ctx.literal())
        elif ctx.call_state():
            return self.visit(ctx.call_state())
        else:
            return self.visit(ctx.expression())

    def visitLiteral(self, ctx:MPParser.LiteralContext):
        #literal:INT_LIT | BOOL_LIT | REAL_LIT | STRING_LIT
        if ctx.INT_LIT():
            return IntLiteral(int(ctx.INT_LIT().getText()))
        elif ctx.BOOL_LIT():
            return BooleanLiteral(bool(ctx.BOOL_LIT().getText()))
        elif ctx.REAL_LIT():
            return FloatLiteral(float(ctx.REAL_LIT().getText()))
        else:
            return StringLiteral(ctx.STRING_LIT().getText())

    def visitIndex_expression(self, ctx:MPParser.Index_expressionContext):
        #index_expression: (IDENTIFIER|call_state) LSB expression RSB

        if ctx.call_state():
            arr = self.visit(ctx.call_state())
        else:
            print("khohieu")
            arr = Id(ctx.IDENTIFIER().getText())
        
        
        return ArrayCell(arr)

    def visitList_expression(self, ctx:MPParser.List_expressionContext):
        #list_expression: expression (COMMA expression)* ;
        lst = []
        for x in ctx.expression():
            sublst = self.visit(x)
            lst.append(sublst)

        return lst