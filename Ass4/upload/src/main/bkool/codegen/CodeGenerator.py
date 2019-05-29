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
from functools import reduce

class MType(Type):
    
    def __init__(self,intype,outtype):
        #intype:list(Type)
        #outtype:Type
        self.partype = intype
        self.rettype = outtype

    def __str__(self):
        return "MType(["+",".join([str(x) for x in self.partype])+"],"+str(self.rettype)

    def accept(self, v, param):
        return None

class ArrayPointerType(Type):
    def __init__(self, ctype):
        #cname: String
        self.eleType = ctype

    def __str__(self):
        return "ArrayPointerType({0})".format(str(self.eleType))

    def accept(self, v, param):
        return None


        
class MethodEnv():
    def __init__(self, emit, classname, parentname, declist):
        #emit:Emitter
        #classname:String
        #parentname:String
        #declist:list(Decl)
        self.emit = emit
        self.classname = classname
        self.parentname = parentname
        self.declist = declist

class StmtEnv():
    def __init__(self, frame, sym, methodenv):
        #frame: Frame
        #sym: List[Member]
        #method: MethodEnv

        self.frame = frame
        self.sym = sym
        self.method = methodenv

class ExprEnv():
    def __init__(self, isLeft, isFirst, stmt):
        #stmt: StmtEnv
        #isLeft: Boolean
        #isFirst: Boolean
        self.stmt = stmt
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

class Member:
    def __init__(self,name,skind,mtype,value = None,value2 = None):
        #name:String
        #sikind:SIKind
        #mtype:Type
        #value:Expr
        self.name = name
        self.sikind = skind
        self.mtype = mtype
        self.value = value
        self.value2 = value2
class ClassData:
    def __init__(self,cname,pname,mem):
        #cname:String -- class name
        #pname:String -- parent name
        #mem:list(Member)
        self.cname = cname
        self.pname = pname
        self.mem = mem

class GlobalEnvironment(BaseVisitor):
    def __init__(self,env):
        #env:list(ClassData)
        self.env = env

    def visitProgram(self,ast:Program,o):
        return list(reduce(lambda x,y: self.visit(y,x),ast.decl,self.env))
    
    def visitClassDecl(self,ast:ClassDecl,o):
        return [ClassData(ast.classname.name,
                        ast.parentname.name if ast.parentname else "",
                        list(reduce(lambda x,y: self.visit(y,x),ast.memlist,[])))] + o
      
    def visitAttributeDecl(self,ast,o):
        name,mtype,e = self.visit(ast.decl,o)
        return [Member(name,ast.sikind,mtype,e)] + o

    def visitVarDecl(self,ast,o):
        return ast.variable.name,ast.varType,None

    def visitConstDecl(self,ast,o):
        return ast.constant.name,ast.constType,ast.value

    def visitMethodDecl(self,ast:MethodDecl,o):
        return [Member(ast.name.name,
                        ast.sikind,
                        MType([x.varType for x in ast.param],ast.returnType))] + o
    




## --------------------------------------------------------------------- ##    
class CodeGenerator(Utils):
    def __init__(self):
        self.libName = "io"

    def init(self):
        mem = [Member("readInt",Static(),MType(list(),IntType()),None),
                Member("writeInt",Static(),MType([IntType()],VoidType()),None),
                Member("writeIntLn",Static(),MType([IntType()],VoidType()),None),
                Member("readFloat",Static(),MType(list(),FloatType()),None),
                Member("writeFloat",Static(),MType([FloatType()],VoidType()),None),
                Member("writeFloatLn",Static(),MType([FloatType()],VoidType()),None),
                Member("readBool",Static(),MType(list(),BoolType()),None),
                Member("writeBool",Static(),MType([BoolType()],VoidType()),None),
                Member("writeBoolLn",Static(),MType([BoolType()],VoidType()),None),
                Member("readStr",Static(),MType(list(),StringType()),None),
                Member("writeStr",Static(),MType([StringType()],VoidType()),None),
                Member("writeStrLn",Static(),MType([StringType()],VoidType()),None)]
        return [ClassData("io","",mem)]

    def gen(self, ast, dir_):
        #ast: AST
        #dir_: String

        gl = self.init()
        ge = GlobalEnvironment(gl)
        glenv = ge.visit(ast,None)
        gc = CodeGenVisitor(ast, glenv, dir_)
        gc.visit(ast, None)


