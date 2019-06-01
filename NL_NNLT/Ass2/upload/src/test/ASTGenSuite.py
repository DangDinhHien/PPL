import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_funccall(self):
        """More complex program"""
        input = """
        function foo (c,d : integer):INTEGER;
        var d : real;
        begin
        end"""
        #expect param : name, param, local, body, returnType
        expect = str(Program([
            FuncDecl(Id("foo"),
            [VarDecl(Id("c"),IntType()),VarDecl(Id("d"),IntType())],
            [VarDecl(Id("d"),FloatType())],
            [],
            IntType())]))
        self.assertTrue(TestAST.test(input,expect,304))

    def test_arrayvar(self):
        input = """
        var a : array [1 .. 4] of integer;
        """
        expect = str(Program([VarDecl(Id("a"),ArrayType("1","4",IntType()))]))
        self.assertTrue(TestAST.test(input,expect,305))

    # def test_simple_assign(self):
    #     input = """
    #     function main ():real;
    #     begin
    #         a:=c;
    #     end"""
    #     expect = str(Program([
    #         FuncDecl(Id("main"),
    #         [],
    #         [],
    #         [Assign(Id("a"),Id("c"))],
    #         FloatType())]))
    #     self.assertTrue(TestAST.test(input,expect,306))

    def test_simple_procedure(self):
        input = """
        procedure main();
        var x : string;
        begin 
        end
        """
        expect = str(Program([
            FuncDecl(Id("main"),
            [],
            [VarDecl(Id("x"),StringType())],
            [],
            VoidType())]))
        self.assertTrue(TestAST.test(input,expect,307))

    def test_simple_assign_with_idexp(self):
        input = """
        procedure main();
        begin
            a[3] := 1;
        end 
        """
        expect = ""#str(Program([FuncDecl(Id("main"),[],[],[Assign(ArrayCell(Id("a"),IntLiteral(2)),Id("k"))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,308))
