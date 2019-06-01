import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test_int(self):
        """Simple program: int main() {} """
        input = """procedure main(); begin putInt(100); end"""
        expect = "100"
        self.assertTrue(TestCodeGen.test(input,expect,500))
    def test_int_ast(self):
    	input = Program([
    		FuncDecl(Id("main"),[],[],[
    			CallStmt(Id("putInt"),[IntLiteral(5)])])])
    	expect = "5"
    	self.assertTrue(TestCodeGen.test(input,expect,501))

    def test_float_ast(self):
        input = Program([
            FuncDecl(Id("main"),[],[],[
                CallStmt(Id("putFloat"),[FloatLiteral(5.5)])])])
        expect = "5.5"
        self.assertTrue(TestCodeGen.test(input,expect,502))

    def test_float(self):
        input = """
        var a,b:integer;
        procedure main();
        begin putFloat(1e2); 
        end
        """
        expect = "100.0"
        self.assertTrue(TestCodeGen.test(input,expect,503))

    def test_1(self):
        input = """
        procedure foo();
        begin putFloat(1e2); 
        end
        procedure main();
        begin
            foo();
        end
        """
        expect = "100.0"
        self.assertTrue(TestCodeGen.test(input,expect,504))

    def test_2(self):
        input = """
        procedure foo();
        begin putFloat(1e2); 
        end
        procedure main();
        begin 
            putFloat(1e2); 
            foo();
        end
        """
        expect = "100.0100.0"
        self.assertTrue(TestCodeGen.test(input,expect,505))

    def test_6(self):
        input = """
        procedure foo(a:integer);
        begin 
            putFloat(1.4); 
        end
        procedure main();
        begin 
            foo(1);
        end
        """
        expect = "1.4"
        self.assertTrue(TestCodeGen.test(input,expect,506))

    def test_7(self):
        input = """
        //procedure foo(a:integer);
        //begin 
        //    putFloat(1.4); 
        //end
        procedure main();
        var a:integer;
        begin 
            a := 1;
            putFloat(1.4);
            //foo(a);
        end
        """
        expect = "1.4"
        self.assertTrue(TestCodeGen.test(input,expect,507))

    def test_8(self):
        input = """
        //procedure foo(a:integer);
        //begin 
        //    putFloat(1.4); 
        //end
        procedure main();
        var a:real;
        begin 
            a := 1.4;
            putFloat(1.4);
            //foo(a);
        end
        """
        expect = "1.4"
        self.assertTrue(TestCodeGen.test(input,expect,508))

    def test_9(self):
        input = """
        //procedure foo(a:integer);
        //begin 
        //    putFloat(1.4); 
        //end
        procedure main();
        var a:real;
        begin 
            a := 1.4;
            putFloat(a);
            //foo(a);
        end
        """
        expect = "1.4"
        self.assertTrue(TestCodeGen.test(input,expect,509))

    def test_10(self):
        input = """
        //procedure foo(a:integer);
        //begin 
        //    putFloat(1.4); 
        //end
        procedure main();
        var a:boolean;
        begin 
            a := True;
            putBool(a);
            //foo(a);
        end
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,510))

    def test_11(self):
        input = """
        procedure main();
        var a:String;
        begin 
            a := "asd";
            putString(a);
        end
        """
        expect = "asd"
        self.assertTrue(TestCodeGen.test(input,expect,511))

    def test_12(self):
        input = """
        procedure main();
        var a:String;
        begin 
            a := "asd";
            putStringLn(a);
        end
        """
        expect = "asd\n"
        self.assertTrue(TestCodeGen.test(input,expect,512))

    def test_13(self):
        input = """
        procedure main();
        begin 
            a := "asd";
            putStringLn(a);
        end
        var a:String;
        """
        expect = "asd\n"
        self.assertTrue(TestCodeGen.test(input,expect,513))

    def test_14(self):
        input = """
        procedure main();
        begin 
            a := fAlse;
            putBoolLn(a);
        end
        var a:boolean;
        """
        expect = "false\n"
        self.assertTrue(TestCodeGen.test(input,expect,514))

    def test_15(self):
        input = """
        procedure main();
        begin 
            a := 100.5;
            putFloatLn(a);
        end
        var a:real;
        """
        expect = "100.5\n"
        self.assertTrue(TestCodeGen.test(input,expect,515))

    def test_16(self):
        input = """
        procedure main();
        var a: integer;
        begin 
            a:=5;
            foo(a);
        end
        procedure foo(a:integer);
        begin
            putIntLn(a);
        end
        """
        expect = "5\n"
        self.assertTrue(TestCodeGen.test(input,expect,516))

    def test_17(self):
        input = """
        procedure main();
        var a: integer;
        begin 
            a:=5;
            z:=1.5;
            f(a,z);
        end
        procedure f(a:integer;b:real);
        begin
            putIntLn(a);
            putFloatLn(b);
        end
        var z:real;
        """
        expect = "5\n1.5\n"
        self.assertTrue(TestCodeGen.test(input,expect,517))

    def test_18(self):
        input = """
        procedure main();
        var a: integer;
        begin 
            a:=5;
            z:=1.5;
            foo(a);
        end
        procedure foo(a:integer);
        begin
            f(a,z);
        end
        procedure f(a:integer;b:real);
        begin
            putIntLn(a);
            putFloatLn(b);
        end
        var z:real;
        """
        expect = "5\n1.5\n"
        self.assertTrue(TestCodeGen.test(input,expect,518))

    def test_19(self):
        input = """
        procedure main();
        var main: integer;
        begin 
            main := 0;
            foo(main);
        end
        procedure foo(a:integer);
        begin
            putIntLn(a);
        end
        """
        expect = "0\n"
        self.assertTrue(TestCodeGen.test(input,expect,519))

    def test_20(self):
        input = """
        procedure main();
        var a,b: integer;
            c: real;
        begin 
            c:=a:=b:=5;
            f(a,c);
        end
        procedure f(a:integer;b:real);
        begin
            putIntLn(a);
            putFloatLn(b);
        end
        """
        expect = "5\n5.0\n"
        self.assertTrue(TestCodeGen.test(input,expect,520))

    def test_21(self):
        input = """
        procedure main();
        var a,b: integer;
            c: real;
        begin 
            c:=a:=b:=5;
            f(a,a);
        end
        procedure f(a:integer;b:real);
        begin
            putIntLn(a);
            putFloatLn(b);
        end
        """
        expect = "5\n5.0\n"
        self.assertTrue(TestCodeGen.test(input,expect,521))

    def test_22(self):
        input = """
        procedure main();
        var a,b: integer;
            c: real;
        begin 
            c:=a:=b:=5;
            putFloatLn(foo(a));
        end
        function foo(a:integer):real;
        begin
            return 5.0;
        end
        //procedure f(a:integer;b:real);
        //begin
        //    putIntLn(a);
        //    putFloatLn(b);
        //end
        """
        expect = "5.0\n"
        self.assertTrue(TestCodeGen.test(input,expect,522))

    def test_23(self):
        input = """
        procedure main();
        var a: integer;
        begin 
            a:=5;
            f(a,foo(a));
        end
        function foo(a:integer):real;
        begin
            return a;
        end
        procedure f(a:integer;b:real);
        begin
            putIntLn(a);
            putFloatLn(b);
        end
        """
        expect = "5\n5.0\n"
        self.assertTrue(TestCodeGen.test(input,expect,523))

    def test_24(self):
        input = """
        procedure main();
        var a: integer;
        begin 
            a:=5;
            f(a,foo(a));
        end
        function foo(a:integer):real;
        begin
            return a;
        end
        procedure f(a:integer;b:real);
        begin
            putIntLn(a);
            putFloatLn(b);
        end
        """
        expect = "5\n5.0\n"
        self.assertTrue(TestCodeGen.test(input,expect,524))

    def test_25(self):
        input = """
        var z:real;
        procedure main();
        var a: integer;
        begin 
            a:=5;
            z:=0.5;
            f(a,foo(a),z);
        end
        function foo(a:integer):real;
        begin
            return a;
        end
        procedure f(a:integer;b,c:real);
        begin
            putIntLn(a);
            putFloat(b);
            putString(" ");
            putFloatLn(c);
        end
        """
        expect = "5\n5.0 0.5\n"
        self.assertTrue(TestCodeGen.test(input,expect,525))

    def test_26(self):
        input = """
        procedure main();
        var a: integer;
        begin 
            a:=0;
            putFloatLn(foo(a));
        end
        function foo(a:integer):real;
        var str:string;
        begin
            str:="string";
            return foo2(str);
        end
        function foo2(x:string):real;
        begin
            putStringLn(x);
            return 0.5;
        end
        """
        expect = "string\n0.5\n"
        self.assertTrue(TestCodeGen.test(input,expect,526))

    def test_27(self):
        input = """
        procedure main();
        var a: integer;
        begin 
            a:=0;
            putFloatLn(foo(a));
        end
        function foo(a:integer):real;
        var str:string;
        begin
            str:="string";
            return foo2(str);
        end
        function foo2(x:string):real;
        begin
            return 0.5;
            putStringLn(x);
        end
        """
        expect = "0.5\n"
        self.assertTrue(TestCodeGen.test(input,expect,527))

    def test_28(self):
        input = """
        procedure main();
        var a: boolean;
        begin 
            a:=false;
            putBoolLn(a);
        end
        """
        expect = "false\n"
        self.assertTrue(TestCodeGen.test(input,expect,528))

    def test_29(self):
        input = """
        procedure main();
        var a: boolean;
        begin 
            z:=a:=false;
            putBoolLn(a);
        end
        var z:boolean;
        """
        expect = "false\n"
        self.assertTrue(TestCodeGen.test(input,expect,529))

    def test_30(self):
        input = """
        procedure main();
        var a: integer;
        begin 
            a:= 1+2;
            putIntLn(a);
        end
        """
        expect = "3\n"
        self.assertTrue(TestCodeGen.test(input,expect,530))

    def test_31(self):
        input = """
        procedure main();
        var a:real;
        begin 
            a:= 1+0.5;
            putFloatLn(1+0.5);
        end
        """
        expect = "1.5\n"
        self.assertTrue(TestCodeGen.test(input,expect,531))

    def test_32(self):
        input = """
        procedure main();
        var a:real;
        begin 
            a:= 1-0.5;
            putFloatLn(a);
        end
        """
        expect = "0.5\n"
        self.assertTrue(TestCodeGen.test(input,expect,532))

    def test_33(self):
        input = """
        procedure main();
        var a:real;
        begin 
            a:= 1*0.5;
            putFloatLn(a);
        end
        """
        expect = "0.5\n"
        self.assertTrue(TestCodeGen.test(input,expect,533))

    def test_34(self):
        input = """
        procedure main();
        var a:real;
        begin 
            a:= 1/0.5;
            putFloatLn(a);
        end
        """
        expect = "2.0\n"
        self.assertTrue(TestCodeGen.test(input,expect,534))

    def test_35(self):
        input = """
        procedure main();
        var a:real;
        begin 
            a:= 4 div 2 ;
            putFloatLn(a);
        end
        """
        expect = "2.0\n"
        self.assertTrue(TestCodeGen.test(input,expect,535))

    def test_36(self):
        input = """
        procedure main();
        var a:boolean;
        begin 
            a:= 1 <> 2 ;
            putBoolLn(a);
        end
        """
        expect = "true\n"
        self.assertTrue(TestCodeGen.test(input,expect,536))

    def test_37(self):
        input = """
        procedure main();
        var a:integer;
        begin 
            a :=3;
            if a > 0 then
                putIntLn(a);
        end
        """
        expect = "3\n"
        self.assertTrue(TestCodeGen.test(input,expect,537))

    def test_38(self):
        input = """
        procedure main();
        var a:integer;
        begin 
            a :=-1;
            if a > 0 then
                putIntLn(a);
            else
                putIntLn(5);
        end
        """
        expect = "5\n"
        self.assertTrue(TestCodeGen.test(input,expect,538))

    def test_39(self):
        input = """
        procedure main();
        var a:integer;
        begin 
            a :=3;
            if a > 0 then
                putIntLn(a);
            else
                putIntLn(5);
        end
        """
        expect = "3\n"
        self.assertTrue(TestCodeGen.test(input,expect,539))

    def test_40(self):
        input = """
        procedure main();
        var a:integer;
        begin 
            a :=-1;
            if a > 0 then
                putIntLn(a);
            else
                if a <= -1 then
                putIntLn(5);
        end
        """
        expect = "5\n"
        self.assertTrue(TestCodeGen.test(input,expect,540))

    def test_41(self):
        input = """
        procedure main();
        var a:integer;
        begin 
            a :=-1;
            if a > 0 then
                putIntLn(a);
            else
                if a < -1 then
                    putIntLn(5);
                else
                    putStringLn("correct");
        end
        """
        expect = "correct\n"
        self.assertTrue(TestCodeGen.test(input,expect,541))

    def test_42(self):
        input = """
        procedure main();
        var a:integer;
        begin 
            a :=2;
            if a > 0 then
                if a < -1 then
                    putIntLn(5);
                else
                    putStringLn("correct");
            else
                putIntLn(a);
        end
        """
        expect = "correct\n"
        self.assertTrue(TestCodeGen.test(input,expect,542))

    def test_43(self):
        input = """
        procedure main();
        var a:integer;
        begin 
            a :=2;
            if not true then
                if a < -1 then
                    putIntLn(5);
                else
                    putStringLn("correct");
            else
                putIntLn(a);
        end
        """
        expect = "2\n"
        self.assertTrue(TestCodeGen.test(input,expect,543))

    def test_44(self):
        input = """
        procedure main();
        var a:boolean;
        begin 
            a :=true;
            while not a do
            begin
                putBoolLn(a);
                a := not true;
            end
        end
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input,expect,544))

    def test_45(self):
        input = """
        procedure main();
        var a:boolean;
        begin 
            a :=true;
            while a do
            begin
                putBoolLn(a);
                a :=false;
            end
        end
        """
        expect = "true\n"
        self.assertTrue(TestCodeGen.test(input,expect,545))

    def test_46(self):
        input = """
        procedure main();
        var a:boolean;
            b:integer;
        begin 
            a :=true;
            b := 3;
            while b > 0 do
            begin
                putBoolLn(a);
                b := b - 1;
            end
        end
        """
        expect = "true\ntrue\ntrue\n"
        self.assertTrue(TestCodeGen.test(input,expect,546))

    def test_47(self):
        input = """
        procedure main();
        var a:boolean;
            b:integer;
        begin 
            a :=true;
            b := 3;
            while b > 0 do
            begin
                putIntLn(b);
                while a do
                begin
                    putBoolLn(a);
                    a:=not a;
                end
                b := b - 1;
            end
        end
        """
        expect = "3\ntrue\n2\n1\n"
        self.assertTrue(TestCodeGen.test(input,expect,547))

    def test_48(self):
        input = """
        procedure main();
        var a:boolean;
            b:integer;
        begin 
            a :=true;
            b := 3;
            wh(b,a);
        end
        procedure wh(a:integer;b:boolean);
        begin
            while a > 0 do
            begin
                putIntLn(a);
                while b do
                begin
                    putBoolLn(b);
                    b:=not b;
                end
                a := a - 1;
            end
        end
        """
        expect = "3\ntrue\n2\n1\n"
        self.assertTrue(TestCodeGen.test(input,expect,548))

    def test_49(self):
        input = """
        procedure main();
        var b:integer;
            a:integer;
        begin 
            a:= 1;
            for b:=0 to 5 do
            begin
                a:=a+1;
                putInt(b);
            end
            putLn();
            putInt(a);
        end
        """
        expect = "012345\n7"
        self.assertTrue(TestCodeGen.test(input,expect,549))

    def test_50(self):
        input = """
        procedure main();
        var b:integer;
            a:integer;
        begin 
            a:= 1;
            for b:=5 downto 0 do
            begin
                a:=a+1;
                putInt(b);
            end
            putLn();
            putInt(a);
        end
        """
        expect = "543210\n7"
        self.assertTrue(TestCodeGen.test(input,expect,550))

    def test_51(self):
        input = """
        procedure main();
        var b:integer;
            a:integer;
        begin 
            a:= 1;
            with a:integer;b:real; do
            begin
                a:= 10;
                putIntLn(a);
            end
            putInt(a);
        end
        """
        expect = "10\n1"
        self.assertTrue(TestCodeGen.test(input,expect,551))

    def test_52(self):
        input = """
        function sum(a:integer;n:integer):integer;
        var i:integer;
            sum:integer;
        begin
            sum:=0;
            for i:=a to n do
            begin
                sum:= sum + i;
            end
            return sum;
        end
        procedure main();
        var b:integer;
            a:integer;
        begin 
            a:= 1;
            b:= 9;
            b:= sum(a,b);
            putIntLn(b);
        end
        """
        expect = "45\n"
        self.assertTrue(TestCodeGen.test(input,expect,552))

    def test_53(self):
        input = """
        function sum(a:integer;n:integer):integer;
        var i:integer;
            sum:integer;
        begin
            sum:=0;
            for i:=a to n do
            begin
                sum:= sum + i;
                if i > 3 then
                    break;
            end
            return sum;
        end
        procedure main();
        var b:integer;
            a:integer;
        begin 
            a:= 1;
            b:= 9;
            b:= sum(a,b);
            putIntLn(b);
        end
        """
        expect = "10\n"
        self.assertTrue(TestCodeGen.test(input,expect,553))
    
    def test_54(self):
        input = """
        function sum(a:integer;n:integer):integer;
        var i:integer;
            sum:integer;
        begin
            sum:=0;
            for i:=a to n do
            begin
                sum:= sum + i;
                if i > 3 then
                    return i;
            end
            return sum;
        end
        procedure main();
        var b:integer;
            a:integer;
        begin 
            a:= 1;
            b:= 9;
            b:= sum(a,b);
            putIntLn(b);
        end
        """
        expect = "4\n"
        self.assertTrue(TestCodeGen.test(input,expect,554))

    def test_55(self):
        input = """
        function sum(a:integer;n:integer):integer;
        var i:integer;
            k:integer;
        begin
            if n < 0 then 
                return 0;
            return n + sum(a,n-1);
        end
        procedure main();
        var b:integer;
            a:integer;
        begin 
            a:= 1;
            b:= 9;
            b:= sum(a,b);
            putIntLn(b);
        end
        """
        expect = "45\n"
        self.assertTrue(TestCodeGen.test(input,expect,555))

    def test_56(self):
        input = """
        function sum(a:integer;n:integer):integer;
        var i:integer;
            k:integer;
        begin
            if n < 0 then 
                return 0;
            else
            return n + sum(a,n-1);
        end
        procedure main();
        var b:integer;
            a:integer;
        begin 
            a:= 1;
            b:= 9;
            b:= sum(a,b);
            putIntLn(b);
        end
        """
        expect = "45\n"
        self.assertTrue(TestCodeGen.test(input,expect,556))

    def test_57(self):
        input = """
        function sum(a:integer;n:integer):integer;
        var i:integer;
            k:integer;
        begin
            if n < 0 then 
                return 0;
            else
            return n + sum(a,n-1);
        end
        procedure main();
        var b:integer;
            a:integer;
        begin 
            a:= 1;
            b:= 9;
            b:= sum(a,b) + sum(a,5);
            putIntLn(b);
        end
        """
        expect = "60\n"
        self.assertTrue(TestCodeGen.test(input,expect,557))

    def test_58(self):
        input = """
        procedure foo(a:real;b:real);
        begin
            a:= a + b;
            b:= a - b;
            a:= a - b;
            return;
        end
        procedure main();
        var a,b,c:real;
        begin 
            a:= 1;
            b:= 9;
            foo(a,b);
            putFloatLn(a);
            putFloat(b);
        end
        """
        expect = "1.0\n9.0"
        self.assertTrue(TestCodeGen.test(input,expect,558))

    def test_59(self):
        input = """
        function foo(a:real;b:real):real;
        begin
            a:= a + b;
            b:= a - b;
            a:= a - b;
            return a;
        end
        procedure main();
        var a,b,c:real;
        begin 
            a:= 1;
            b:= 9;
            c:= foo(a,b);
            b:=foo(b,a);
            putFloatLn(c);
            putFloat(b);
        end
        """
        expect = "9.0\n1.0"
        self.assertTrue(TestCodeGen.test(input,expect,559))

    def test_60(self):
        input = """
        function foo(a:real;b:real):real;
        var i :integer;
        begin
            for i:= 0 to 10 do
            begin
                if i <2 then
                begin
                    putInt(i);
                    return i;
                end
                else
                    return 10;
            end
            return 10;
        end
        procedure main();
        var a,b,c:real;
        begin 
            a:= 1;
            b:= 9;
            c:= foo(a,b);
            putFloat(c);
        end
        """
        expect = "00.0"
        self.assertTrue(TestCodeGen.test(input,expect,560))

    def test_61(self):
        input = """
        function foo(a:real;b:real):real;
        var i :integer;
        begin
            i := 0;
            with a,b:integer; do
            begin
                if i <2 then
                begin
                    putInt(i);
                    return i;
                end
                else
                    return 10;
            end
        end
        procedure main();
        var a,b,c:real;
        begin 
            a:= 1;
            b:= 9;
            c:= foo(a,b);
            putFloat(c);
        end
        """
        expect = "00.0"
        self.assertTrue(TestCodeGen.test(input,expect,561))

    def test_62(self):
        input = """
        procedure foo(a:real;b:real);
        var i :integer;
        begin
            i := 0;
            with a,b:integer; do
            begin
                if i <2 then
                begin
                    putInt(i);
                    return;
                end
                else
                    a:= 0;//return 10;
            end
        end
        procedure main();
        var a,b,c:real;
        begin 
            a:= 1;
            b:= 9;
            foo(a,b);
            putFloat(b);
        end
        """
        expect = "09.0"
        self.assertTrue(TestCodeGen.test(input,expect,562))

    def test_63(self):
        input = """
        procedure main();
        var c:real;
        begin 
            c:=giaithua(3);
            putFloat(c);
        end
        function giaithua(n:integer):integer;
        begin
            if n<1 then return 1;
            else return n*giaithua(n-1);
        end
        """
        expect = "6.0"
        self.assertTrue(TestCodeGen.test(input,expect,563))

    def test_64(self):
        input = """
        procedure main();
        var c:real;
        begin 
            c:=giaithua(3);
            putFloat(c);
        end
        function giaithua(n:integer):integer;
        begin
            if n<1 then return 1;
            else return n*giaithua(n-1);
        end
        """
        expect = "6.0"
        self.assertTrue(TestCodeGen.test(input,expect,564))

    def test_65(self):
        input = """
        procedure main();
        var c:real;
        begin 
            c:=giaithua(3);
            putFloat(c);
        end
        function giaithua(n:integer):integer;
        begin
            if n<1 then return 1;
            else return n*giaithua(n-1);
        end
        """
        expect = "6.0"
        self.assertTrue(TestCodeGen.test(input,expect,565))

    def test_66(self):
        input = """
        procedure main();
        var c:real;
        begin 
            c:=foo(3);
            putFloat(c);
        end
        function foo(n:integer):integer;
        var i:integer;
        begin
            for i:= 0 to 5 do begin
                return 5;
            end
            return 4;
        end
        """
        expect = "5.0"
        self.assertTrue(TestCodeGen.test(input,expect,566))

    def test_67(self):
        input = """
        procedure main();
        var c:real;
        begin 
            c:=foo(3);
            putFloat(c);
        end
        function foo(n:integer):integer;
        var i:integer;
        begin
            i:= 0;
            with i:real; do
            begin
                i:= 10.5;
                putFloat(i);

            return 0;
            end
            putINt(i);
        end
        """
        expect = "10.50.0"
        self.assertTrue(TestCodeGen.test(input,expect,567))

    def test_68(self):
        input = """
        procedure main();
        var c:real;
        begin 
            c:=foo(3);
            putFloat(c);
        end
        function foo(n:integer):integer;
        var i:integer;
        begin
            i:= 0;
            with i:real;k:integer; do
            begin
                i:= 10.5;
                putFloat(i);
                for k:=0 to 5 do 
                    return 0;
            end
            return 0;
            putINt(i);
        end
        """
        expect = "10.50.0"
        self.assertTrue(TestCodeGen.test(input,expect,568))

    def test_69(self):
        input = """
        procedure main();
        var c:real;
        begin 
            c:=foo(3);
            putFloat(c);
        end
        function foo(n:integer):integer;
        var i:integer;
        begin
            i:= 0;
            with i:real;k:integer; do
            begin
                i:= 10.5;
                putFloat(i);
                for k:=0 to 5 do 
                    if k >3 then
                        return 0;
            end
            putINt(i);
            return 0;
        end
        """
        expect = "10.50.0"
        self.assertTrue(TestCodeGen.test(input,expect,569))

    def test_70(self):
        input = """
        procedure main();
        var c:real;
        begin 
            c:=foo(3);
            putFloat(c);
        end
        function foo(n:integer):integer;
        var i:integer;
        begin
            i:= 0;
            with i:real;k:integer; do
            begin
                k:= 5; 
                if k >3 then
                    return 0;
            end
            return 0;
            putINt(i);
        end
        """
        expect = "0.0"
        self.assertTrue(TestCodeGen.test(input,expect,570))

    def test_71(self):
        input = """
        procedure main();
        var c:real;
        begin 
            c:=foo(3);
            putFloat(c);
        end
        function foo(n:integer):integer;
        var i:integer;
        begin
            i:= 0;
            with i:integer; do
            begin
                i:= 5;
            end
            putINtlN(i);
            return 5;
        end
        """
        expect = "0\n5.0"
        self.assertTrue(TestCodeGen.test(input,expect,571))

    def test_72(self):
        input = """
        procedure main();
        var c:real;
        begin 
            c:=foo(3);
            putFloat(c);
        end
        function foo(n:integer):integer;
        var i:integer;
        begin
            i:= 0;
            if (1> 0) and then (0<1) then
                putINtlN(i);
            return 5;
        end
        """
        expect = "0\n5.0"
        self.assertTrue(TestCodeGen.test(input,expect,572))

    def test_73(self):
        input = """
        procedure main();
        var c:real;
        begin 
            c:=foo(3);
            putFloat(c);
        end
        function foo(n:integer):integer;
        var i:integer;
        begin
            i:= 0;
            if (-1> 0) and then (0<1) then
                putINtlN(i);
            return 5;
        end
        """
        expect = "5.0"
        self.assertTrue(TestCodeGen.test(input,expect,573))
    
    def test_74(self):
        input = """
        procedure main();
        var c:real;
        begin 
            c:=foo(3);
            putFloat(c);
        end
        function foo(n:integer):integer;
        var i:integer;
        begin
            i:= 0;
            if (2 > 0) or else (3<1) then
                putINtlN(i);
            return 5;
        end
        """
        expect = "0\n5.0"
        self.assertTrue(TestCodeGen.test(input,expect,574))

    def test_75(self):
        input = """
        procedure main();
        var c:real;
        begin 
            c:=foo(3);
            putFloat(c);
        end
        function foo(n:integer):integer;
        var i:integer;
        begin
            i:= 0;
            if (-1 > 0) or else (3<1) then
                putINtlN(i);
            return 5;
        end
        """
        expect = "5.0"
        self.assertTrue(TestCodeGen.test(input,expect,575))

    def test_76(self):
        input = """
        procedure main();
        var c:real;
        begin 
            c:=foo(3);
            putFloat(c);
        end
        function foo(n:integer):integer;
        var i:integer;
        begin
            n :=3;
            if n > 0 then
                return 0;
            return 0;
        end
        """
        expect = "0.0"
        self.assertTrue(TestCodeGen.test(input,expect,576))

    def test_77(self):
        input = """
        procedure main();
        var c:real;
        begin 
            c:=foo(9);
            putFloat(c);
        end
        function foo(n:integer):integer;
        var i:integer;
        begin
            while n > 0 do
            begin
                if n < 3 then
                    return 5;
                putInt(n);
                n:=n-1;
            end
            return 1;
        end
        """
        expect = "98765435.0"
        self.assertTrue(TestCodeGen.test(input,expect,577))

    def test_78(self):
        input = """
        procedure main();
        var c:real;
        begin 
            c:=foo(9);
            putFloat(c);
        end
        function foo(n:integer):integer;
        var i:integer;
        begin
            while n > 0 do
            begin
                return 5;
            end
            return 0;
        end
        """
        expect = "5.0"
        self.assertTrue(TestCodeGen.test(input,expect,578))

    def test_79(self):
        input = """
        procedure main();
        var c:real;
        begin 
            c:= foo(-3);
            putFloat(c);
        end
        function foo(n:integer):integer;
        var i:integer;
        begin
            if n > 0 then
                return 5;
            else return 2;
        end
        """
        expect = "2.0"
        self.assertTrue(TestCodeGen.test(input,expect,579))

    def test_80(self):
        input = """
        procedure main();
        var c:real;
        begin 
            c:= foo(-3);
            putFloat(c);
        end
        function foo(n:integer):integer;
        var i:integer;
        begin
            while n > 0 do
            begin
                return 5;
            end
            return 6;
        end
        """
        expect = "6.0"
        self.assertTrue(TestCodeGen.test(input,expect,580))

    def test_81(self):
        input = """
        procedure main();
        var c:real;
        begin 
            c:= foo(3);
            putFloat(c);
        end
        function foo(n:integer):integer;
        var i:integer;
        begin
            for i:=0 to n do
                return 5;
            return 6;
        end
        """
        expect = "5.0"
        self.assertTrue(TestCodeGen.test(input,expect,581))

    def test_82(self):
        input = """
        procedure main();
        var c:real;
        begin 
            c:= foo(3);
            putFloat(c);
        end
        function foo(n:integer):integer;
        var i:integer;
        begin
            if 3>0 then
                return 5;
            else
                return 1;
        end
        """
        expect = "5.0"
        self.assertTrue(TestCodeGen.test(input,expect,582))

    def test_83(self):
        input = """
        var i:integer;
        function f():integer;
        begin
            return 200;
        end
        procedure main();
        var
            main:integer;
        begin
            main := f();
            putIntLN(main);
            with i:integer;main:integer;f:integer;
            do begin
                main:=f:=i:=100;
                putIntln(i);
                puTinTln(main);
                PUTINTLN(f);
            end
            putIntln(main);
        end
        var g:real;
        """
        expect = "200\n100\n100\n100\n200\n"
        self.assertTrue(TestCodeGen.test(input,expect,583))

    def test_84(self):
        input = """
        var i:integer;
        function f():integer;
        begin
            return 200;
        end
        procedure main();
        var
            main:integer;
        begin
            main := f();
            with i:integer;main:integer;f:integer;
            do begin
                g:= 5.36;
                putFloat(g);
            end
            putFloatln(g);
        end
        var g:real;
        """
        expect = "5.365.36\n"
        self.assertTrue(TestCodeGen.test(input,expect,584))

    def test_85(self):
        input = """
        var i:integer;
        function f():integer;
        begin
            return 200;
        end
        procedure main();
        var
            main:integer;
        begin
            main := f();
            with i:integer;main:integer;f:integer;
            do begin
                g:= 5.36;
                putFloat(g);
            end
            putFloatln(g);
        end
        var g:real;
        """
        expect = "5.365.36\n"
        self.assertTrue(TestCodeGen.test(input,expect,585))

    def test_86(self):
        input = """
        procedure f();
        begin
            if foo() > 5 then
                putInt(5);
        end
        function foo():real;
        begin
            return 5.0;
        end
        procedure main();
        begin
            f();
        end
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input,expect,586))

    def test_87(self):
        input = """
        procedure f();
        begin
            if foo() > 5 then
                return;

            putint(0);
        end
        function foo():real;
        begin
            return 5.0;
        end
        procedure main();
        begin
            f();
        end
        """
        expect = "0"
        self.assertTrue(TestCodeGen.test(input,expect,587))


    def test_88(self):
        input = """
        procedure f(n:integer);
        begin
            if n > 5 then
                return;

            putint(0);
        end
        procedure main();
        begin
            f(9);
        end
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input,expect,588))

    def test_89(self):
        input = """
        procedure f(n:integer);
        begin
            for n:= 0 to 10 do
                if n = 3 then continue;
                else putint(n);
        end
        procedure main();
        begin
            f(9);
        end
        """
        expect = "01245678910"
        self.assertTrue(TestCodeGen.test(input,expect,589))

    def test_90(self):
        input = """
        procedure f(n:integer);
        begin
            for n:= 0 to 10 do
                if n = 3 then break;
                else putint(n);
        end
        procedure main();
        begin
            f(9);
        end
        """
        expect = "012"
        self.assertTrue(TestCodeGen.test(input,expect,590))

    def test_91(self):
        input = """
        procedure f(n:integer);
        begin
            for n:= 0 to 10 do
                with a:integer; do
                begin
                    if n = 3 then break;
                    else putint(n);
                end
        end
        procedure main();
        begin
            f(9);
        end
        """
        expect = "012"
        self.assertTrue(TestCodeGen.test(input,expect,591))

    def test_92(self):
        input = """
        procedure f(n:integer);
        begin
            for n:= 0 to 10 do
                with a:integer; do
                begin
                    if n = 3 then continue;
                    else putint(n);
                end
        end
        procedure main();
        begin
            f(9);
        end
        """
        expect = "01245678910"
        self.assertTrue(TestCodeGen.test(input,expect,592))

    def test_93(self):
        input = """
        procedure f(n:integer;m:integer);
        begin
            for n:= 0 to 2 do
            begin
                for m:= 0 to 3 do
                    if m = 2 then break;
                    else putInt(m);
                putInt(n);
                putLn();
            end
        end
        procedure main();
        begin
            f(9,0);
        end
        """
        expect = "010\n011\n012\n"
        self.assertTrue(TestCodeGen.test(input,expect,593))

    def test_94(self):
        input = """
        procedure f(n:integer;m:integer);
        begin
            for n:= 0 to 2 do
            begin
                for m:= 0 to 3 do
                    if m = 2 then continue;
                    else putInt(m);
                putInt(n);
                putLn();
            end
        end
        procedure main();
        begin
            f(9,0);
        end
        """
        expect = "0130\n0131\n0132\n"
        self.assertTrue(TestCodeGen.test(input,expect,594))

    def test_95(self):
        input = """
        procedure f(n:integer;m:integer);
        begin
            if n>0 then
                if m < 0 then
                    putInt(m);
                else 
                    return;
        end
        procedure main();
        begin
            f(9,0);
        end
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input,expect,595))

    def test_96(self):
        input = """
        procedure f(n:integer;m:integer);
        begin
            if n>0 then
                if m < 0 then
                    putInt(m);
                else 
                    return;
        end
        procedure main();
        begin
            f(9,-1);
        end
        """
        expect = "-1"
        self.assertTrue(TestCodeGen.test(input,expect,596))

    def test_97(self):
        input = """
        procedure f(n:integer;m:integer);
        begin
            if n>0 then
                if m < 0 then
                    putInt(m);
                else 
                    return;
            else
            begin
                for m:=0 to 10 do
                    putint(m);
            end
        end
        procedure main();
        begin
            f(-1,-1);
        end
        """
        expect = "012345678910"
        self.assertTrue(TestCodeGen.test(input,expect,597))

    def test_98(self):
        input = """
        procedure f(n:integer;m:integer);
        begin
            if n>0 then
                if m < 0 then
                    putInt(m);
                else 
                    return;
            else
            begin
                while m<0 do
                begin
                    putint(m);
                    m:= m +1;
                end
            end
        end
        procedure main();
        begin
            f(-1,-1);
        end
        """
        expect = "-1"
        self.assertTrue(TestCodeGen.test(input,expect,598))

    def test_99(self):
        input = """
        procedure f(n:integer;m:integer);
        begin
            if n>0 then
                if m < 0 then
                    putInt(m);
                else 
                    return;
            else
            begin
                while m<0 do
                begin
                    putint(m);
                    m:= m +1;
                end
            end
        end
        procedure main();
        begin
            f(-1,-5);
        end
        """
        expect = "-5-4-3-2-1"
        self.assertTrue(TestCodeGen.test(input,expect,599))
