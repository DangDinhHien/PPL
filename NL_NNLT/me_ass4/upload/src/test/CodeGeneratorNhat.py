'''
 *   @author Nguyen Hua Phung
 *   @version 1.0
 *   23/10/2015
 *   This file provides a simple version of code generator
 *
'''
from Utils import *
from StaticCheck import *
from StaticError import *
from functools import reduce
from Emitter import Emitter
from Frame import Frame
from abc import ABC, abstractmethod

#note:
# -> mapping to java class
# val : index -> local
# val : cname -> global

class CodeGenerator(Utils):
    def __init__(self):
        self.libName = "io"
        self.curFunc = Symbol("null", MType([],VoidType()), CName("MCClass"))

    def init(self):
        return [    Symbol("getInt", MType(list(), IntType()), CName(self.libName)),
                    Symbol("putInt", MType([IntType()], VoidType()), CName(self.libName)),
                    Symbol("putIntLn", MType([IntType()], VoidType()), CName(self.libName)),
                    Symbol("putFloatLn", MType([FloatType()], VoidType()), CName(self.libName)),
                    Symbol("getFloat", MType([], FloatType()), CName(self.libName)),
                    Symbol("putFloat", MType([FloatType()], VoidType()), CName(self.libName)),
                    Symbol("putFloatLn", MType([FloatType()], VoidType()), CName(self.libName)),
                    Symbol("putBool", MType([BoolType()], VoidType()), CName(self.libName)),
                    Symbol("putBoolLn", MType([BoolType()], VoidType()), CName(self.libName)),
                    Symbol("putString", MType([StringType()], VoidType()), CName(self.libName)),
                    Symbol("putStringLn", MType([StringType()], VoidType()), CName(self.libName)),
                    Symbol("putLn", MType([], VoidType()), CName(self.libName)),
                    ]

    def gen(self, ast, dir_):
        #ast: AST
        #dir_: String
        gl = self.init()
        gc = CodeGenVisitor(ast, gl, dir_)
        gc.visit(ast, None)

# class StringType(Type):
    
#     def __str__(self):
#         return "StringType"

#     def accept(self, v, param):
#         return None

class ArrayPointerType(Type):
    def __init__(self, ctype):
        #cname: String
        self.eleType = ctype

    def __str__(self):
        return "ArrayPointerType({0})".format(str(self.eleType))

    def accept(self, v, param):
        return None

class ClassType(Type):
    def __init__(self,cname):
        self.cname = cname
    def __str__(self):
        return "Class({0})".format(str(self.cname))
    def accept(self, v, param):
        return None

#use for function        
class SubBody():
    def __init__(self, frame, sym):
        #frame: Frame
        #sym: List[Symbol]

        self.frame = frame
        self.sym = sym

#use for expression
class Access():
    def __init__(self, frame, sym, isLeft, isFirst, isDuplicate = False):
        #frame: Frame
        #sym: List[Symbol]
        #isLeft: Boolean
        #isFirst: Boolean

        self.frame = frame
        self.sym = sym
        self.isLeft = isLeft
        self.isFirst = isFirst

class Val(ABC):
    pass

class Index(Val):
    def __init__(self, value):
        #value: Int

        self.value = value

class CName(Val):
    def __init__(self, value):
        #value: String

        self.value = value

