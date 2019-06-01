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
from Emitter import Emitter
from Frame import Frame
from abc import ABC, abstractmethod
import functools

class CodeGenerator(Utils):
    def __init__(self):
        self.libName = "io"

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
        
class SubBody():
    def __init__(self, frame, sym):
        #frame: Frame
        #sym: List[Symbol]

        self.frame = frame
        self.sym = sym

class Access():
    def __init__(self, frame, sym, isLeft, isFirst):
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
        self.current_function = None #Symbol("",MType([],VoidType()),CName(self.className))

    def VarGlobal(self, ast, c):
        ctxt = c
        nameAtt = ast.variable.name
        typeAtt = ast.varType
        self.emit.printout(self.emit.emitATTRIBUTE(nameAtt, typeAtt, False, ""))
        symbol = Symbol(nameAtt, typeAtt, CName(self.className))
        c.append(symbol)
        return c

    def FuncGlobal(self,ast, c):
        ctxt = c
        nameFunc = ast.name.name
        typeFunc = MType([x.varType for x in ast.param], ast.returnType)
        symbol = Symbol(nameFunc, typeFunc, CName(self.className))
        c.append(symbol)
        return c

    def visitProgram(self, ast, c):
        #ast: Program
        #c: Any
        self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))
        #get global env
        nenv = functools.reduce(lambda x,y: self.VarGlobal(y,x) if type(y) is VarDecl else self.FuncGlobal(y,x), ast.decl, self.env if self.env else []) 

        e = SubBody(None, nenv)
        # visit all funtion in program
        lsFun = list(filter(lambda x:type(x) is FuncDecl, ast.decl))
        for x in lsFun:
            e = self.visit(x, e)
        # generate default constructor for MPClass
        self.genMETHOD(FuncDecl(Id("<init>"), list(), list(), list(),None), c, Frame("<init>", VoidType))
        self.emit.emitEPILOG()
        return c

    def genMETHOD(self, consdecl, c, frame):
        #consdecl: FuncDecl
        #c: Any
        #frame: Frame
        isInit = consdecl.returnType is None
        isMain = consdecl.name.name == "main" and len(consdecl.param) == 0 and type(consdecl.returnType) is VoidType
        returnType = VoidType() if isInit else consdecl.returnType
        methodName = "<init>" if isInit else consdecl.name.name
        intype = [ArrayPointerType(StringType())] if isMain else [x.varType for x in consdecl.param]
        mtype = MType(intype, returnType)


        self.emit.printout(self.emit.emitMETHOD(methodName, mtype, not isInit, frame))


        frame.enterScope(True)

        glenv = c

        # Generate code for parameter declarations
        if isInit:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", ClassType(self.className), frame.getStartLabel(), frame.getEndLabel(), frame)) 
        if isMain:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args", ArrayPointerType(StringType()), frame.getStartLabel(), frame.getEndLabel(), frame))
        
        glSubBody = SubBody(frame,glenv)
        if (isMain is False) and (intype != []):
            glSubBody = functools.reduce(lambda a,b: self.visit(b,a), consdecl.param, glSubBody) 

        body = consdecl.body

        current_env = functools.reduce(lambda a,b: self.visit(b,a), consdecl.local, glSubBody)

        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))

        # Generate code for statements
        if isInit:
            self.emit.printout(self.emit.emitREADVAR("this", ClassType(self.className), 0, frame))
            self.emit.printout(self.emit.emitINVOKESPECIAL(frame))

        #visit body of function
        list(map(lambda x: self.visit(x, current_env), body))

        # get and print Endlabel
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        
        returnstmt = list(filter(lambda x: type(x)is Return, body))
        if type(returnType) is VoidType or not returnstmt:
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope();

    def visitVarDecl(self,ast,c):
        # this function visit local variable(not global)
        #ast: VarDecl
        #c  : SubBody
        env  = c.sym if type(c) is SubBody else []
        indx = c.frame.getNewIndex()
        self.emit.printout(self.emit.emitVAR(indx, ast.variable.name, ast.varType, c.frame.getStartLabel(), c.frame.getEndLabel(), c.frame))
        return SubBody(c.frame, [Symbol(ast.variable.name, ast.varType, Index(indx))] + env)

    def visitFuncDecl(self, ast, o):
        #ast: FuncDecl
        #o: Any
        subctxt = o
        frame = Frame(ast.name, ast.returnType)
        self.current_function = self.lookup(ast.name.name.lower(), subctxt.sym, lambda x: x.name.lower())
        self.genMETHOD(ast, subctxt.sym, frame)
        return o

    def Call(self,ast,c):
        ctxt = c
        frame = ctxt.frame
        nenv = ctxt.sym

        sym = self.lookup(ast.method.name.lower(), nenv, lambda x: x.name.lower())

        cname = sym.value.value
        ctype = sym.mtype
        method_name = sym.name

        param_type = list(zip(ast.param,ctype.partype))
        ret = ""
        for x in param_type:
            str1, typ1 = self.visit(x[0], Access(frame, nenv, False, True))
            ret += str1+self.emit.emitI2F(frame) if (type(typ1),type(x[1]))==(IntType,FloatType) else str1
        return (ret + self.emit.emitINVOKESTATIC(cname + "/" + method_name, ctype, frame), ctype.rettype)

    def visitCallStmt(self, ast, c):
        self.emit.printout(self.Call(ast,c)[0])

    def visitCallExpr(self,ast,c):
        return self.Call(ast,c)

    def visitAssign(self,ast,o):
        ctxt = o
        frame = ctxt.frame
        env = ctxt.sym

        resRight, typeRight = self.visit(ast.exp,Access(frame, env, False, False))
        resLeft, typeLeft = self.visit(ast.lhs, Access(frame, env, True, False))
        str_I2f = self.emit.emitI2F(frame) if (type(typeLeft),type(typeRight)) == (FloatType,IntType) else ""

        self.emit.printout(resRight+ str_I2f  + resLeft)
    
    def visitIf(self,ast,c):
        frame = c.frame
        env = c.sym

        resExpr, typeExpr = self.visit(ast.expr,Access(frame, env, False, True))
        
        if len(ast.elseStmt)==0:
            falseLabel = frame.getNewLabel()
            self.emit.printout(resExpr + self.emit.emitIFFALSE(falseLabel, frame))
            list(map(lambda x: self.visit(x, c), ast.thenStmt))
            self.emit.printout(self.emit.emitLABEL(falseLabel, frame))
        else:
            falseLabel = frame.getNewLabel()
            trueLabel = frame.getNewLabel()
            # if false go to falselabel
            self.emit.printout(resExpr + self.emit.emitIFFALSE(falseLabel, frame))
            # if true then do stmt
            list(map(lambda x: self.visit(x, c), ast.thenStmt))
            # then go to Truelable
            self.emit.printout(self.emit.emitGOTO(trueLabel, frame))
            
            self.emit.printout(self.emit.emitLABEL(falseLabel, frame))
            list(map(lambda x: self.visit(x, c), ast.elseStmt))
            self.emit.printout(self.emit.emitLABEL(trueLabel, frame))

    def visitWhile(self,ast,c):
        frame = c.frame
        env = c.sym

        frame.enterLoop()
        
        self.emit.printout(self.emit.emitLABEL(frame.getContinueLabel(), frame))

        resExpr, typeExpr = self.visit(ast.exp,Access(frame, env,False,False))

        self.emit.printout(resExpr)
        
        self.emit.printout(self.emit.emitIFFALSE(frame.getBreakLabel(), frame))

        list(map(lambda x:self.visit(x,c) ,ast.sl))

        self.emit.printout(self.emit.emitGOTO(frame.getContinueLabel(), frame))

        self.emit.printout(self.emit.emitLABEL(frame.getBreakLabel(), frame))

        frame.exitLoop()

    def visitFor(self,ast,c):

        frame = c.frame
        env = c.sym
        beginLabel = frame.getNewLabel()
        frame.enterLoop()
        
        self.visit(Assign(ast.id,ast.expr1),SubBody(frame, env))

        self.emit.printout(self.emit.emitLABEL(beginLabel, frame))
        
        op_ = ('<=','+') if ast.up is True else ('>=','-')

        self.emit.printout(self.visit(BinaryOp(op_[0],ast.id,ast.expr2),SubBody(frame, env))[0])

        self.emit.printout(self.emit.emitIFFALSE(frame.getBreakLabel(), frame))

        list(map(lambda x:self.visit(x,SubBody(frame, env)) ,ast.loop))

        self.emit.printout(self.emit.emitLABEL(frame.getContinueLabel(), frame))
        
        self.visit(Assign(ast.id,BinaryOp(op_[1],ast.id,IntLiteral(1))),SubBody(frame, env))
        
        self.emit.printout(self.emit.emitGOTO(beginLabel, frame))

        self.emit.printout(self.emit.emitLABEL(frame.getBreakLabel(), frame))

        frame.exitLoop()

    def visitReturn(self,ast,c):
        if ast.expr:
            resExpr, resType = self.visit(ast.expr, Access(c.frame, c.sym, False, True))
            typeFunc = self.current_function.mtype.rettype
            if (type(typeFunc),type(resType)) == (FloatType,IntType):
                self.emit.printout(resExpr + self.emit.emitI2F(c.frame) + self.emit.emitRETURN(FloatType(), c.frame))
            else:
                self.emit.printout(resExpr + self.emit.emitRETURN(resType, c.frame))
                
            # try:
            #     lable = c.frame.getBreakLabel()
            # except:
            #     lable = -1
            # if lable !=-1 :self.emit.printout(self.emit.emitGOTO(c.frame.getBreakLabel(), c.frame))
            


        else:
            self.emit.printout(self.emit.emitRETURN(VoidType(), c.frame))

    def visitBreak(self,ast,c):
        self.emit.printout(self.emit.emitGOTO(c.frame.getBreakLabel(), c.frame))
    
    def visitContinue(self,ast,c):
        self.emit.printout(self.emit.emitGOTO(c.frame.getContinueLabel(), c.frame))
    
    def visitWith(self,ast,c):

        ctxt = c
        frame = ctxt.frame
        newEnv = ctxt.sym

        frame.enterScope(False)

        varEnv = functools.reduce(lambda a,b: self.visit(b,a), ast.decl,SubBody(frame, newEnv))

        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))

        list(map(lambda x:self.visit(x,varEnv),ast.stmt))

        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))

        frame.exitScope()
        
        return c
        
    def visitIntLiteral(self, ast, o):
        #ast: IntLiteral
        #o: Any
        ctxt = o
        frame = ctxt.frame
        return self.emit.emitPUSHICONST(ast.value, frame), IntType()

    def visitFloatLiteral(self, ast, o):
        #ast: FloatLiteral
        #o: Any
        ctxt = o
        frame = ctxt.frame
        return self.emit.emitPUSHFCONST(str(ast.value), frame), FloatType()

    def visitBinaryOp(self,ast,o):
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        op = ast.op.lower()

        # str1, type1 = self.visit(ast.left,o)
        
        # str2, type2 = self.visit(ast.right,o)
        str1, type1 = self.visit(ast.left,Access(frame, nenv, False, False))
        
        str2, type2 = self.visit(ast.right,Access(frame, nenv, False, False))
        
        retType = type1
        # convert type of factor and return type of expression
        if (type(type1) ,type(type2)) == (FloatType,IntType):
            str2+=self.emit.emitI2F(frame)
            retType = FloatType()
        elif (type(type1) ,type(type2)) == (IntType,FloatType):
            str1+=self.emit.emitI2F(frame)
            retType = FloatType()
        elif (type(type1) ,type(type2)) == (IntType,IntType):
            if ast.op is '/':
                str2+=self.emit.emitI2F(frame)
                str1+=self.emit.emitI2F(frame)
                retType = FloatType()
            else:
                retType = IntType()

        if op in ['+','-']:
            return str1+str2+self.emit.emitADDOP(op,retType,frame),retType
        elif op in ['*','/']:
            return str1+str2+self.emit.emitMULOP(op,retType,frame),retType
        elif op == 'mod': # error ,let fix as soon as posible
            return str1+str2+self.emit.emitMOD(frame),IntType()
        elif op == 'div':
            return str1+str2+self.emit.emitDIV(frame),IntType()
        elif op in ['<','>','<=','>=','=','<>']:
            return str1+str2+self.emit.emitREOP(op, retType, frame),BoolType()

        elif op in ['and','or']:
            str_op = self.emit.emitANDOP(frame) if op == 'and' else self.emit.emitOROP(frame)
            return str1+str2+str_op,BoolType()
        elif op in ['andthen','orelse']:
            return self.emit.emit_ANDTHEN_ORELSE(op,str1,str2,frame),BoolType()

    def visitUnaryOp(self,ast,o):
        ctxt = o
        frame = ctxt.frame
        env = ctxt.sym
        resExpr, typeExpr = self.visit(ast.body, Access(frame, env, False, True))
        if ast.op.lower() == "not":
            return resExpr + self.emit.emitNOT(typeExpr, frame), typeExpr
        elif ast.op.lower() == "-": 
            return resExpr + self.emit.emitNEGOP(typeExpr, frame), typeExpr

    def visitId(self,ast,o):
        
        if type(o) is Access:      
            sym  = self.lookup(ast.name.lower(), o.sym, lambda x: x.name.lower())
            code = ""
            nameId = sym.name
            if o.isLeft:
                if type(sym.value) is CName:
                    code = self.emit.emitPUTSTATIC(sym.value.value + "." + nameId, sym.mtype, o.frame)
                elif type(sym.value) is Index:
                    code = self.emit.emitWRITEVAR(nameId, sym.mtype, sym.value.value, o.frame)
            else:
                if type(sym.value) is CName:
                    code = self.emit.emitGETSTATIC(sym.value.value + "." + nameId, sym.mtype, o.frame)
                elif type(sym.value) is Index:
                    code = self.emit.emitREADVAR(nameId.lower(), sym.mtype, sym.value.value, o.frame)

            return code,sym.mtype
        # else:
        #     sym  = self.lookup(ast.name.lower(), o.sym, lambda x: x.name.lower())
        #     return "",sym.mtype

    def visitStringLiteral(self, ast, o):
        #ast: StringLiteral
        #o: Any
        ctxt = o
        frame = ctxt.frame
        return self.emit.emitPUSHCONST(str(ast.value), StringType(), frame), StringType()

    def visitBooleanLiteral(self,ast,o):
        ctxt = o
        frame = ctxt.frame
        return self.emit.emitPUSHICONST(str(ast.value).lower(), frame), BoolType()
    
