import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    # def test_int_ast(self):
    #     input = Program([ClassDecl(Id("a"),[
    #         MethodDecl(Static(),Id("main"),[],VoidType(),Block([],[
    #             CallStmt(Id("io"),Id("writeInt"),[IntLiteral(5)])]))])])
    #     expect = "5"
    #     self.assertTrue(TestCodeGen.test(input,expect,501))

    # def test_float_ast(self):
    #     input = Program([ClassDecl(Id("a"),[
    #         MethodDecl(Static(),Id("main"),[],VoidType(),Block([],[
    #             CallStmt(Id("io"),Id("writeFloat"),[FloatLiteral(5.0)])]))])])
    #     expect = "5.0"
    #     self.assertTrue(TestCodeGen.test(input,expect,502))

    # def test_string_ast(self):
    #     input = Program([ClassDecl(Id("a"),[
    #         MethodDecl(Static(),Id("main"),[],VoidType(),Block([],[
    #           CallStmt(Id("io"),Id("writeStr"),[StringLiteral("\"acc\"")])]))])])
    #     expect = "acc"
    #     self.assertTrue(TestCodeGen.test(input,expect,503))

    # def test_string2_ast(self):
    #     input = """
    #         class a{
    #             void static main(){
    #                 io.writeStr("cc");
    #             }
    #         }
    #     """
    #     expect = "cc"
    #     self.assertTrue(TestCodeGen.test(input,expect,504))

    # def test_boolean_ast(self):
    #     input = """
    #         class abc extends io{
    #             a, b:int;
    #             final float c = 1;

    #             void shape(a, b:int; e:float){
    #                 t: string;
    #                 f: float;
    #                 final int aa = 1;
    #                 io.writeBool(false);
    #             }
    #         }
    #     """
    #     expect = "false"
    #     self.assertTrue(TestCodeGen.test(input,expect,505))

    # def test_assign1_ast(self):
    #     input = """
    #         class a{
    #             static d: float;
    #             bb: float;
    #             void static main(){
    #                 d: int;
    #                 d := 5;
    #                 io.writeInt(d);
    #             }
    #         }
    #     """
    #     expect = "5"
    #     self.assertTrue(TestCodeGen.test(input,expect,506))

    # def test_assign1_ast(self):
    #     input = """
    #         class a{
    #             static d: float;
    #             bb: float;
    #             void static main(){
    #                 d: float;
    #                 d := 5 + 3.0;
    #                 d := d + 1;
    #                 io.writeFloat(d);
    #             }
    #         }
    #     """
    #     expect = "9.0"
    #     self.assertTrue(TestCodeGen.test(input,expect,506))

    # def test_assign1_ast(self):
    #     input = """
    #         class a{
    #             static d: float;
    #             bb: float;
    #             void static main(){
    #                 d: float;
    #                 d := 6 / 3;
    #                 io.writeFloat(d);
    #             }
    #         }
    #     """
    #     expect = "2.0"
    #     self.assertTrue(TestCodeGen.test(input,expect,506))

    # def test_assign1_ast(self):
    #     input = """
    #         class a{
    #             static d: float;
    #             bb: float;
    #             void static main(){
    #                 d: float;
    #                 e: boolean;
    #                 e := (1 <= 1);
    #                 io.writeBool(e);
    #             }
    #         }
    #     """
    #     expect = "true"
    #     self.assertTrue(TestCodeGen.test(input,expect,506))

    # def test_assign1_ast(self):
    #     input = """
    #         class a{
    #             static d: float;
    #             bb: float;
    #             void static main(){
    #                 d: float;
    #                 e: boolean;
    #                 e := (1 < 1);
    #                 io.writeBool(e);
    #             }
    #         }
    #     """
    #     expect = "false"
    #     self.assertTrue(TestCodeGen.test(input,expect,506))

    # def test_assign1_ast(self):
    #     input = """
    #         class a{
    #             static d: float;
    #             bb: float;
    #             void static main(){
    #                 d: float;
    #                 e: boolean;
    #                 d := 4.5;
    #                 e := (d > 1);
    #                 io.writeBool(e);
    #             }
    #         }
    #     """
    #     expect = "true"
    #     self.assertTrue(TestCodeGen.test(input,expect,506))

    # def test_assign1_ast(self):
    #     input = """
    #         class a{
    #             static d: float;
    #             bb: float;
    #             void static main(){
    #                 d: float;
    #                 e: boolean;
    #                 d := 4.5;
    #                 e := (d == 1) || (d > 3.3);
    #                 io.writeBool(e);
    #             }
    #         }
    #     """
    #     expect = "true"
    #     self.assertTrue(TestCodeGen.test(input,expect,506))

    # def test_assign1_ast(self):
    #     input = """
    #         class a{
    #             static d: float;
    #             bb: float;
    #             void static main(){
    #                 d: float;
    #                 e: boolean;
    #                 d := 4.5;
    #                 e := (d != 1) && (d >= 3.3);
    #                 io.writeBool(e);
    #             }
    #         }
    #     """
    #     expect = "true"
    #     self.assertTrue(TestCodeGen.test(input,expect,506))

    # def test_assign1_ast(self):
    #     input = """
    #         class a{
    #             static d: float;
    #             bb: float;
    #             void static main(){
    #                 d: float;
    #                 e: float;
    #                 d := 4.5;
    #                 e := 9 \\ 10;
    #                 io.writeFloat(e);
    #             }
    #         }
    #     """
    #     expect = "0.0"
    #     self.assertTrue(TestCodeGen.test(input,expect,506))

    # def test_assign1_ast(self):
    #     input = """
    #         class a{
    #             static d: float;
    #             bb: float;
    #             void static main(){
    #                 d: float;
    #                 e: float;
    #                 d := + 4.5;
    #                 io.writeFloat(d);
    #             }
    #         }
    #     """
    #     expect = "4.5"
    #     self.assertTrue(TestCodeGen.test(input,expect,506))

    # def test_assign1_ast(self):
    #     input = """
    #         class a{
    #             static d: float;
    #             bb: float;
    #             void static main(){
    #                 d: float;
    #                 e: float;
    #                 d := - 4.5;
    #                 io.writeFloat(d);
    #             }
    #         }
    #     """
    #     expect = "-4.5"
    #     self.assertTrue(TestCodeGen.test(input,expect,506))

    # def test_assign1_ast(self):
    #     input = """
    #         class a{
    #             static d: float;
    #             bb: float;
    #             void static main(){
    #                 d: float;
    #                 e: float;
    #                 e := -4.1;
    #                 d := -e;
    #                 io.writeFloat(d);
    #             }
    #         }
    #     """
    #     expect = "4.1"
    #     self.assertTrue(TestCodeGen.test(input,expect,506))

    # def test_assign1_ast(self):
    #     input = """
    #         class a{
    #             static d: float;
    #             bb: float;
    #             void static main(){
    #                 d: float;
    #                 e: boolean;
    #                 e := !!!(1 >= 10);
    #                 io.writeBool(e);
    #             }
    #         }
    #     """
    #     expect = "true"
    #     self.assertTrue(TestCodeGen.test(input,expect,506))

    # def test_assign1_ast(self):
    #     input = """
    #         class a{
    #             static d: float;
    #             bb: float;
    #             void static main(){
    #                 d: float;
    #                 e: boolean;
    #                 e := !(1 != 10);
    #                 io.writeBool(e);
    #             }
    #         }
    #     """
    #     expect = "false"
    #     self.assertTrue(TestCodeGen.test(input,expect,506))

    def test_assign1_ast(self):
        input = """
            class a{
                static d: float;
                bb: float;
                void static main(){
                    d, f: int;
                    e: boolean;
                    %%d := 4;
                    if true then 
                        d := 5;

                    f := d;

                    %%io.writeInt(d);
                    
                    
                }
            }
        """
        expect = "5.0"
        self.assertTrue(TestCodeGen.test(input,expect,506))

