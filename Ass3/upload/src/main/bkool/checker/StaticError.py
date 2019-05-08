#update: 6/04/2019
from abc import ABC

class Kind(ABC):
    pass

class Class(Kind):
    def __str__(self):
        return "Class"

class Method(Kind):
    def __str__(self):
        return "Method"

class SpecialMethod(Kind):
    def __str__(self):
        return "Special Method"

class Attribute(Kind):
    def __str__(self):
        return "Attribute"

class Parameter(Kind):
    def __str__(self):
        return "Parameter"

class Constant(Kind):
    def __str__(self):
        return "Constant"

class Variable(Kind):
    def __str__(self):
        return "Variable"

class Identifier(Kind):
    def __str__(self):
        return "Identifier"

class StaticError(Exception):
    pass
class Undeclared(StaticError):
    """k: Kind
       n: string: name of identifier """
    def __init__(self,k,n):
        self.k = k
        self.n = n
    def __str__(self):
        return  "Undeclared "+ str(self.k) + ": " + self.n

class Redeclared(StaticError):
    """k: Kind
       n: string: name of identifier """
    def __init__(self,k,n):
        self.k = k
        self.n = n
    def __str__(self):
        return  "Redeclared "+ str(self.k) + ": " + self.n

class TypeMismatchInExpression(StaticError):
    """exp: AST.Expr"""
    def __init__(self,exp):
        self.exp = exp

    def __str__(self):
        return  "Type Mismatch In Expression: "+ str(self.exp)

class TypeMismatchInStatement(StaticError):
    """stmt:AST.Stmt"""
    def __init__(self,stmt):
        self.stmt = stmt

    def __str__(self):
        return "Type Mismatch In Statement: "+ str(self.stmt)

class CannotAssignToConstant(StaticError):
    """stmt:AST.Stmt"""
    def __init__(self,stmt):
        self.stmt = stmt

    def __str__(self):
        return "Cannot Assign To Constant: "+ str(self.stmt)

class TypeMismatchInConstant(StaticError):
    """constdecl:AST.ConstDecl"""
    def __init__(self,constdecl):
        self.constdecl = constdecl

    def __str__(self):
        return "Type Mismatch In Constant Declaration: "+ str(self.constdecl)

class NotConstantExpression(StaticError):
    """expr: AST.Expr"""
    def __init__(self,expr):
        self.expr = expr

    def __str__(self):
        return "Not Constant Expression: " + str(self.expr)

class BreakNotInLoop(StaticError):
    def __str__(self):
        return "Break Not In Loop"

class ContinueNotInLoop(StaticError):
    def __str__(self):
        return "Continue Not In Loop"


