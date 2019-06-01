import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test_0(self):
        input = Program([ClassDecl(Id("a"),[
            MethodDecl(Static(),Id("main"),[],VoidType(),Block([],[
                CallStmt(Id("io"),Id("writeInt"),[IntLiteral(5)])]))])])
        expect = "5"
        self.assertTrue(TestCodeGen.test(input,expect,500))

    def test_1(self):
        input = Program([ClassDecl(Id("a"),[
            MethodDecl(Static(),Id("main"),[],VoidType(),Block([],[
                CallStmt(Id("io"),Id("writeFloat"),[FloatLiteral(5.0)])]))])])
        expect = "5.0"
        self.assertTrue(TestCodeGen.test(input,expect,501))

    def test_2(self):
        input = Program([ClassDecl(Id("a"),[
            MethodDecl(Static(),Id("main"),[],VoidType(),Block([],[
              CallStmt(Id("io"),Id("writeStr"),[StringLiteral("\"acc\"")])]))])])
        expect = "acc"
        self.assertTrue(TestCodeGen.test(input,expect,502))

    def test_3(self):
        input = """
            class a{
                void static main(){
                    io.writeStr("cc");
                }
            }
        """
        expect = "cc"
        self.assertTrue(TestCodeGen.test(input,expect,503))

    def test_4(self):
        input = """
            class a {
                a, b:int;

                void static main(){
                    io.writeBool(false);
                }
            }
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input,expect,504))

    def test_5(self):
        input = """
            class a{
                static d: float;
                bb: float;
                void static main(){
                    d: int;
                    d := 5;
                    io.writeInt(d);
                }
            }
        """
        expect = "5"
        self.assertTrue(TestCodeGen.test(input,expect,505))

    def test_6(self):
        input = """
            class a{
                static d: float;
                bb: float;
                void static main(){
                    d: float;
                    d := 5 + 3.0;
                    d := d + 1;
                    io.writeFloat(d);
                }
            }
        """
        expect = "9.0"
        self.assertTrue(TestCodeGen.test(input,expect,506))

    def test_7(self):
        input = """
            class a{
                static d: float;
                bb: float;
                void static main(){
                    d: float;
                    d := 6 / 3;
                    io.writeFloat(d);
                }
            }
        """
        expect = "2.0"
        self.assertTrue(TestCodeGen.test(input,expect,507))

    def test_8(self):
        input = """
            class a{
                static d: float;
                bb: float;
                void static main(){
                    d: float;
                    e: boolean;
                    e := (1 <= 1);
                    io.writeBool(e);
                }
            }
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,508))

    def test_9(self):
        input = """
            class a{
                static d: float;
                bb: float;
                void static main(){
                    d: float;
                    e: boolean;
                    e := (1 < 1);
                    io.writeBool(e);
                }
            }
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input,expect,509))

    def test_10(self):
        input = """
            class a{
                static d: float;
                bb: float;
                void static main(){
                    d: float;
                    e: boolean;
                    d := 4.5;
                    e := (d > 1);
                    io.writeBool(e);
                }
            }
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,510))

    def test_11(self):
        input = """
            class a{
                static d: float;
                bb: float;
                void static main(){
                    d: float;
                    e: boolean;
                    d := 4.5;
                    e := (d == 1) || (d > 3.3);
                    io.writeBool(e);
                }
            }
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,511))

    def test_12(self):
        input = """
            class a{
                static d: float;
                bb: float;
                void static main(){
                    d: float;
                    e: boolean;
                    d := 4.5;
                    e := (d != 1) && (d >= 3.3);
                    io.writeBool(e);
                }
            }
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,512))

    def test_13(self):
        input = """
            class a{
                static d: float;
                bb: float;
                void static main(){
                    d: float;
                    e: float;
                    d := 4.5;
                    e := 9 \\ 10;
                    io.writeFloat(e);
                }
            }
        """
        expect = "0.0"
        self.assertTrue(TestCodeGen.test(input,expect,513))

    def test_14(self):
        input = """
            class a{
                static d: float;
                bb: float;
                void static main(){
                    d: float;
                    e: float;
                    d := + 4.5;
                    io.writeFloat(d);
                }
            }
        """
        expect = "4.5"
        self.assertTrue(TestCodeGen.test(input,expect,514))

    def test_15(self):
        input = """
            class a{
                static d: float;
                bb: float;
                void static main(){
                    d: float;
                    e: float;
                    d := - 4.5;
                    io.writeFloat(d);
                }
            }
        """
        expect = "-4.5"
        self.assertTrue(TestCodeGen.test(input,expect,515))

    def test_16(self):
        input = """
            class a{
                static d: float;
                bb: float;
                void static main(){
                    d: float;
                    e: float;
                    e := -4.1;
                    d := -e;
                    io.writeFloat(d);
                }
            }
        """
        expect = "4.1"
        self.assertTrue(TestCodeGen.test(input,expect,516))

    def test_17(self):
        input = """
            class a{
                static d: float;
                bb: float;
                void static main(){
                    d: float;
                    e: boolean;
                    e := !!!(1 >= 10);
                    io.writeBool(e);
                }
            }
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,517))

    def test_18(self):
        input = """
            class a{
                static d: float;
                bb: float;
                void static main(){
                    d: float;
                    e: boolean;
                    e := !(1 != 10);
                    io.writeBool(e);
                }
            }
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input,expect,518))

    def test_19(self):
        input = """
            class a{
                static d: float;
                bb: float;
                void static main(){
                    d, f: int;
                    e: boolean;
                    %%d := 0;
                    e := false;
                    for d := 1 to 3 do
                        e := true;
                 
                    io.writeBool(e);
                }
            }
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,519))

    def test_20(self):
        input = """
            class a{
                static d: float;
                bb: float;
                void static main(){
                    d, f: int;
                    e: boolean;
                    %%d := 0;
                    e := false;
                    for d := 1 to 3 do
                        io.writeBool(e);
                 
                    
                }
            }
        """
        expect = "falsefalsefalse"
        self.assertTrue(TestCodeGen.test(input,expect,520))

    def test_21(self):
        input = """
            class a{
                static d: float;
                bb: float;
                void static main(){
                    d, f: int;
                    e: boolean;
                    %%d := 0;
                    e := false;
                    for d := 1 to 3 do
                        io.writeBoolLn(e);
                }
            }
        """
        expect = "false\nfalse\nfalse\n"
        self.assertTrue(TestCodeGen.test(input,expect,521))

    def test_22(self):
        input = """
            class a{
                static d: float;
                bb: float;
                void static main(){
                    d, f: int;
                    e: boolean;
                    %%d := 0;
                    e := false;
                    for d := 3 downto 1 do
                        io.writeBoolLn(true);
                }
            }
        """
        expect = "true\ntrue\ntrue\n"
        self.assertTrue(TestCodeGen.test(input,expect,522))

    def test_23(self):
        input = """
            class a{
                static d: float;
                bb: float;
                void static main(){
                    d, f: int;
                    e: boolean;
                    %%d := 0;
                    e := false;
                    for d := 3 downto 1 do
                        io.writeIntLn(d);
                }
            }
        """
        expect = "3\n2\n1\n"
        self.assertTrue(TestCodeGen.test(input,expect,523))

    def test_24(self):
        input = """
            class a{
                static d: float;
                bb: float;
                void static main(){
                    d, f: int;
                    e: boolean;
                    e := false;
                    for d := 2 + 2 downto 1 do
                        io.writeIntLn(d);
                }
            }
        """
        expect = "4\n3\n2\n1\n"
        self.assertTrue(TestCodeGen.test(input,expect,524))

    def test_25(self):
        input = """
            class a{
                static d: float;
                bb: float;
                void static main(){
                    d, f: int;
                    e: boolean;
                    e := false;
                    for d := 2 + 2 downto 1 do
                        break;
                    io.writeIntLn(d);
                }
            }
        """
        expect = "4\n"
        self.assertTrue(TestCodeGen.test(input,expect,525))

    def test_26(self):
        input = """
            class a{
                static d: float;
                bb: float;
                void static main(){
                    d, f: int;
                    e: boolean;
                    e := false;
                    for d := 2 + 2 downto 1 do
                        continue;
                    io.writeIntLn(d);
                }
            }
        """
        expect = "0\n"
        self.assertTrue(TestCodeGen.test(input,expect,526))

    def test_27(self):
        input = """
            class a{
                static d: float;
                bb: float;
                void static main(){
                    a: float;
                    e: boolean;
                    e := false;
                    {
                        a, b: int;
                        a := 0;
                        io.writeInt(a);
                    }
                }
            }
        """
        expect = "0"
        self.assertTrue(TestCodeGen.test(input,expect,527))

    def test_28(self):
        input = """
            class a{
                static d: float;
                bb: float;
                void static main(){
                    a: float;
                    e: boolean;
                    e := false;
                    {
                        a, b: int;
                        a := 0;
                        {
                            b : float;
                            io.writeInt(a);
                        }
                    }
                }
            }
        """
        expect = "0"
        self.assertTrue(TestCodeGen.test(input,expect,528))

    def test_29(self):
        input = """
            class a{
                static d: float;
                bb: float;
                void static main(){
                    a: int;
                    e: boolean;
                    e := false;
                    for a := 3 downto 1 do {
                        if a == 1 then {
                            break;
                        }
                    }

                    io.writeInt(a);
                }
            }
        """
        expect = "1"
        self.assertTrue(TestCodeGen.test(input,expect,529))

    def test_30(self):
        input = """
            class a{
                static d: float;
                bb: float;
                void static main(){
                    a: int;
                    e: boolean;
                    e := false;
                    for a := 3 downto 1 do {
                        if a == 1 then {
                            e := true;
                            break;
                        }
                    }

                    io.writeBool(e);
                }
            }
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,530))

    def test_31(self):
        input = """
            class a{
                static d: float;
                bb: float;
                void static main(){
                    a: int;
                    e: boolean;
                    e := false;
                    for a := 3 downto 1 do {
                        if a == 2 then {
                            continue;
                        }
                        io.writeInt(a);
                    }

                    io.writeBool(e);
                }
            }
        """
        expect = "31false"
        self.assertTrue(TestCodeGen.test(input,expect,531))

    def test_32(self):
        input = """
            class a {
                static d: float;
                bb: float;
                void static main(){
                    a: int;
                    e: boolean;
                    e := false;
                    b.foo();
                }
            }

            class b {
                void static foo(){
                    io.writeInt(1);
                }
            }
        """
        expect = "1"
        self.assertTrue(TestCodeGen.test(input,expect,532))

    def test_33(self):
        input = """
            class a {
                static d: float;
                bb: float;
                void static foo(){
                    io.writeInt(1);
                }

                void static main(){
                    a: int;
                    e: boolean;
                    e := false;
                    this.foo();
                }
            }

        """
        expect = "1"
        self.assertTrue(TestCodeGen.test(input,expect,533))

    def test_34(self):
        input = """
            class a{
                static d: float;
                bb: float;
                void static main(){
                    a: int;
                    e: boolean;
                    e := false;
                    a := 10;

                    {
                        {
                            a : float;
                            a := 4.0;
                            io.writeFloat(a);
                        }

                    }

                    io.writeInt(a);
                }
            }
        """
        expect = "4.010"
        self.assertTrue(TestCodeGen.test(input,expect,534))

    def test_35(self):
        input = """
            class a {
                void static foo2(){
                    io.writeInt(1);
                }
                void static main(){
                    io.writeInt(10);
                    b.foo2();
                }
            }

            class b {
                void static foo2(){
                    io.writeInt(1);
                }

            }

        """
        expect = "101"
        self.assertTrue(TestCodeGen.test(input,expect,535))

    def test_36(self):
        input = """
            class a {
                void static main(){
                    dem :int;
                    dem := b.foo2();
                    io.writeInt(dem);
                }
            }

            class b {
                int static foo2(){
                    return 1;
                }
            }

        """
        expect = "1"
        self.assertTrue(TestCodeGen.test(input,expect,536))

    def test_37(self):
        input = """
            class a {
                void static main(){
                    dem :int;
                    dem := b.foo2();
                    io.writeInt(b.foo2());
                }
            }

            class b {
                int static foo2(){
                    return 1;
                }
            }

        """
        expect = "1"
        self.assertTrue(TestCodeGen.test(input,expect,537))

    def test_38(self):
        input = """
            class a {
                void static main(){
                    dem :int;
                    dem := b.foo2();
                    io.writeBool(b.foo2());
                }
            }

            class b {
                int static foo2(){
                    return 1;
                }
            }

        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,538))

    def test_39(self):
        input = """
            class a {
                void static main(){
                    dem :int;
                    dem := b.foo2();
                    io.writeBool(b.foo2());
                }
            }

            class b {
                boolean static foo2(){
                    return true;
                }
            }

        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,539))

    def test_40(self):
        input = """
            class a {
                void static main(){
                    dem :string;
                    dem := b.foo2();
                    io.writeStr(b.foo2());
                }
            }

            class b {
                string static foo2(){
                    return "str";
                }
            }

        """
        expect = "str"
        self.assertTrue(TestCodeGen.test(input,expect,540))

    def test_41(self):
        input = """
            class a {
                void static main(){
                    final string dem = "str";
                    io.writeStr(dem);
                }
            }

            class b {
                string static foo2(){
                    return "str";
                }
            }

        """
        expect = "str"
        self.assertTrue(TestCodeGen.test(input,expect,541))

    def test_42(self):
        input = """
            class a {
                void static main(){
                    final boolean dem = true;
                    io.writeBool(dem);
                }
            }

            class b {
                string static foo2(){
                    return "str";
                }
            }

        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,542))

    def test_43(self):
        input = """
            class a {
                void static main(){
                    t: int;
                    t := 10;
                    io.writeInt(t);
                }
            }

            class b {
                static a, b: int;
                string static foo2(){
                    return "str";
                }
            }

        """
        expect = "10"
        self.assertTrue(TestCodeGen.test(input,expect,543))

    def test_44(self):
        input = """
            class a{
                static d: float;
                bb: float;
                void static main(){
                    d, f: int;
                    e: boolean;
                    e := false;
                    for d := 2 + 3 downto 1 do
                        io.writeIntLn(d);
                }
            }
        """
        expect = "5\n4\n3\n2\n1\n"
        self.assertTrue(TestCodeGen.test(input,expect,544))

    def test_45(self):
        input = """
            class a{
                static d: float;
                bb: float;
                void static main(){
                    d, f: int;
                    e: boolean;
                    e := true;
                    for d := 2 + 2 downto 1 do
                        break;
                    io.writeIntLn(d);
                }
            }
        """
        expect = "4\n"
        self.assertTrue(TestCodeGen.test(input,expect,545))

    def test_46(self):
        input = """
            class a{
                static d: float;
                bb: float;
                void static main(){
                    d, f: int;
                    e: boolean;
                    e := false;
                    for d := 2 + 2 downto 1 do
                        continue;
                    io.writeIntLn(d);
                    io.writeBool(e);
                }
            }
        """
        expect = "0\nfalse"
        self.assertTrue(TestCodeGen.test(input,expect,546))

    def test_47(self):
        input = """
            class a{
                static d: float;
                bb: float;
                void static main(){
                    a: float;
                    e: boolean;
                    e := false;
                    {
                        a, b: int;
                        a := 10;
                        io.writeInt(a);
                    }
                }
            }
        """
        expect = "10"
        self.assertTrue(TestCodeGen.test(input,expect,547))

    def test_48(self):
        input = """
            class a{
                static d: float;
                bb: float;
                void static main(){
                    a: float;
                    e: boolean;
                    e := false;
                    {
                        a, b: int;
                        a := -10;
                        {
                            b : float;
                            io.writeInt(a);
                        }
                    }
                }
            }
        """
        expect = "-10"
        self.assertTrue(TestCodeGen.test(input,expect,548))

    def test_49(self):
        input = """
            class a{
                static d: float;
                bb: float;
                void static main(){
                    a: int;
                    e: boolean;
                    e := false;
                    for a := 3 downto 1 do {
                        if a == 3 then {
                            break;
                        }
                    }

                    io.writeInt(a);
                }
            }
        """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,549))

    def test_50(self):
        input = """
            class a{
                static d: float;
                bb: float;
                void static main(){
                    a: int;
                    e: boolean;
                    e := false;
                    for a := 3 downto 1 do {
                        if a == 1 then {
                            e := false;
                            break;
                        }
                    }

                    io.writeBool(e);
                }
            }
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input,expect,550))

    def test_51(self):
        input = """
            class a{
                static d: float;
                bb: float;
                void static main(){
                    a: int;
                    e: boolean;
                    e := false;
                    for a := 3 downto 1 do {
                        if a == 3 then {
                            continue;
                        }
                        io.writeInt(a);
                    }

                    io.writeBool(e);
                }
            }
        """
        expect = "21false"
        self.assertTrue(TestCodeGen.test(input,expect,551))

    def test_52(self):
        input = """
            class a {
                static d: float;
                bb: float;
                void static main(){
                    a: int;
                    e: boolean;
                    e := false;
                    b.foo();
                }
            }

            class b {
                void static foo(){
                    io.writeInt(11);
                }
            }
        """
        expect = "11"
        self.assertTrue(TestCodeGen.test(input,expect,552))

    def test_53(self):
        input = """
            class a {
                static d: float;
                bb: float;
                void static foo(){
                    io.writeFloat(7.67);
                }

                void static main(){
                    a: int;
                    e: boolean;
                    e := false;
                    this.foo();
                }
            }

        """
        expect = "7.67"
        self.assertTrue(TestCodeGen.test(input,expect,553))

    def test_54(self):
        input = """
            class a{
                static d: float;
                bb: float;
                void static main(){
                    a: int;
                    e: boolean;
                    e := false;
                    a := 10;

                    {
                        {
                            a : float;
                            a := 4.0;
                            io.writeFloat(a - 1.0);
                        }

                    }

                    io.writeInt(a);
                }
            }
        """
        expect = "3.010"
        self.assertTrue(TestCodeGen.test(input,expect,554))

    def test_55(self):
        input = """
            class a {
                void static foo2(){
                    io.writeInt(1);
                }
                void static main(){
                    io.writeInt(10);
                    b.foo2();
                }
            }

            class b {
                void static foo2(){
                    io.writeInt(10);
                }

            }

        """
        expect = "1010"
        self.assertTrue(TestCodeGen.test(input,expect,555))

    def test_56(self):
        input = """
            class a {
                void static main(){
                    dem :int;
                    dem := b.foo2();
                    io.writeInt(dem);
                }
            }

            class b {
                int static foo2(){
                    return 1;
                }
            }

        """
        expect = "1"
        self.assertTrue(TestCodeGen.test(input,expect,556))

    def test_57(self):
        input = """
            class a {
                void static main(){
                    dem :int;
                    dem := b.foo2();
                    io.writeInt(b.foo2());
                }
            }

            class b {
                int static foo2(){
                    return -1;
                }
            }

        """
        expect = "-1"
        self.assertTrue(TestCodeGen.test(input,expect,557))

    def test_58(self):
        input = """
            class a {
                void static main(){
                    dem :int;
                    dem := b.foo2();
                    io.writeBool(b.foo2());
                }
            }

            class b {
                int static foo2(){
                    return 0;
                }
            }

        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input,expect,558))

    def test_59(self):
        input = """
            class a {
                void static main(){
                    dem :int;
                    dem := b.foo2();
                    io.writeBool(b.foo2());
                }
            }

            class b {
                boolean static foo2(){
                    return true;
                }
            }

        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,559))

    def test_60(self):
        input = """
            class a {
                void static main(){
                    dem :string;
                    dem := b.foo2();
                    io.writeStr(b.foo2());
                }
            }

            class b {
                string static foo2(){
                    return "strCMD";
                }
            }

        """
        expect = "strCMD"
        self.assertTrue(TestCodeGen.test(input,expect,560))

    def test_61(self):
        input = """
            class a {
                void static main(){
                    final string dem = "strTTT";
                    io.writeStr(dem);
                }
            }

            class b {
                string static foo2(){
                    return "str";
                }
            }

        """
        expect = "strTTT"
        self.assertTrue(TestCodeGen.test(input,expect,561))

    def test_62(self):
        input = """
            class a {
                void static main(){
                    final boolean dem = false;
                    io.writeBool(dem);
                }
            }

            class b {
                string static foo2(){
                    return "str";
                }
            }

        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input,expect,562))

    def test_63(self):
        input = """
            class a {
                void static main(){
                    t: int;
                    t := 10 - 9;
                    io.writeInt(t);
                }
            }

            class b {
                static a, b: int;
                string static foo2(){
                    return "str";
                }
            }

        """
        expect = "1"
        self.assertTrue(TestCodeGen.test(input,expect,563))


    def test_64(self):
        input = """
            class a{
                static d: float;
                bb: float;
                void static main(){
                    d: float;
                    d := 6 / 2;
                    io.writeFloat(d);
                }
            }
        """
        expect = "3.0"
        self.assertTrue(TestCodeGen.test(input,expect,564))

    def test_65(self):
        input = """
            class a{
                static d: float;
                bb: float;
                void static main(){
                    d: float;
                    e: boolean;
                    e := (1 > 1);
                    io.writeBool(e);
                }
            }
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input,expect,565))

    def test_66(self):
        input = """
            class a{
                static d: float;
                bb: float;
                void static main(){
                    d: float;
                    e: boolean;
                    e := (1 < 1);
                    io.writeBool(e);
                }
            }
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input,expect,566))

    def test_67(self):
        input = """
            class a{
                static d: float;
                bb: float;
                void static main(){
                    d: float;
                    e: boolean;
                    d := 44.5;
                    e := (d > 1);
                    io.writeBool(e);
                }
            }
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,567))

    def test_68(self):
        input = """
            class a{
                static d: float;
                bb: float;
                void static main(){
                    d: float;
                    e: boolean;
                    d := 4.5;
                    e := (d < 1) || (d > 3.3);
                    io.writeBool(e);
                }
            }
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,568))

    def test_69(self):
        input = """
            class a{
                static d: float;
                bb: float;
                void static main(){
                    d: float;
                    e: boolean;
                    d := 4.5;
                    e := (d != 1) && (d >= 3.3);
                    io.writeBool(e);
                }
            }
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,569))

    def test_70(self):
        input = """
            class a{
                static d: float;
                bb: float;
                void static main(){
                    d: float;
                    e: float;
                    d := 4.5;
                    e := 19 \\ 10;
                    io.writeFloat(e);
                }
            }
        """
        expect = "1.0"
        self.assertTrue(TestCodeGen.test(input,expect,570))

    def test_71(self):
        input = """
            class a{
                static d: float;
                bb: float;
                void static main(){
                    d: float;
                    e: float;
                    d := +++ 4.5;
                    io.writeFloat(d);
                }
            }
        """
        expect = "4.5"
        self.assertTrue(TestCodeGen.test(input,expect,571))

    def test_72(self):
        input = """
            class a{
                static d: float;
                bb: float;
                void static main(){
                    d: float;
                    e: float;
                    d := --- 4.5;
                    io.writeFloat(d);
                }
            }
        """
        expect = "-4.5"
        self.assertTrue(TestCodeGen.test(input,expect,572))

    def test_73(self):
        input = """
            class a{
                static d: float;
                bb: float;
                void static main(){
                    d: float;
                    e: float;
                    e := -4.1;
                    d := -e;
                    io.writeFloat(d);
                }
            }
        """
        expect = "4.1"
        self.assertTrue(TestCodeGen.test(input,expect,573))

    def test_74(self):
        input = """
            class a{
                static d: float;
                bb: float;
                void static main(){
                    d: float;
                    e: boolean;
                    e := !!!!(1 >= 10);
                    io.writeBool(e);
                }
            }
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input,expect,574))

    def test_75(self):
        input = """
            class a{
                static d: float;
                bb: float;
                void static main(){
                    d: float;
                    e: boolean;
                    e := !(1 < 10);
                    io.writeBool(e);
                }
            }
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input,expect,575))

    def test_76(self):
        input = """
            class a{
                static d: float;
                bb: float;
                void static main(){
                    d, f: int;
                    e: boolean;
                    e := false;
                    for d := 1 to 3 do
                        e := true;
                 
                    io.writeBool(e);
                }
            }
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,576))

    def test_77(self):
        input = """
            class a{
                static d: float;
                bb: float;
                void static main(){
                    d, f: int;
                    e: boolean;
                    e := 1 < 3;
                    for d := 1 to 3 do
                        io.writeBool(e);
                 
                    
                }
            }
        """
        expect = "truetruetrue"
        self.assertTrue(TestCodeGen.test(input,expect,577))

    def test_78(self):
        input = """
            class a {
                void static main(){
                    dem :int;
                    dem := b.foo2();
                    io.writeFloat(b.foo3());
                }
            }

            class b {
                float static foo3(){
                    return -7.7;
                }
                int static foo2(){
                    return 1;
                }
            }

        """
        expect = "-7.7"
        self.assertTrue(TestCodeGen.test(input,expect,578))

    def test_79(self):
        input = """
            class a {
                void static main(){
                    dem :int;
                    dem := b.foo2();
                    io.writeBool(b.foo2());
                }
            }

            class b {
                boolean static foo2(){
                    return 1 > 1;
                }
            }

        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input,expect,579))

    def test_80(self):
        input = """
            class a {
                void static main(){
                    dem :string;
                    dem := b.foo2();
                    io.writeStr(b.foo2());
                }
            }

            class b {
                string static foo2(){
                    return "strAB";
                }
            }

        """
        expect = "strAB"
        self.assertTrue(TestCodeGen.test(input,expect,580))

    def test_81(self):
        input = """
            class a {
                void static main(){
                    final string dem = "str";
                    io.writeStrLn(dem);
                }
            }

            class b {
                string static foo2(){
                    return "str";
                }
            }

        """
        expect = "str\n"
        self.assertTrue(TestCodeGen.test(input,expect,581))

    def test_82(self):
        input = """
            class a {
                void static main(){
                    final boolean dem = true;
                    io.writeBool(dem);
                }
            }

            class b {
                string static foo2(){
                    return "str";
                }
            }

        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,582))

    def test_83(self):
        input = """
            class a {
                void static main(){
                    t: int;
                    t := 10 * 10;
                    io.writeInt(t);
                }
            }

            class b {
                static a, b: int;
                string static foo2(){
                    return "str";
                }
            }

        """
        expect = "100"
        self.assertTrue(TestCodeGen.test(input,expect,583))

    def test_84(self):
        input = """
            class a{
                static d: float;
                bb: float;
                void static main(){
                    d, f: int;
                    for d := 2 + 3 downto 1 do
                        io.writeIntLn(d);
                }
            }
        """
        expect = "5\n4\n3\n2\n1\n"
        self.assertTrue(TestCodeGen.test(input,expect,584))

    def test_85(self):
        input = """
            class a{
                static d: float;
                bb: float;
                void static main(){
                    d, f: int;
                    e: boolean;
                    e := true;
                    for d := 2 + 2 downto 1 do
                        break;
                    io.writeIntLn(d);
                    io.writeBool(e);
                }
            }
        """
        expect = "4\ntrue"
        self.assertTrue(TestCodeGen.test(input,expect,585))

    def test_86(self):
        input = """
            class a{
                static d: float;
                bb: float;
                void static main(){
                    d, f: int;
                    e: boolean;
                    e := false;
                    for d := 2 + 2 downto -1 do
                        continue;
                    io.writeIntLn(d);
                    io.writeBool(e);
                }
            }
        """
        expect = "-2\nfalse"
        self.assertTrue(TestCodeGen.test(input,expect,586))

    def test_87(self):
        input = """
            class a{
                static d: float;
                bb: float;
                void static main(){
                    a: float;
                    e: boolean;
                    e := false;
                    {
                        a, b: int;
                        a := 10;
                        {
                            {

                                io.writeInt(a);
                            }
                        }
                    }
                }
            }
        """
        expect = "10"
        self.assertTrue(TestCodeGen.test(input,expect,587))

    def test_88(self):
        input = """
            class a{
                static d: float;
                bb: float;
                void static main(){
                    a: float;
                    e: boolean;
                    e := false;
                    {
                        a, b: int;
                        a := -10 * -1;
                        {
                            b : float;
                            io.writeInt(a);
                        }
                    }
                }
            }
        """
        expect = "10"
        self.assertTrue(TestCodeGen.test(input,expect,588))

    def test_89(self):
        input = """
            class a{
                static d: float;
                bb: float;
                void static main(){
                    a: int;
                    e: boolean;
                    e := false;
                    for a := 3 to 10 do {
                        if a == -3 then {
                            break;
                        }
                    }

                    io.writeInt(a);
                }
            }
        """
        expect = "11"
        self.assertTrue(TestCodeGen.test(input,expect,589))

    def test_90(self):
        input = """
            class a{
                static d: float;
                bb: float;
                void static main(){
                    a: int;
                    e: boolean;
                    e := false;
                    for a := 3 downto 1 do {
                        if a == 1 then {
                            e := 1 < 1;
                            break;
                        }
                    }

                    io.writeBool(e);
                }
            }
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input,expect,590))

    def test_91(self):
        input = """
            class a{
                static d: float;
                bb: float;
                void static main(){
                    d: float;
                    e: boolean;
                    e := !(1 >= 10);
                    io.writeBool(e);
                }
            }
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,591))

    def test_92(self):
        input = """
            class a{
                static d: float;
                bb: float;
                void static main(){
                    d: float;
                    e: boolean;
                    e := !!(1 < 10);
                    io.writeBool(e);
                }
            }
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,592))

    def test_93(self):
        input = """
            class a{
                static d: float;
                bb: float;
                void static main(){
                    d, f: int;
                    e: boolean;
                    e := false;
                    for d := 1 to 3 do
                    {
                        io.writeStr("*");
                        e := true;
                    }
                 
                    io.writeBool(e);
                }
            }
        """
        expect = "***true"
        self.assertTrue(TestCodeGen.test(input,expect,593))

    def test_94(self):
        input = """
            class a{
                static d: float;
                bb: float;
                void static main(){
                    d, f: int;
                    e: boolean;
                    e := 1 < 3;
                    for d := 1 to 3 - 2 do
                        io.writeBool(e);
                    
                }
            }
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,594))

    def test_95(self):
        input = """
            class a {
                void static main(){
                    dem :int;
                    dem := b.foo2();
                    io.writeFloat(b.foo3());
                }
            }

            class b {
                float static foo3(){
                    return -7.5 * 2;
                }
                int static foo2(){
                    return 1;
                }
            }

        """
        expect = "-15.0"
        self.assertTrue(TestCodeGen.test(input,expect,595))

    def test_96(self):
        input = """
            class a {
                void static main(){
                    dem :int;
                    dem := b.foo2();
                    io.writeBool(b.foo2());
                }
            }

            class b {
                boolean static foo2(){
                    return !(1 > 1);
                }
            }

        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,596))

    def test_97(self):
        input = """
            class a {
                void static main(){
                    dem :string;
                    dem := b.foo2();
                    io.writeStr(b.foo2());
                }
            }

            class b {
                string static foo2(){
                    return "strAB";
                }
            }

        """
        expect = "strAB"
        self.assertTrue(TestCodeGen.test(input,expect,597))

    def test_98(self):
        input = """
            class a {
                void static main(){
                    final string dem = "str";
                    io.writeStrLn(dem);
                    io.writeStrLn(b.foo2());
                }
            }

            class b {
                string static foo2(){
                    return "str";
                }
            }

        """
        expect = "str\nstr\n"
        self.assertTrue(TestCodeGen.test(input,expect,598))

    def test_99(self):
        input = """
            class a {
                void static main(){
                    final string dem = "str";
                    io.writeStrLn(dem);
                    io.writeFloat(b.foo2());
                }
            }

            class b {
                float static foo2(){
                    return 7.7;
                }
            }

        """
        expect = "str\n7.7"
        self.assertTrue(TestCodeGen.test(input,expect,599))