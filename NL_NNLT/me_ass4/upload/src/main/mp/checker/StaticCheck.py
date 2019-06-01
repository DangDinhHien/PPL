
"""
 * @author nhphung
 *student : Tran Hoai Nam --- 1612131
"""
from AST import * 
from Visitor import *
from Utils import Utils
from StaticError import *

class MType:
    def __init__(self,partype,rettype):
        self.partype = partype
        self.rettype = rettype

class Symbol:
    def __init__(self,name,mtype,value = None):
        self.name = name
        self.mtype = mtype
        self.value = value

def IsEqualType(l,r,isParam = False):
    if (type(l) == ArrayType):
        if type(r) == ArrayType:
            return str(l)==str(r)
        else:
            return False
    if isParam == False:
        if type(l) == VoidType or type(l)==StringType:
            return False
    else:
        if (type(l), type(r)) == (StringType,StringType):
            return True

    if (type(l), type(r)) == (FloatType,IntType):
        return True 
    #print(type(l),type(r))
    return type(l)==type(r)

def deleteRedeclareVariable(env,name_):
    [env.remove(it) for it in env if it.name == name_]

class StaticChecker(BaseVisitor,Utils):

    global_envi = [Symbol("getInt",MType([],IntType())),
                    Symbol("putInt",MType([IntType()],VoidType())),
                    Symbol("putIntLn",MType([IntType()],VoidType())),
                    Symbol("getFloat",MType([],FloatType())),
                    Symbol("putFloat",MType([FloatType()],VoidType())),
                    Symbol("putFloatLn",MType([FloatType()],VoidType())),
                    Symbol("putBool",MType([BoolType()],VoidType())),
                    Symbol("putBoolLn",MType([BoolType()],VoidType())),
                    Symbol("putString",MType([StringType()],VoidType())),
                    Symbol("putStringLn",MType([StringType()],VoidType())),
                    Symbol("putLn",MType([],VoidType()))
                   ]
            
    def __init__(self,ast):
        self.ast = ast
   
    def check(self):
        return self.visit(self.ast,StaticChecker.global_envi)

    def visitProgram(self,ast, c):

        env=c.copy()

        mainfunc = None
        
        list_reachfunc   = {}

        for decl in ast.decl:
            if type(decl) is VarDecl:

                check = self.lookup(decl.variable.name.lower(),env,lambda x: x.name.lower())
                if not(check is None):
                    raise Redeclared(Variable(),decl.variable.name)
                env.append(Symbol(decl.variable.name, decl.varType))
            elif type(decl) is FuncDecl:
                
                check = self.lookup(decl.name.name.lower(),env,lambda x: x.name.lower())
                if  not (check is None): # neu trung
                    if type(decl.returnType) is VoidType: # dua tren cai khai bao lan sau
                        raise Redeclared(Procedure(),decl.name.name)
                    raise Redeclared(Function(),decl.name.name)
                # neu khong trung
                rtype_ = decl.returnType
                # if type(rtype_) is ArrayType:
                #     rtype_ = self.visit(decl.returnType,env)
                env.append(Symbol(decl.name.name, MType([x.varType for x in decl.param],rtype_)))
                
                if type(rtype_) is VoidType and decl.name.name.lower() == "main" :
                    #print(decl.param)
                    if len(decl.param) == 0:
                        mainfunc = decl
                    # check if parameter of main procedure is exsting
                    

                list_reachfunc[decl.name.name] = 0 if decl.name.name.lower() != "main" else 1

        if mainfunc is None:
            raise NoEntryPoint()

        list(map(lambda x: self.visit(x,(env,None,None,False,list_reachfunc)),ast.decl))

        for x in list_reachfunc:
            if list_reachfunc[x]==0:
                check = self.lookup(x.lower(),env,lambda x:x.name.lower())
                if type(check.mtype.rettype) is VoidType:
                    raise Unreachable(Procedure(),x)
                raise Unreachable(Function(),x)
        return []

    def visitFuncDecl(self,ast, c):
        #name: Id
        #param: list(VarDecl)
        #returnType: Type => VoidType for Procedure
        #local:list(VarDecl)
        #body: list(Stmt)

        evn = c[0].copy()
        local_evn = []
        
        for p in ast.param:

            check = self.lookup(p.variable.name.lower(),local_evn,lambda x: x.name.lower())

            if not (check is None):
                raise Redeclared(Parameter(),p.variable.name)

            local_evn.append(Symbol(p.variable.name, p.varType))
            deleteRedeclareVariable(evn,p.variable.name)

        for p in ast.local:
            check = self.lookup(p.variable.name.lower(),local_evn,lambda x: x.name.lower())

            if not ( check is None):
                raise Redeclared(Variable(),p.variable.name)

            local_evn.append(Symbol(p.variable.name, p.varType))

            deleteRedeclareVariable(evn,p.variable.name)

        evn+=local_evn

        check_Return = None
        check_all_flow_isReturn = "NotReturn";

        for stmt in ast.body:
            
            if check_Return is "IgnoreDown" or check_Return is "Return" : #or check_Return is "BC":
                raise UnreachableStatement(stmt)
            check_Return = self.visit(stmt,(evn,ast.name.name,ast.returnType,False,c[4]))  
            if check_Return is "Return": check_all_flow_isReturn = "Return"

        if check_all_flow_isReturn is "NotReturn" and type(ast.returnType) is not VoidType:
            raise FunctionNotReturn(ast.name.name)


    def visitReturn(self,ast,c):
        env   = c[0].copy()
        rtype = c[2]
        if type(rtype) is VoidType: # procedure
            if ast.expr is None:
                return "Return" 
            else: 
                raise TypeMismatchInStatement(ast)
        else:# function
            #print(rtype,self.visit(ast.expr,(env,None, False,c[3],c[4])))
            if ast.expr is None or IsEqualType(rtype,self.visit(ast.expr,(env,None, False,c[3],c[4]))) is False:
                raise TypeMismatchInStatement(ast)
            else: return "Return"  

    def visitIf(self,ast,c):
        #expr:Expr
        #thenStmt:list(Stmt)
        #elseStmt:list(Stmt)
        env = c[0].copy()

        if type(self.visit(ast.expr,(env,c[1],c[2],c[3],c[4]))) != BoolType:
            raise TypeMismatchInStatement(ast)


        check_thenStmt = "NotReturn"
        check = None
        for stmt in ast.thenStmt:
            if check is "IgnoreDown" or check is "Return":
                raise UnreachableStatement(stmt)
            check = self.visit(stmt,(env,c[1],c[2],c[3],c[4]))
            if check is "Return": check_thenStmt = "Return"
            # only one stmt has returned then => "Return"


        check_elseStmt = "NotReturn" 
        check = None
        for stmt in ast.elseStmt:
            if check is "IgnoreDown" or check is "Return":
                raise UnreachableStatement(stmt)
            check = self.visit(stmt,(env,c[1],c[2],c[3],c[4]))
            if check is "Return":check_elseStmt = "Return"

        if check_thenStmt is "Return" and check_elseStmt is "Return":
            return "Return"
        else :return "NotReturn"
        
        #return None
    def visitWith(self,ast,c):
        #decl:list(VarDecl)
        #stmt:list(Stmt)
        env = c[0].copy()
        local_env = []
        for vardecl in ast.decl:
            check = self.lookup(vardecl.variable.name.lower(),local_env,lambda x: x.name.lower())
            if not check is None:
                raise Redeclared(Variable(),vardecl.variable.name)
            local_env.append(Symbol(vardecl.variable.name,vardecl.varType))
            deleteRedeclareVariable(env,vardecl.variable.name)

        env += local_env

        check_all_flow_inWITH_isReturn = "NotReturn"

        check = None
        for stat in ast.stmt:
            if check is "IgnoreDown" or check is "Return" :
                raise UnreachableStatement(stat)
            check = self.visit(stat,(env,c[1],c[2],c[3],c[4]))
            if check is "Return" : check_all_flow_inWITH_isReturn = "Return"
        
        if check_all_flow_inWITH_isReturn is "Return":
            return "Return"
        else: return "NotReturn"



    def visitFor(self,ast,c):
        #id:Id
        #expr1,expr2:Expr
        #loop:list(Stmt)
        #up:Boolean #True => increase; False => decrease
        env = c[0].copy()

        Id_ = self.visit(ast.id,(env,c[1],c[2],False,c[4]))
        ex1 = self.visit(ast.expr1,(env,c[1],c[2],False,c[4]))
        ex2 = self.visit(ast.expr2,(env,c[1],c[2],False,c[4]))


        if not (type(Id_) is IntType and type(ex1) is IntType and type(ex2) is IntType):
            raise TypeMismatchInStatement(ast)
        # visit all block

        check = None

        for stmt in ast.loop: 
            if check is "IgnoreDown" or check is "Return":
                raise UnreachableStatement(stmt)
            check = self.visit(stmt,(env,c[1],c[2],True,c[4]))



    def visitWhile(self,ast,c):
        #sl:list(Stmt)
        #exp: Expr
        env = c[0].copy()

        checktype = self.visit(ast.exp,(env,c[1],c[2],True,c[4]))
        if not type(checktype) is BoolType:
            raise TypeMismatchInStatement(ast)

        check = None
        for stmt in ast.sl:
            if check is "IgnoreDown" or check is "Return":
                raise UnreachableStatement(stmt)
            check = self.visit(stmt,(env,c[1],c[2],True,c[4]))



    def visitAssign(self,ast,c):
        #lhs:Expr
        #exp:Expr
        env = c[0].copy() if c[0] is not None else []

        le  = self.visit(ast.lhs,(env,c[1],c[2],c[3],c[4]))
        ri  = self.visit(ast.exp,(env,c[1],c[2],c[3],c[4]))

        if type(le) == ArrayType or type(le) == StringType:
            raise TypeMismatchInStatement(ast)

        if (type(le),type(ri)) == (IntType,IntType)or\
        (type(le),type(ri)) == (FloatType,IntType) or\
        (type(le),type(ri)) == (FloatType,FloatType) or\
        (type(le),type(ri)) == (BoolType,BoolType):
            return le 
        else: raise TypeMismatchInStatement(ast)

    

    def visitCallStmt(self, ast, c): 
        #TODO
        evn = c[0].copy()

        res = self.lookup(ast.method.name.lower(),evn,lambda x: x.name.lower())

        list_param = [self.visit(x,(evn,c[1],c[2],c[3],c[4])) for x in ast.param]

        

        if res is None or not type(res.mtype) is MType or not type(res.mtype.rettype) is VoidType:
            raise Undeclared(Procedure(),ast.method.name)
        elif len(res.mtype.partype) != len(list_param):

            raise TypeMismatchInStatement(ast)            
        else:
            for i,param in enumerate(list_param):
                
                if IsEqualType(res.mtype.partype[i],param,isParam=True) is False:
                    raise TypeMismatchInExpression(ast)

            if ast.method.name in c[4] and ast.method.name != c[1]:
                c[4][ast.method.name] += 1

    def visitCallExpr(self, ast, c): 
        #TODO
        evn = c[0].copy()

        res = self.lookup(ast.method.name.lower(),evn,lambda x: x.name.lower())

        list_param = [self.visit(x,(evn,c[1],c[2],c[3],c[4])) for x in ast.param]


        if res is None or not type(res.mtype) is MType or type(res.mtype.rettype) is VoidType:
            raise Undeclared(Function(),ast.method.name)
        elif len(res.mtype.partype) != len(list_param) or type(res.mtype.rettype) is VoidType:
            raise TypeMismatchInExpression(ast)            
        else:
            for i,param in enumerate(list_param):
                if IsEqualType(res.mtype.partype[i],param,isParam=True) is False:

                    raise TypeMismatchInExpression(ast)

            if ast.method.name in c[4] and ast.method.name != c[1]:
                c[4][ast.method.name] += 1
        return res.mtype.rettype

    def visitArrayCell(self,ast,c):
        """
        arr: Expr is arraytpye
        idx: Expr is integer
        """
        env = c[0].copy()
        if type(self.visit(ast.idx,(env,c[1],c[2],c[3],c[4]))) is not IntType:
            raise TypeMismatchInExpression(ast)
        else:
            arr = self.visit(ast.arr,(env,c[1],c[2],c[3],c[4]))
            if type(arr) is ArrayType:
                return arr.eleType
            else:
                raise TypeMismatchInExpression(ast)

    def visitUnaryOp(self,ast,c):
        """
        op: String
        body: Expr
        """
        env = c[0].copy()
        rtype  = self.visit(ast.body,(env,c[1],c[2],c[3],c[4]))
        if ast.op is "!":
            if type(rtype) is not BoolType:
                raise TypeMismatchInExpression(ast) 
            return BoolType()
        elif ast.op is "-":
            if (type(rtype) is not IntType) and (type(rtype) is not FloatType):
                raise TypeMismatchInExpression(ast)
        return rtype

    def visitBinaryOp(self,ast,c):
        #op:string: AND THEN => andthen; OR ELSE => orelse; other => keep it
        #left:Expr
        #right:Expr
        env = c[0].copy() if c[0] is not None else []
        le  = self.visit(ast.left,(env,c[1],c[2],c[3],c[4]))
        ri  = self.visit(ast.right,(env,c[1],c[2],c[3],c[4]))
        op  = ast.op

        if op == "+" or op == "-" or op == "*" or op == "/":
            if (type(le),type(ri)) == (IntType,IntType):
                return FloatType() if op == "/" else IntType()

            elif (type(le),type(ri)) == (FloatType,IntType) or\
            (type(le),type(ri)) == (IntType,FloatType) or\
            (type(le),type(ri)) == (FloatType,FloatType):
                return FloatType()

            else: raise TypeMismatchInExpression(ast)

        elif op == "div" or op == "mod":
            if (type(le),type(ri)) == (IntType,IntType):
                return IntType()
            raise TypeMismatchInExpression(ast)

        elif op == "<" or op == "<=" or op == ">" or op ==">=" or op == "=" or op == "<>":
            if (type(le),type(ri)) == (IntType,IntType)or\
            (type(le),type(ri)) == (FloatType,IntType) or\
            (type(le),type(ri)) == (IntType,FloatType) or\
            (type(le),type(ri)) == (FloatType,FloatType) or\
            ((type(le),type(ri)) == (BoolType,BoolType) and\
            (op == "=" or op == "<>")) :
                return BoolType()
            else: raise TypeMismatchInExpression(ast)

        elif op == "and" or op == "or" or op == "andthen" or op == "orelse":
            if (type(le),type(ri)) == (BoolType,BoolType):
                return BoolType()
            raise TypeMismatchInExpression(ast)

        else: raise TypeMismatchInExpression(ast)

    def visitId(self,ast,c):
        """ 
        name:string 
        """
        env = c[0].copy() if c[0] is not None else []
        
        res = self.lookup(ast.name.lower(), env, lambda x:x.name.lower())

        if res is None or type(res.mtype) is MType :
            raise Undeclared(Identifier(),ast.name) 
        elif type(res) is Symbol: # id
            return res.mtype #Mtype or Int or float ...
        else:
            raise Undeclared(Identifier(),ast.name)

    def visitBreak(self,ast,c):
        if c[3] == False:
            raise BreakNotInLoop()
        else: return "IgnoreDown"

    def visitContinue(self,ast,c):
        if c[3] == False:
            raise ContinueNotInLoop()
        else: return "IgnoreDown"

    def visitIntLiteral(self,ast, c): 
        return IntType()

    def visitFloatLiteral(self,ast, c): 
        return FloatType()

    def visitStringLiteral(self,ast, c): 
        return StringType()

    def visitBooleanLiteral(self,ast, c): 
        return BoolType()

    def visitIntType(self,ast,c):
        return IntType()

    def visitFloatType(self,ast,c):
        return FloatType()

    def visitBoolType(self,ast,c):
        return BoolType()

    def visitStringType(self,ast,c):
        return StringType()

    def visitVoidType(self,ast,c):
        return VoidType()

    def visitArrayType(self,ast,c):
        return ast
   