class CodeGenVisitor(BaseVisitor, Utils):
    def __init__(self, astTree, env, dir_):
        #astTree: AST
        #env: List[ClassData]
        #dir_: File

        self.astTree = astTree
        self.env = env
        self.path = dir_
        

    def visitProgram(self, ast, c):
        #ast: Program
        #c: Any
        for x in ast.decl:
            self.visit(x,c)
        return c

    def visitClassDecl(self, ast, c):
        #ast:ClassDecl
        #c:Any
        print(ast)
        emit = Emitter(self.path + "/" + ast.classname.name + ".j")
        parentname = ast.parentname.name if ast.parentname else "java.lang.Object"
        emit.printout(emit.emitPROLOG(ast.classname.name, parentname))
        e = MethodEnv(emit, ast.classname.name,parentname,[])

        #genAttribute
        for x in self.env:
            if ast.classname.name == x.cname:
                for y in reversed(x.mem):
                    if type(y.mtype) is not MType:
                        isFinal = False if y.value is None else True
                        if type(y.sikind) is Static:
                            emit.printout(emit.emitATTRIBUTE(y.name, y.mtype, isFinal, ""))
                        else:
                            emit.printout(emit.emitATTRIBUTE(y.name, y.mtype, isFinal, ""))

                break
                ### ------------

        lstMethod = list(filter(lambda x: type(x) is MethodDecl, ast.memlist))
        list(map(lambda x: self.visit(x, e), lstMethod))
        # generate default constructor
        self.genMETHOD(MethodDecl(Instance(),Id("<init>"), list(), None, Block(list(), list())), 
            e, 
            Frame("<init>", VoidType()))
        emit.emitEPILOG()
        return c

    def visitVarDecl(self, ast, o):
        #o: MethodEnv, frame
        idx = o[1].getNewIndex()
        emit = o[0].emit
        emit.printout(emit.emitVAR(idx, ast.variable.name, ast.varType, o[1].getStartLabel(), o[1].getEndLabel(), o[1]))
        o[0].declist = [Member(ast.variable.name, Instance(), ast.varType, Index(idx))] + o[0].declist

    def visitConstDecl(self, ast, o):
        #o: MethodEnv, frame
        idx = o[1].getNewIndex()
        emit = o[0].emit
        emit.printout(emit.emitVAR(idx, ast.constant.name, ast.constType, o[1].getStartLabel(), o[1].getEndLabel(), o[1]))
        o[0].declist = [Member(ast.constant.name, Instance(), ast.constType, Index(idx), ast.value)] + o[0].declist


    def genMETHOD(self, consdecl, o, frame):
        #consdecl: MethodDecl
        #o: MethodEnv
        #frame: Frame

        isInit = consdecl.returnType is None
        isMain = consdecl.name.name == "main" and len(consdecl.param) == 0 and type(consdecl.returnType) is VoidType
        returnType = VoidType() if isInit else consdecl.returnType
        methodName = "<init>" if isInit else consdecl.name.name
        intype = [ArrayPointerType(StringType())] if isMain else list()
        mtype = MType(intype, returnType)
        emit = o.emit
        emit.printout(emit.emitMETHOD(methodName, mtype,type(consdecl.sikind) is Static, frame))

        frame.enterScope(True)
        
        # Generate code for parameter declarations
        if (type(consdecl.sikind) is Instance):
            emit.printout(emit.emitVAR(frame.getNewIndex(),"this",ClassType(Id(o.classname)),frame.getStartLabel(),frame.getEndLabel(),frame))
        elif isMain:
            emit.printout(emit.emitVAR(frame.getNewIndex(), "args", ArrayPointerType(StringType()), frame.getStartLabel(), frame.getEndLabel(), frame))
        #TODO generate code for parameter
        if isMain is False:
            for x in consdecl.param:
                self.visit(x, (o, frame))

        #TODO generate code for local declarations
        body = consdecl.body
        for x in body.decl:
            self.visit(x.decl, (o, frame))

        emit.printout(emit.emitLABEL(frame.getStartLabel(), frame))

        # Generate code for statements
        if isInit:
            emit.printout(emit.emitREADVAR("this", ClassType(Id(o.classname)), 0, frame))
            emit.printout(emit.emitINVOKESPECIAL(frame))
        list(map(lambda x: self.visit(x, StmtEnv(frame, [], o)), body.stmt))

        emit.printout(emit.emitLABEL(frame.getEndLabel(), frame))
        if type(returnType) is VoidType:
            emit.printout(emit.emitRETURN(VoidType(), frame))
        emit.printout(emit.emitENDMETHOD(frame))
        frame.exitScope();

    def visitMethodDecl(self, ast, o):
        #ast: MethodDecl
        #o: MethodEnv
        frame = Frame(ast.name, ast.returnType)
        self.genMETHOD(ast, o, frame)
        return o

    def visitCallStmt(self, ast, o):
        #ast: CallStmt
        #o: StmtEnv
        emit = o.method.emit
        frame = o.frame

        sym = self.lookup(ast.obj.name,self.env,lambda x: x.cname)
        if sym:
            cname = sym.cname
            ctype = ClassType(Id(sym.cname))
        else:
            raise Undeclared(Identifier(),ast.name)
        #cname,ctype = self.visit(ast.obj, ExprEnv(False,True,o))
        symclass = self.lookup(ctype.classname.name,self.env,lambda x:x.cname)
        methodsym = self.lookup(ast.method.name,symclass.mem,lambda x:x.name)
        mtype = methodsym.mtype

        in_ = ("", list())
        for x in ast.param:
            str1, typ1 = self.visit(x, ExprEnv(False, True,o))
            if type(typ1) is IntType and type(x) is FloatType:
                in_ = (in_[0] + str1 + emit.emitI2F(frame), in_[1].append(typ1))    
            else:
                in_ = (in_[0] + str1, in_[1].append(typ1))
        emit.printout(in_[0])
        emit.printout(emit.emitINVOKESTATIC(cname + "/" + ast.method.name, mtype, frame))

    def visitFor(self, ast, o):
        #o: stmt
        frame = o.frame
        emit = o.method.emit
        beginLabel = frame.getNewLabel()
        frame.enterLoop()
        ### expr1
        self.visit(Assign(ast.id, ast.expr1), o)
        emit.printout(emit.emitLABEL(beginLabel, frame))

        frame.exitLoop()

    def visitIf(self, ast, o):
        #o: stmt
        frame = o.frame
        emit = o.method.emit
        res1, type1 = self.visit(ast.expr, ExprEnv(False, False, o))

        if len(ast.elseStmt) == 0:
            falseLabel = frame.getNewLabel()
            emit.printout(res1 + emit.emitIFFALSE(falseLabel, frame))
            self.visit(ast.thenStmt, o)
            emit.printout(emit.emitLABEL(falseLabel, frame))
        else:
            elseLabel = frame.getNewLabel()
            exitLabel = frame.getNewLabel()
            emit.printout(res1 + emit.emitIFFALSE(elseLabel, frame))            
            self.visit(ast.thenStmt, o)
            emit.printout(emit.emitGOTO(exitLabel, frame))

            emit.printout(emit.emitLABEL(elseLabel, frame))
            self.visit(ast.elseStmt, o)
            emit.printout(emit.emitLABEL(exitLabel, frame))

    def visitAssign(self, ast, o):
        frame = o.frame
        emit = o.method.emit
        
        resR, typeR = self.visit(ast.exp, ExprEnv(False, False, o))
        resL, typeL = self.visit(ast.lhs, ExprEnv(True, False, o))

        str_I2f = emit.emitI2F(frame) if (type(typeL),type(typeR)) == (FloatType,IntType) else ""

        emit.printout(resR + str_I2f  + resL)
    
    def visitBinaryOp(self, ast, o):
        #o: ExprEnv
        frame = o.stmt.frame
        emit = o.stmt.method.emit
        op = ast.op.lower()

        str1, type1 = self.visit(ast.left, ExprEnv(False, False, o.stmt))
        str2, type2 = self.visit(ast.right, ExprEnv(False, False, o.stmt))

        retType = type1
        if (type(type1) ,type(type2)) == (FloatType,IntType):
            str2 += emit.emitI2F(frame)
            retType = FloatType()
        elif (type(type1) ,type(type2)) == (IntType,FloatType):
            str1 += emit.emitI2F(frame)
            retType = FloatType()
        elif (type(type1) ,type(type2)) == (IntType,IntType):
            if ast.op is '/':
                str2 += emit.emitI2F(frame)
                str1 += emit.emitI2F(frame)
                retType = FloatType()
            else:
                retType = IntType()

        if op in ['+','-']:
            return str1 + str2 + emit.emitADDOP(op,retType,frame),retType
        elif op in ['*','/']:
            return str1 + str2 + emit.emitMULOP(op,retType,frame),retType
        elif op == '%':
            return str1 + str2 + emit.emitMOD(frame),IntType()
        elif op == '\\':
            return str1 + str2 + emit.emitDIV(frame),IntType()
        elif op in ['<','>','<=','>=','==','!=']:
            return str1 + str2 + emit.emitREOP(op, retType, frame),BoolType()
        elif op in ['&&','||']:
            str_op = emit.emitANDOP(frame) if op == '&&' else emit.emitOROP(frame)
            return str1 + str2 + str_op,BoolType()

    def visitUnaryOp(self, ast, o):
        #o: ExprEnv
        frame = o.stmt.frame
        emit = o.stmt.method.emit
        res1, type1 = self.visit(ast.body, ExprEnv(False, False, o.stmt))
        op = ast.op.lower()
        if op == "-":
            return res1 + emit.emitNEGOP(type1, frame), type1
        elif op == "!":
            return res1 + emit.emitNOT(type1, frame), type1
        else: ### +
            return res1, type1

    def visitReturn(self, ast, o):
        #o: stmt
        emit = o.method.emit
        frame = o.frame
        print(o.frame.returnType)

        res1, type1 = self.visit(ast.expr, ExprEnv(False, False, o))
        returnType = frame.returnType
        if (type(returnType),type(type1)) == (FloatType, IntType):
            emit.printout(res1 + emit.emitI2F(frame) + emit.emitRETURN(FloatType(), frame))
        else:
            emit.printout(res1 + emit.emitRETURN(returnType, frame))        


    def visitBreak(self, ast, o):
        #o: stmt
        emit = o.method.emit
        frame = o.frame
        emit.printout(emit.emitGOTO(frame.getBreakLabel(), frame))

    def visitContinue(self, ast, o):
        # o: stmt
        emit = o.method.emit
        frame = o.frame
        emit.printout(emit.emitGOTO(frame.getContinueLabel(), frame))


    def visitId(self,ast,o):
        #ast:Id
        #o:ExprEnv
        emit = o.stmt.method.emit
        if type(o) is ExprEnv:
            #print(o.stmt.method.declist[0].name)
            mem = self.lookup(ast.name, o.stmt.method.declist, lambda x: x.name)
            code = ""
            if not mem:
                raise Undeclared(Identifier(), ast.name)
            if o.isLeft is True:
                ## check fun or var
                if type(mem.mtype) is MType:
                    pass
                elif type(mem.value) is Index:
                    code = emit.emitWRITEVAR(mem.name, mem.mtype, mem.value.value, o.stmt.frame)
            else:
                if type(mem.mtype) is MType:
                    pass
                elif type(mem.value) is Index:
                    code = emit.emitREADVAR(mem.name, mem.mtype, mem.value.value, o.stmt.frame)

            return code, mem.mtype

        # sym = self.lookup(ast.name,self.env,lambda x: x.cname)
        # if sym:
        #     return (sym.cname,ClassType(Id(sym.cname)))
        # else:
        #     raise Undeclared(Identifier(),ast.name)

    def visitIntLiteral(self, ast, o):
        #ast: IntLiteral
        #o: ExprEnv
        emit = o.stmt.method.emit
        frame = o.stmt.frame
        return emit.emitPUSHICONST(ast.value, frame), IntType()

    def visitFloatLiteral(self, ast, o):
        #ast: FLoatLiteral
        #o: ExprEnv
        emit = o.stmt.method.emit
        frame = o.stmt.frame
        return emit.emitPUSHFCONST(str(ast.value), frame), FloatType()

    def visitStringLiteral(self, ast, o):
        #ast: StringLiteral
        #o: ExprEnv
        emit = o.stmt.method.emit
        frame = o.stmt.frame
        return emit.emitPUSHCONST(str(ast.value), StringType(), frame), StringType()

    def visitBooleanLiteral(self, ast, o):
        #ast: BoaleanLiteral
        #o: ExprEnv
        emit = o.stmt.method.emit
        frame = o.stmt.frame
        return emit.emitPUSHICONST(str(ast.value), frame), BoolType()