class CodeGenVisitor(BaseVisitor, Utils):
    def __init__(self, astTree, env, dir_):
        #astTree: AST
        #env: List[Symbol]
        #dir_: File
        self.astTree = astTree
        self.env = env
        self.className = "MPClass"
        self.path = dir_
        self.emit = Emitter(self.path + "/" + self.className + ".j")
        self.curFunc = None

    #generate the static field for global variable
    def VarGlobal(self, ast, c):
        ctxt = c
        nameAt = ast.variable.name
        typeAt = ast.varType 
        self.emit.printout(self.emit.emitATTRIBUTE(nameAt, typeAt, False, ""))
        symbol = Symbol(ast.variable.name, typeAt, CName(self.className))
        c.append(symbol)
        return c

    def FuncGlobal(self,ast, c):
        ctxt = c
        nameFunc = ast.name.name
        typeFunc = MType([x.varType for x in ast.param], ast.returnType)
        symbol = Symbol(nameFunc, typeFunc, CName(self.className))
        c.append(symbol)
        return c
    
    def printoutstmt(self, ast, env):
        #env : subbody
        frame = env.frame
        newEnv = env.sym
        if type(ast) is Assign:
            self.emit.printout(self.visit(ast, Access(frame, newEnv, True, True))[0])
        elif type(ast) is BinaryOp:
            self.emit.printout(self.visit(ast, Access(frame, newEnv, False, True))[0])
        elif type(ast) is CallExpr:
            self.emit.printout(self.visit(ast, Access(frame, newEnv, False, True, True))[0])
            sym = self.lookup(ast.method.name, newEnv, lambda x:x.name) 
            returnType = sym.mtype.rettype

        elif type(ast) is CallStmt:
            self.emit.printout(self.visit(ast, SubBody(frame, newEnv)))
        elif type(ast) is UnaryOp or type(ast) is Id or type(ast) is IntLiteral or type(ast) is FloatLiteral or type(ast) is StringLiteral or type(ast) is BooleanLiteral:
            self.emit.printout(self.visit(ast, Access(frame, newEnv, False, True))[0])
            self.emit.printout(self.emit.emitPOP(frame))
        else:
            self.visit(ast, env)


    def visitProgram(self, ast, c):
        #ast: Program
        #c: Any
        self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))
        nenv = reduce(lambda x,y: self.VarGlobal(y,x) if type(y) is VarDecl else self.FuncGlobal(y,x), ast.decl, self.env if self.env else [])
        
        lstFunc = list(filter(lambda x:type(x) is FuncDecl, ast.decl))
        reduce(lambda a,b: self.visit(b,a), lstFunc, SubBody(None, nenv))
        #e = SubBody(None, self.env)
        #for x in ast.decl:
        #    e = self.visit(x, e)
        # generate default constructor
        self.genMETHOD(FuncDecl(Id("<init>"), list(), list(), list(),None), c, Frame("<init>", VoidType))
        self.emit.emitEPILOG()
        return c

    def visitVarDecl(self, ast, c):
        env = c.sym if type(c) is SubBody else []
        indx = c.frame.getNewIndex()
        self.emit.printout(self.emit.emitVAR(indx, ast.variable.name, ast.varType, c.frame.getStartLabel(), c.frame.getEndLabel(), c.frame))
        return SubBody(c.frame, [Symbol(ast.variable.name, ast.varType, Index(indx))] + env)

    def genMETHOD(self, consdecl, o, frame):
        #consdecl: FuncDecl
        #o: Any
        #frame: Frame
        isInit = consdecl.returnType is None
        isMain = consdecl.name.name == "main" and len(consdecl.param) == 0 and type(consdecl.returnType) is VoidType
        returnType = VoidType() if isInit else consdecl.returnType
        methodName = "<init>" if isInit else consdecl.name.name
        intype = [ArrayPointerType(StringType())] if isMain else [x.varType for x in consdecl.param]
        mtype = MType(intype, returnType)

        #generate method for a function . use emitMETHOD(methodname, type_descrip, true if static, frame)
        self.emit.printout(self.emit.emitMETHOD(methodName, mtype, not isInit, frame))

        #involked when parsing new scope
        frame.enterScope(True)

        glenv = o

        # Generate code for parameter declarations
        if isInit:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", ClassType(self.className), frame.getStartLabel(), frame.getEndLabel(), frame))
        if isMain:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args", ArrayPointerType(StringType()), frame.getStartLabel(), frame.getEndLabel(), frame))
        
        glSubBody = SubBody(frame, glenv)

        if (isMain is False) and (intype != []):
            glSubBody = reduce(lambda a,b: self.visit(b,a), consdecl.param, SubBody(frame, glenv))

        temp = glSubBody
        glSubBody = reduce(lambda a,b: self.visit(b, a), consdecl.local, temp) 

        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))

        # Generate code for statements
        body = consdecl.body
        if isInit:
            self.emit.printout(self.emit.emitREADVAR("this", ClassType(self.className), 0, frame))
            self.emit.printout(self.emit.emitINVOKESPECIAL(frame))

        #list(map(lambda x: self.visit(x, SubBody(frame, glSubBody.sym)), body))
        list(map(lambda x: self.printoutstmt(x, glSubBody),body))
        
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))

        returnstmt = list(filter(lambda x: type(x)is Return, body))
        if type(returnType) is VoidType or not returnstmt:
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()

    def visitFuncDecl(self, ast, o):
        #ast: FuncDecl
        #o: Any ... subbody
        subctxt = o
        frame = Frame(ast.name, ast.returnType)
        self.curFunc = self.lookup(ast.name.name.lower(), subctxt.sym, lambda x: x.name.lower())
        self.genMETHOD(ast, subctxt.sym, frame)

        return o
        #return SubBody(None, [Symbol(ast.name, MType(list(), ast.returnType), CName(self.className))] + subctxt.sym)

    def visitAssign(self, ast, c):
        ctxt = c
        frame = ctxt.frame
        env = ctxt.sym

        assign_str = ""
        str_I2F = ""

        (resLeft, typeLeft) = self.visit(ast.lhs, Access(frame, env, True, True))
        (resRight, typeRight) = self.visit(ast.exp, Access(frame, env, False, True))

        if type(typeLeft) == FloatType and type(typeRight) == IntType:
            str_I2F = self.emit.emitI2F(frame)

        (resLeft1, typeLeft1) = self.visit(ast.lhs, Access(frame, env, True, False))
        assign_str = resLeft + resRight + str_I2F + resLeft1
        resType = typeLeft1

        return (assign_str, resType)
    
    def visitIf(self, ast, c):
        #c : SubBody
        frame = c.frame
        env = c.sym
        (resExpr, typeExpr) = self.visit(ast.expr, Access(frame, env, False, True))
        if not ast.elseStmt:
            falseLabel = frame.getNewLabel()
            self.emit.printout(resExpr + self.emit.emitIFFALSE(falseLabel, frame))
            list(map(lambda x: self.printoutstmt(x, c),ast.thenStmt))
            self.emit.printout(self.emit.emitLABEL(falseLabel, frame))
        else:
            falseLabel = frame.getNewLabel()
            trueLabel = frame.getNewLabel()
            self.emit.printout(resExpr + self.emit.emitIFFALSE(falseLabel, frame))
            list(map(lambda x: self.printoutstmt(x, c),ast.thenStmt))
            self.emit.printout(self.emit.emitGOTO(str(trueLabel), frame) + self.emit.emitLABEL(str(falseLabel), frame))
            list(map(lambda x: self.printoutstmt(x, c),ast.elseStmt))
            self.emit.printout(self.emit.emitLABEL(str(trueLabel), frame))


    def visitWhile(self, ast, c):
        frame = c.frame
        env = c.sym

        frame.enterLoop()
        self.emit.printout(self.emit.emitLABEL(frame.getContinueLabel(), frame))
        resExpr, typeExpr = self.visit(ast.exp,Access(frame, env,False,False))
        self.emit.printout(resExpr)
        self.emit.printout(self.emit.emitIFFALSE(frame.getBreakLabel(), frame))
        list(map(lambda x:self.printoutstmt(x,c) ,ast.sl))
        self.emit.printout(self.emit.emitGOTO(frame.getContinueLabel(), frame))
        self.emit.printout(self.emit.emitLABEL(frame.getBreakLabel(), frame))
        frame.exitLoop()

    def visitFor(self, ast, c):
        frame = c.frame
        env = c.sym
        beginLabel = frame.getNewLabel()
        frame.enterLoop()
        #sinh ma cho expr1
        self.emit.printout(self.visit(Assign(ast.id,ast.expr1),SubBody(frame, env))[0])
        self.emit.printout(self.emit.emitLABEL(beginLabel, frame))
        
        #sinh ma cho expr2
        op_ = ('<=','+') if ast.up == "True" else ('>=','-')
        self.emit.printout(self.visit(BinaryOp(op_[0],ast.id,ast.expr2),SubBody(frame, env))[0])
        self.emit.printout(self.emit.emitIFFALSE(frame.getBreakLabel(), frame))

        #sinh stmt
        list(map(lambda x:self.printoutstmt(x,c) ,ast.loop))

        #sinh ma continue
        self.emit.printout(self.emit.emitLABEL(frame.getContinueLabel(), frame))
        
        #sinh ma expr3
        self.emit.printout(self.visit(Assign(ast.id,BinaryOp(op_[1],ast.id,IntLiteral(1))),SubBody(frame, env))[0])
        
        #back
        self.emit.printout(self.emit.emitGOTO(beginLabel, frame))

        #sinh ma break
        self.emit.printout(self.emit.emitLABEL(frame.getBreakLabel(), frame))
        frame.exitLoop()

    def visitBreak(self,ast,c):
        self.emit.printout(self.emit.emitGOTO(c.frame.getBreakLabel(), c.frame))
    
    def visitContinue(self,ast,c):
        self.emit.printout(self.emit.emitGOTO(c.frame.getContinueLabel(), c.frame))

    def visitWith(self, ast, c):
        #decl:list(VarDecl)
        #stmt:list(Stmt)
        frame = c.frame
        env = c.sym
            
        frame.enterScope(False)
        withSubBody = reduce(lambda a,b: self.visit(b, a), ast.decl, c)
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        list(map(lambda x: self.printoutstmt(x, withSubBody),ast.stmt))  
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame)) 
        frame.exitScope()
        
        return c

    def visitReturn(self, ast, c):
        #expr:Expr
        if ast.expr:
            (resExpr, resType) = self.visit(ast.expr, Access(c.frame, c.sym, False, True))
            typeFunc = self.curFunc.mtype.rettype
            if type(typeFunc) == FloatType and type(resType) == IntType:
                self.emit.printout(resExpr + self.emit.emitI2F(c.frame) + self.emit.emitRETURN(FloatType(), c.frame))
            else:
                self.emit.printout(resExpr + self.emit.emitRETURN(resType, c.frame))
        else:
            self.emit.printout(self.emit.emitRETURN(VoidType(), c.frame))

    def visitCallStmt(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        sym = self.lookup(ast.method.name.lower(), nenv, lambda x: x.name.lower())

        method_name = sym.name
        cname = sym.value.value
        ctype = sym.mtype
        returnType = ctype.rettype

        listparamType = ctype.partype
        
        checkList = []
        for item in range(len(listparamType)):
            checkList.append((ast.param[item], listparamType[item]))
        
        in_ = ("", [])
        for x in checkList:
            #gan param
            (code, ty) = self.visit(x[0], Access(frame, nenv, False, True))
            if type(ty) is IntType and type(x[1]) is FloatType:
                in_ = (in_[0] + code + self.emit.emitI2F(frame), in_[1] + [ty])
            else:
                in_ = (in_[0] + code, in_[1] + [ty])
        
        return in_[0] + self.emit.emitINVOKESTATIC(cname + "/" + method_name, ctype, frame)

    def visitCallExpr(self, ast, o):
        #ast: CallStmt
        #o: Any
        #method:Id
        #param:list(Expr)
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        sym = self.lookup(ast.method.name.lower(), nenv, lambda x: x.name.lower())

        method_name = sym.name
        cname = sym.value.value
        ctype = sym.mtype
        returnType = ctype.rettype 
        
        if ctxt.isLeft is True and ctxt.isFirst is False:
            return (self.emit.emitWRITEVAR2(ast.method.name, returnType, frame), returnType)
        else:
            listParamType = ctype.partype
            # zip
            checkList=[]
            for item in range(len(listParamType)):
                checkList.append((ast.param[item],listParamType[item]))
            
            in_ = ("",[])
            for x in checkList:
                #str1 : param
                #typ1 : type param
                (str1,typ1) = self.visit(x[0],Access(frame,nenv,False,True))
                if type(typ1) is IntType and type(x[1]) is FloatType:
                    in_ = (in_[0] + str1 + self.emit.emitI2F(frame), in_[1] + [typ1])
                else:
                    in_ = (in_[0] + str1, in_[1] + [typ1])
        
        return (in_[0] + self.emit.emitINVOKESTATIC(cname + "/" + method_name, ctype, frame), returnType)
        #return (in_[0], returnType)
          

    def visitBinaryOp(self, ast, c):
        #op:string
        #left:Expr
        #right:Expr
        ctxt = c
        frame = c.frame
        env = ctxt.sym
        op = ast.op
        resType = IntType()
        code = ""
        opstr = ""
        stri2f = ""

        (resLeft, typeLeft) = self.visit(ast.left, Access(frame, env, False, True))
        (resRight, typeRight) = self.visit(ast.right, Access(frame, env, False, True))

        if op == "+" or op == "-":
            if type(typeLeft) is FloatType and type(typeRight) is IntType:
                opstr = resLeft + resRight + self.emit.emitI2F(frame) + self.emit.emitADDOP(op, FloatType(), frame) 
                resType = FloatType()   
            elif type(typeLeft) is IntType and type(typeRight) is FloatType:
                opstr = resLeft + self.emit.emitI2F(frame) + resRight + self.emit.emitADDOP(op, FloatType(), frame)             
                resType = FloatType()
            else:
                opstr = resLeft + resRight + self.emit.emitADDOP(op, typeLeft, frame)
                resType = typeLeft
        elif op == "*" :
            if type(typeLeft) is FloatType and type(typeRight) is IntType:
                opstr = resLeft + resRight + self.emit.emitI2F(frame) + self.emit.emitMULOP(op, FloatType(), frame)
                resType = FloatType()
            elif type(typeLeft) is IntType and type(typeRight) is FloatType:
                opstr = resLeft + self.emit.emitI2F(frame) + resRight + self.emit.emitMULOP(op, FloatType(), frame)
                resType = FloatType()
            else:
                opstr = resLeft + resRight + self.emit.emitMULOP(op, typeLeft, frame)
                resType = typeLeft
        elif op == "/" :
            if type(typeLeft) is IntType and type(typeRight) is IntType:
                opstr = resLeft + self.emit.emitI2F(frame) + resRight + self.emit.emitI2F(frame) + self.emit.emitMULOP(op, FloatType(), frame)
                resType = FloatType()
            if type(typeLeft) is FloatType and type(typeRight) is IntType:
                opstr = resLeft + resRight + self.emit.emitI2F(frame) + self.emit.emitMULOP(op, FloatType(), frame)
                resType = FloatType()
            elif type(typeLeft) is IntType and type(typeRight) is FloatType:
                opstr = resLeft + self.emit.emitI2F(frame) + resRight + self.emit.emitMULOP(op, FloatType(), frame)
                resType = FloatType()
            elif type(typeLeft) is FloatType and type(typeRight) is FloatType:
                opstr = resLeft + resRight + self.emit.emitMULOP(op, FloatType(), frame)
                resType = FloatType()
             


        elif op.lower() == "div":
            opstr = resLeft + resRight + self.emit.emitDIV(frame)
            resType = IntType()
        elif op.lower() == "mod":
            opstr = resLeft + resRight + self.emit.emitMOD(frame)
            resType = IntType()

        elif (op == ">") or (op == "<") or (op == ">=") or (op == "<="):
            if type(typeLeft) is FloatType and type(typeRight) is IntType:
                opstr = resLeft + resRight + self.emit.emitI2F(frame) + self.emit.emitREOP(op, FloatType(), frame)
            elif type(typeLeft) is IntType and type(typeRight) is FloatType:
                opstr = resLeft + self.emit.emitI2F(frame) + resRight + self.emit.emitREOP(op, FloatType(), frame)
            else:
                opstr = resLeft + resRight + self.emit.emitREOP(op, typeLeft, frame)
            resType = BoolType()
        
        elif (op == "<>" or op == "="):
            if type(typeLeft) is FloatType and type(typeRight) is IntType:
                opstr = resLeft + resRight + self.emit.emitI2F(frame) + self.emit.emitREOP(op, FloatType(), frame)
            elif type(typeLeft) is IntType and type(typeRight) is FloatType:
                opstr = resLeft + self.emit.emitI2F(frame) + resRight + self.emit.emitREOP(op, FloatType(), frame)
            else:
                opstr = resLeft + resRight + self.emit.emitREOP(op, typeLeft, frame)
            
            resType = BoolType()
            
        elif (op.lower() == "and" or op.lower() == "or"):
            #opstr = resLeft + resRight + self.emit.emitANDOP(frame) if ast.op.lower() == "and" else self.emit.emitOROP(frame)
            if ast.op.lower() == "and":
                opstr = resLeft + resRight + self.emit.emitANDOP(frame)
            elif ast.op.lower() == "or":
                opstr = resLeft + resRight + self.emit.emitOROP(frame)
            resType = BoolType()
        elif ast.op.lower() == "andthen" or ast.op.lower() == "orelse":
            opstr = self.emit.emitAndThen_OrElse(ast.op.lower(), resLeft, resRight, frame)
            resType = BoolType()
        
        return(opstr, resType)        

    def visitUnaryOp(self,ast,c):
        ctxt = c
        frame = ctxt.frame
        env = ctxt.sym
        (resExpr, typeExpr) = self.visit(ast.body, Access(frame, env, False, True))
        if ast.op.lower() == "not":
            return (resExpr + self.emit.emitNOT(typeExpr, frame), typeExpr)

        elif ast.op == "-": 
            return (resExpr + self.emit.emitNEGOP(typeExpr, frame), typeExpr)
    

    
    def visitId(self, ast, o):
        #o : Access or SubBody
        
        if type(o) is not SubBody: 
            sym = self.lookup(ast.name.lower(), o.sym, lambda x: x.name.lower())

            name_id = sym.name
            code = ""
            if o.isLeft is True and o.isFirst is True:
                pass
            #putStatic or store var
            elif o.isLeft is True:
                if type(sym.value) is CName:
                    code = self.emit.emitPUTSTATIC(sym.value.value + "." + name_id, sym.mtype, o.frame)
                elif type(sym.value) is Index:
                    code = self.emit.emitWRITEVAR(name_id, sym.mtype, sym.value.value, o.frame)
            #if lhs -> getstatic or load var
            elif o.isLeft is False:
                if type(sym.value) is CName:
                    code = self.emit.emitGETSTATIC(sym.value.value + "." + name_id, sym.mtype, o.frame)
                elif type(sym.value) is Index:
                    code = self.emit.emitREADVAR(name_id, sym.mtype, sym.value.value, o.frame)
            return (code, sym.mtype)    
        else:
            sym = self.lookup(ast.name, o.sym, lambda x: x.name)
            return ("", sym.mtype)

    def visitIntLiteral(self, ast, o):
        #ast: IntLiteral
        #o: Any

        ctxt = o
        frame = ctxt.frame
        return self.emit.emitPUSHICONST(int(ast.value), frame), IntType()

    def visitFloatLiteral(self, ast, o):
        #ast : FloatLiteral
        #o : any

        ctxt = o
        frame = ctxt.frame
        return self.emit.emitPUSHFCONST(str(ast.value), frame), FloatType()
    
    def visitBooleanLiteral(self,ast,o):
        ctxt = o
        frame = ctxt.frame
        return (self.emit.emitPUSHICONST(str(ast.value).lower(), frame), BoolType())

    def visitStringLiteral(self, ast, o):
        #ast: StringLiteral
        #o: Any
        ctxt = o
        frame = ctxt.frame
        return self.emit.emitPUSHCONST(str(ast.value), StringType(), frame), StringType()
