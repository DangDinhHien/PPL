from MPVisitor import MPVisitor
from MPParser import MPParser
from AST import *

class ASTGeneration(MPVisitor):
    def visitProgram(self,ctx:MPParser.ProgramContext):
        lst = []
        vlist = list(map(self.visit,ctx.variable_decalation()))
        plist = list(map(self.visit,ctx.procedure_declaration()))
        flist = list(map(self.visit,ctx.function_declaration()))
        for i in range(0,ctx.getChildCount()):
            if isinstance(ctx.getChild(i),MPParser.Variable_decalationContext) and vlist:
                lst+=vlist.pop(0)
            elif isinstance(ctx.getChild(i),MPParser.Function_declarationContext) and flist:
                lst.append(flist.pop(0))
            elif isinstance(ctx.getChild(i),MPParser.Procedure_declarationContext) and plist:
                lst.append(plist.pop(0))

        return Program(lst)


    def visitVariable_decalation(self,ctx:MPParser.Variable_decalationContext):
        lst = []
        for x in ctx.list_of_declaration():
            sublst = self.visit(x)
            lst +=sublst
        return lst;

    def visitList_of_declaration(self,ctx:MPParser.List_of_declarationContext):

        lst = self.visit(ctx.list_of_id()) 
        lst_ret = []
        for x in lst:
            lst_ret.append(VarDecl(x,self.visit(ctx.type_data())))
        return lst_ret

    def visitList_of_id(self,ctx:MPParser.List_of_idContext):
        lst = []
        lst_temp = []
        for x in ctx.ID():
            if (x.getText() in lst_temp): continue
            else:
                lst_temp.append(x.getText())
                lst.append(Id(x.getText()))
        return lst

    def visitType_data(self,ctx:MPParser.Type_dataContext):
        if ctx.primitive_type():
            return self.visit(ctx.primitive_type())
        else: return self.visit(ctx.compound_type())
    
    def visitPrimitive_type(self,ctx:MPParser.Primitive_typeContext):
        if ctx.INTTYPE():
            return IntType()
        elif ctx.REALTYPE():
            return FloatType()
        elif ctx.STRINGTYPE():
            return StringType()
        else : return BoolType()
   
    def visitCompound_type(self,ctx:MPParser.Compound_typeContext):
        lower = ctx.INTLIT(0).getText()
        upper = ctx.INTLIT(1).getText()
        if ctx.SUB_OP(0):
            lower = '-'+lower
        if ctx.SUB_OP(1):
            upper = '-'+upper

        return ArrayType(int(lower),int(upper),self.visit(ctx.primitive_type()))

    # function declaration

    def visitFunction_declaration(self,ctx:MPParser.Function_declarationContext):
        param = []
        for x in ctx.list_of_declaration():
            param+=self.visit(x);
        local_var_list = self.visit(ctx.variable_decalation()) if ctx.variable_decalation() else []

        compound_stmt = self.visit(ctx.compound_stat())
        return_type = self.visit(ctx.type_data())
        return FuncDecl(Id(ctx.ID().getText()),param,local_var_list,compound_stmt,return_type)
    #procedure declaration
    def visitProcedure_declaration(self,ctx:MPParser.Procedure_declarationContext):
        param = []
        for x in ctx.list_of_declaration():
            param+=self.visit(x);
        local_var_list = self.visit(ctx.variable_decalation()) if ctx.variable_decalation() else []
        compound_stmt = self.visit(ctx.compound_stat())
        return FuncDecl(Id(ctx.ID().getText()),param,local_var_list,compound_stmt)
    def visitCompound_stat(self,ctx:MPParser.Compound_statContext):
        
        lst = []
        for x in ctx.stat():
            sublst = self.visit(x)

            if not isinstance(sublst,list):
                sublst = [sublst]
            lst+=sublst

        for x in lst:
            if isinstance(x,list):
                if(len(x)==0):
                    lst.remove(x) 
        return lst 
        #return [self.visit(x) for x in ctx.stat()]

    def visitStat(self,ctx:MPParser.StatContext):
        if ctx.match_stat():
            return self.visit(ctx.match_stat())
        elif ctx.unmatch_stat():
            return self.visit(ctx.unmatch_stat())
    def visitMatch_stat(self,ctx:MPParser.Match_statContext):
        if ctx.getChildCount()==6:
            exp_ = self.visit(ctx.exp())
            thenStmt_ = self.visit(ctx.match_stat(0))
            elseStmt_ = self.visit(ctx.match_stat(1))

            if not isinstance(thenStmt_,list):
                thenStmt_=[thenStmt_]
            if not isinstance(elseStmt_,list):
                elseStmt_=[elseStmt_]

            return If(exp_,thenStmt_,elseStmt_)
       
        else: return self.visit(ctx.other_stat())

    def visitUnmatch_stat(self,ctx:MPParser.Unmatch_statContext):
        
        if ctx.getChildCount()==4:
            exp = self.visit(ctx.exp())
            thenStmt = self.visit(ctx.stat())
            if not isinstance(thenStmt,list):
                thenStmt=[thenStmt]

            return If(exp,thenStmt)

        elif ctx.getChildCount()==6:    
            exp_ = self.visit(ctx.exp())
            thenStmt_ = self.visit(ctx.match_stat())
            elseStmt_ = self.visit(ctx.unmatch_stat())

            if not isinstance(thenStmt_,list):
                thenStmt_=[thenStmt_]
            
            if not isinstance(elseStmt_,list):
                elseStmt_=[elseStmt_]
            
            return If(exp_,thenStmt_,elseStmt_)

    def visitOther_stat(self,ctx:MPParser.Other_statContext):
        return self.visit(ctx.getChild(0))
    
    def visitCall_stat(self,ctx:MPParser.Call_statContext):
        param_list = (self.visit(ctx.list_of_exp()) if ctx.list_of_exp() else [])
        return CallStmt(Id(ctx.ID().getText()),param_list)
    
    def visitContinue_stat(self,ctx:MPParser.Continue_statContext):
        return Continue()
    
    def visitBreak_stat(self,ctx:MPParser.Break_statContext):
        return Break()
   
    def visitWhile_stat(self,ctx:MPParser.While_statContext):
        exp = self.visit(ctx.exp())    #exxp
        sl = self.visit(ctx.stat())     #list(Stmt)
        # check sl is list?
        if(not isinstance(sl,list)):
            sl = [sl]
        return While(exp,sl)

    def visitReturn_stat(self,ctx:MPParser.Return_statContext):
        expr = self.visit(ctx.exp()) if ctx.exp() else None
        return Return(expr)

    def visitFor_stat(self,ctx:MPParser.For_statContext):
        id_ = Id(ctx.ID().getText())
        expr1 = self.visit(ctx.exp(0))
        expr2 = self.visit(ctx.exp(1))
        up = True if ctx.TO() else False
        loop = self.visit(ctx.stat())     #list(Stmt)
        # check loop is list?
        if(not isinstance(loop,list)):
            loop = [loop]
        return For(id_,expr1,expr2,up,loop)   
    def visitAssign_stat(self,ctx:MPParser.Assign_statContext):
        #return []
        lst = []
        l = ctx.getChildCount()-4
        rhs = self.visit(ctx.exp())
        while l>=0:
            lhs = Id(ctx.getChild(l).getText()) if not isinstance(ctx.getChild(l),MPParser.Index_expContext) else self.visit(ctx.getChild(l))
            sublst = [Assign(lhs,rhs)]
            lst += sublst
            l -= 2
            rhs = lhs
        return lst
    def visitWith_stat(self,ctx:MPParser.With_statContext):
        #decl:list(VarDecl)
        #stmt:list(Stmt)
        decl = []
        for x in ctx.list_of_declaration():
            decl+=self.visit(x)
        stmt=self.visit(ctx.stat())
        if(not isinstance(stmt,list)):
            stmt = [stmt]
        return With(decl,stmt)



    # expression
    def visitList_of_exp(self,ctx:MPParser.List_of_expContext):
        lst = []
        for x in ctx.exp():
            sublst = self.visit(x)
            lst.append(sublst)
        return lst

    def visitExp(self,ctx:MPParser.ExpContext):
        if ctx.getChildCount()==1:
            return self.visit(ctx.exp1())
        elif ctx.AND():
            return BinaryOp("andthen",self.visit(ctx.exp()),self.visit(ctx.exp1()))
        elif ctx.OR():
            return BinaryOp("orelse",self.visit(ctx.exp()),self.visit(ctx.exp1()))
    def visitExp1(self,ctx:MPParser.Exp1Context):
        if ctx.getChildCount()==1:
            return self.visit(ctx.getChild(0))
        else:
            return BinaryOp(ctx.getChild(1).getText(),self.visit(ctx.exp2(0)),self.visit(ctx.exp2(1)))
    
    def visitExp2(self,ctx:MPParser.Exp2Context):
        if ctx.getChildCount()==1:
            return self.visit(ctx.getChild(0))
        else:
            return BinaryOp(ctx.getChild(1).getText(),self.visit(ctx.exp2()),self.visit(ctx.exp3()))
    
    def visitExp3(self,ctx:MPParser.Exp3Context):
        if ctx.getChildCount()==1:
            return self.visit(ctx.getChild(0))
        else:
            return BinaryOp(ctx.getChild(1).getText(),self.visit(ctx.exp3()),self.visit(ctx.exp4()))
    
    def visitExp4(self,ctx:MPParser.Exp4Context):
        if ctx.getChildCount()==1:
            return self.visit(ctx.getChild(0))
        else:
            return UnaryOp(ctx.getChild(0).getText(),self.visit(ctx.exp4()))
    
    # def visitExp5(self,ctx:MPParser.Exp5Context):
    #     if ctx.exp():
    #         return ArrayCell(self.visit(ctx.exp6()),self.visit(ctx.exp()))
    #     else : return self.visit(ctx.getChild(0))
    # def visitExp6(self,ctx:MPParser.Exp6Context):
    #     if ctx.exp6():
    #         return self.visit(ctx.exp6())
    #     elif ctx.ID() : 
    #         return Id(ctx.ID().getText())
    #     elif ctx.call_exp():
    #         return self.visit(ctx.call_exp())
    #     elif ctx.exp7():
    #         return self.visit(ctx.exp7())


    # def visitExp7(self,ctx:MPParser.Exp7Context):
    #     if ctx.literals():
    #         return self.visit(ctx.literals())
    #     else:
    #         return self.visit(ctx.exp())

    def visitExp5(self,ctx:MPParser.Exp5Context):
        if ctx.exp():
            return ArrayCell(self.visit(ctx.exp6()),self.visit(ctx.exp()))
        else : return self.visit(ctx.getChild(0))
        

    def visitExp6(self,ctx:MPParser.Exp6Context):
        if ctx.literals():
            return self.visit(ctx.literals())
        elif ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.call_exp():
            return self.visit(ctx.call_exp())
        # elif ctx.index_exp():
        #     return self.visit(ctx.index_exp())
        else:
            return self.visit(ctx.exp())

    def visitCall_exp(self,ctx:MPParser.Call_expContext):
        
        param_list = (self.visit(ctx.list_of_exp()) if ctx.list_of_exp() else [])
        #return CallStmt(Id(ctx.ID().getText()),param_list)
        return CallExpr(Id(ctx.ID().getText()),param_list)
    
    def visitLiterals(self,ctx:MPParser.LiteralsContext):
        if ctx.INTLIT():
            #return IntLiteral(ctx.INTLIT().getText())
            return IntLiteral(int(ctx.INTLIT().getText()))
        elif ctx.BOOLLIT():
            if(len(ctx.BOOLLIT().getText())==4 ):
                return BooleanLiteral(True)
            return BooleanLiteral(False)
        elif ctx.REALLIT():
            return FloatLiteral(float(ctx.REALLIT().getText()))
        else:
            return StringLiteral(ctx.STRINGLIT().getText())

    def visitIndex_exp(self,ctx:MPParser.Index_expContext):
        if ctx.ID():
            arr = Id(ctx.ID().getText())
        else:
            arr = self.visit(ctx.call_exp())
        idx = self.visit(ctx.exp())
        return ArrayCell(arr,idx)



