import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):

    def test_simple_program(self):
        input = """procedure main (); begin end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))
    def test_simple_program_202(self):
        input = """PROCEDURE main (); begin end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,202))
    def test_wrong_miss_close(self):
        input = """PRocedure main( begin end"""
        expect = "Error on line 1 col 16: begin"
        self.assertTrue(TestParser.test(input,expect,203))
    def test_variable_declaration_204(self):
        input = """
        var x:integer;
        Procedure main();
        begin
           
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,204))
    def test_variable_declaration_205(self):

        input = """
        var x:integer;
            y,x,z:Integer;
        Procedure main();
        begin
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,205))
    def test_variable_declaration_206(self):
        input = """
        var x:integer;
            y,x,z:Integer;
            tem_:array[1 .. 5] of integer;
        Procedure main();
        begin
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,206))
    def test_variable_declaration_207(self):
        input = """
        var x:integer;
            y,x,z:reAl;
            tem_:array[1 .. 5] of integer;
        Procedure main();
        begin
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,207))
    def test_function_declaration_208(self):
        input = """ 
        function abc():integer;
        var a:integer;
        begin
        end
        Procedure main();
        begin
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,208))
    def test_function_declaration_209(self):
        input = """ 
        function abc():integer;
        var a:integer;
        begin
            a:=5;
            c:=b-5;
        end
        Procedure main();
        begin
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,209))
    def test_function_declaration_210(self):
        input = """ 
        function abc():array [1 .. 3] of real;
        var a:integer;
        begin
        end
        Procedure main();
        begin
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,210))
    def test_function_declaration_211(self):
        input = """ 
        function abc():array [1 .. 3] of string;
        var a,b,c,d:integer;
            x,y:array [1 .. 3] of string;
        begin
            a:=5;
            c:=b-5;
        end
        Procedure main();
        begin
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,211))
    def test_procedure_declaration_212(self):
        input = """ 
        Procedure abc();
        var a:integer;
            begin
            end
        Procedure main();
        begin
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,212))
    def test_procedure_declaration_213(self):
        input = """ 
        Procedure abc();
        var a,b,c,d:integer;
            x,y:array [1 .. 3] of string;
        begin
        end
        Procedure main();
        begin
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,213))
    def test_procedure_declaration_214(self):
        input = """ 
        Procedure abc();
        var a,b,c,d:integer;
            x,y:array [1 .. 3] of string;
        begin
            a:=5;
            c:=b-5;
        end
        Procedure main();
        begin
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,214))
    def test_assignment_stat_215(self):
        input = """ 
        Procedure main();
        begin
            a:= 5;
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,215))
    def test_assignment_stat_216(self):
        input = """ 
        Procedure main();
        begin
            a:=b:=c:= 5;
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,216))
    def test_assignment_stat_217(self):
        input = """ 
        Procedure main();
        begin
            a:=b:=c:= abc()[5];
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,217))
    def test_assignment_stat_218(self):
        input = """ 
        Procedure main();
        begin
            a:=b:=c:= abc()+dfc();
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,218))
    def test_assignment_stat_219(self):
        input = """ 
        Procedure main();
        begin
            //a:= n<10 and b>5;
            //a:=b:=c:= (abc()+dfc())[1];
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,219))
    def test_if_stat_220(self):
        input = """ 
        Procedure main();
        begin
            if a>b then
             a:=5;
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,220))
    def test_if_stat_221(self):
        input = """ 
        Procedure main();
        begin
            if a>b then
                a:=b;
            else
                b:=a;
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,221))
    def test_if_stat_222(self):
        input = """ 
        Procedure main();
        begin
            if a>b then
                if a>5 then
                    a:=b;
            else
                b:=a;
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,222))
    def test_if_stat_223(self):
        input = """ 
        Procedure main();
        begin
            if a>b then
                if a>5 then
                    a:=b;
                else
                    if a>3 then
                        a:=3;
                    else
                        a:=3;
            else
                b:=a;
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,223))
    def test_while_stat_224(self):
        input = """ 
        Procedure main();
        begin
            n:=2;
            while n<10 do
                n:=n*n;
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,224))
    def test_while_stat_225(self):
        input = """ 
        Procedure main();
        begin
            n:=2;
            while n<10 do
                n:=n*n;
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,225))
    def test_while_stat_226(self):
        input = """ 
        Procedure main();
        begin
            n:=2;
            while ((n<10) and (a>b)) do
                n:=n*n;
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,226))
    def test_exp_227(self):
        input = """ 
        Procedure main();
        begin
            n:= a or b;
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,227))
    def test_exp_228(self):
        input = """ 
        Procedure main();
        begin
            n:= a or b or c and d;
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,228))
    def test_exp_229(self):
        input = """ 
        Procedure main();
        begin
            n:= a or b or c and d;
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,229))
    def test_exp_230(self):
        input = """ 
        Procedure main();
        begin
            n:= a or b or c and d or e and f and g;
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,230))
    def test_exp_231(self):
        input = """ 
        Procedure main();
        begin
            n:= 5>=a;
            m:= 6<=5;
            q:= 5<>2;
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,231))
    def test_exp_232(self):
        input = """ 
        Procedure main();
        begin
            n:= true;
            m:= false;
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,232))
    def test_exp_233(self):
        input = """ 
        Procedure main();
        begin
            n:= not a;
            m:= a+-c;
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,233))
    def test_exp_234(self):
        input = """ 
        Procedure main();
        begin
            n:= not (not a);
            //n:= not not a
            m:= - (-c);
            //m:= --c;
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,234))
    def test_exp_235(self):
        input = """ 
        Procedure main();
        begin
            n:= 5--6;
            m:= m+5;
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,235))
    def test_exp_236(self):
        input = """ 
        Procedure main();
        begin
            a:=a+5;
            b:=a-5;
            c:=5/2;
            d:=6*5;
            e:=g mod 5;
            g:=h div 5;
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,236))
    def test_exp_237(self):
        input = """ 
        Procedure main();
        begin
            a:= c/5/5-3+2--2*123+b;
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,237))
    def test_exp_238(self):
        input = """ 
        Procedure main();
        begin
            a:= a and b and not c and d;
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,238))
    def test_exp_239(self):
        input = """ 
        Procedure main();
        begin
            a:= 5+bcd()+edf()[1];
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,239))
    def test_exp_240(self):
        input = """ 
        Procedure main();
        begin
            n:= a(1,2)[b(123+5)[c(174.145)]];
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,240))
    def test_while_241(self):
        input = """ 
        Procedure main();
        begin
            n:=1;
            S:=0;
            while n<10 do
            begin
                S:=S+n;
                n:=n+1;
            end
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,241))
    def test_while_242(self):
        input = """ 
        Procedure main();
        begin
            n:=1;
            S:=0;
            while (n<10) and (s<20) do
            begin
                S:=S+n;
                n:=n+1;
            end
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,242))
    def test_while_242(self):
        input = """ 
        Procedure main();
        begin
            n:=1;
            S:=0;
            while (n<10) and (s<20) do
            begin
                S:=S+n;
                n:=n+1;
            end
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,242))
    def test_while_243(self):
        input = """ 
        Procedure main();
        begin
            n:=1;
            S:=0;
            while (n<10) and (s<20) do
                n:=n+1;
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,243))
    def test_for_244(self):
        input = """ 
        Procedure main();
        begin
            n:=10;
            S:=1;
            for i:=1 to n do
                S:=S*i;
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,244))
    def test_for_244(self):
        input = """ 
        Procedure main();
        begin
            n:=10;
            S:=1;
            for i:=1 to n do
            begin
                S:=S*i;
                if(S>20) then
                    break;
            end
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,244))
    def test_for_245(self):
        input = """ 
        Procedure main();
        begin
            n:=10;
            S:=1;
            for i:=n downto i do
            begin
                S:=S*i;
                if(S>20) then
                    break;
            end
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,245))
    def test_for_246(self):
        input = """ 
        Procedure main();
        begin
            n:=10;
            S:=1;
            for i:=n downto i do
            begin
                S:=S*i;
                if(S>20) then
                    continue;
            end
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,246))
    def test_with_247(self):
        input = """Procedure main();begin
            
            while 1<2 do begin
            end
                b := c[a]+b;
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,247))
    def test_with_248(self):
        input = """ 
        Procedure main();
        begin
            with a:integer;b: array [1 .. 2] of real;do
                begin
                    a:=2;
                    b:= function1();
                end
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,248))
    def test_call_function_249(self):
        input = """ 
        Procedure main();
        begin
            n:= fucntion1(a,b,c);
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,249))

    def test_call_function_250(self):
        input = """
        //var a:array[1-2..5] ;
        Procedure main();
        begin
            k:=5+--5--------5;
            n:=--5;
            m:=not not a;
            if 5<-15 then
            a:=5;
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,250))
    def test_call_function_251(self):
        input = """ 
        var i:integer;
        function f():integer;
        begin
            return 200;
        end
        procedure main();
        var main_:integer;
        begin
            main:=f();
            putIntLn(main );
            with
                i : integer ;
                main : integer ;
                f : integer ;
            do begin
                main := f := i := 100;
                putIntLn( i );
                putIntLn(main );
                putIntLn( f );
            end
            putIntLn(main );
        end
        var g : real ;
        """ 
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,251))
    def test_all_252(self):
        input = """
        var a:array[5 .. 5] of integer;
        Procedure main();
        begin
            k:=5+--5--------5;
            n:=--5;
            m:=not not a;
            if 5<-15 then
            a:=5;
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,252))
    def test_all_253(self):
        input = """
        Procedure main();
        var a,b,c,x,y,z:integer;
        begin
            if(y<5)and(z<10)then
            begin
            end
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,253))
    def test_all_254(self):
        input = """
        Procedure main();
        var a,b,c,x,y,z:integer;
        begin
            if(y<5)and(z<10)then
            begin
            end
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,254))
    def test_all_255(self):
        input = """
        var x:integer;
        var y:real;
        Procedure main();
        var a,b:integer;
        begin
            if(y<5)and(y<10)then
            begin
                x:=a;
                y:=b;
                putIntLn( x );
                putIntLn( y );
            end
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,255))
    def test_all_256(self):
        input = """
        var x:integer;
        var y:real;
        function increase(x:integer):integer;
        begin
            return x+1;
        end
        Procedure main();
        var a,b:integer;
        begin
            putIntLn(increase(x));
            putIntLn(increase(y));
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,256))
    def test_all_257(self):
        input = """
        var x,y:integer;
        Procedure main();
        var a,b:integer;
        begin
            putIntLn(--increase(--x));
            putIntLn(--increase(--y));
        end
        function increase(x:integer):integer;
        begin
            return x+1;
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,257))
    def test_all_258(self):
        input = """ 
        var i:integer;
        function square(i:integer):integer;
        begin
            return f*f;
        end
        procedure main();
        var main,x:integer;
        begin
            main:=square(x);
            putIntLn(main);
            with
                i : integer ;
                main : integer ;
                f : integer ;
            do begin
                main := f := i := 100;
                putIntLn(i);
                putIntLn(main);
                putIntLn(f);
            end
            putIntLn(main);
        end
        var g : real ;  
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,258))
    def test_all_259(self):
        input = """
        Procedure main();
        begin
            putIntLn("Hello Word!!!");
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,259))



    def test_all_260(self):
        input = """
        Procedure main();
        begin
            putIntLn("Hello Word!!!");
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,260))
    def test_all_261(self):
        input = """
        function giaithua(n:integer):integer;
        var gt:integer;
        begin
            gt:=1;
            for i:=1 to n do
            begin
                gt:= gt*i;
            end
            return gt;
        end
        Procedure main();
        begin
            putIntLn(giaithua(5));
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,261))
    def test_all_262(self):
        input = """
        function tong(n:integer):integer;
        var tong_:integer;
        begin
            tong_:=0;
            for i:=1 to n do
            begin
                tong_ := tong_+i;
            end
            return tong_;
        end
        Procedure main();
        begin
            putIntLn(tong(5));
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,262))
    def test_all_263(self):
        input = """
        function tong_array(arr:array[1 .. 10] of integer):integer;
        var tong_:integer;
        begin
            tong_:=0;
            for i:=1 to 10 do
            begin
                tong_ := tong_+arr[i];
            end
            return tong_;
        end
        Procedure main();
        var k: array[1 .. 10] of integer;
        begin
            putIntLn(tong_array(k));
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,263))
    def test_all_264(self):
        input = """
        function max_element_array(arr:array[1 .. 10] of integer):integer;
        var index_:integer;
        begin
            index:=1;
            for i:=2 to 10 do
            begin
                if(arr[i]>arr[index]) then
                begin
                    index := i;
                end
            end
            return index;
        end
        Procedure main();
        var k: array[1 .. 10] of integer;
        begin
            putIntLn(max_element_array(k));
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,264))

    def test_all_265(self):
        input = """
        function min_element_array(arr:array[1 .. 10] of integer):integer;
        var index_:integer;
        begin
            index:=1;
            for i:=2 to 10 do
            begin
                if(arr[i]<arr[index]) then
                begin
                    index := i;
                end
            end
            return index;
        end
        Procedure main();
        var k: array[1 .. 10] of integer;
        begin
            putIntLn(min_element_array(k));
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,265))
    def test_all_266(self):
        input = """
        function sum_odd_element_array(arr:array[1 .. 10] of integer):integer;
        var tong_:integer;
        begin
            tong_:=0;
            for i:=1 to 10 do
            begin
                if(arr[i] mod 2 = 1) then
                begin
                    tong_:=tong_+arr[i];
                end
            end
            return tong_;
        end
        Procedure main();
        var k: array[1 .. 10] of integer;
        begin
            putIntLn(sum_odd_element_array(k));
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,266))
    def test_all_267(self):
        input = """
        Procedure main();
        begin
            putIntLn("Hello Word!!!\\n");
            putIntLn("Hello Word!!!\\n");
            putIntLn("Hello Word!!!\\n");
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,267))
    def test_all_268(self):
        input = """
        function sum_even_element_array(arr:array[1 .. 10] of integer):integer;
        var tong_:integer;
        begin
            tong_:=0;
            for i:=1 to 10 do
            begin
                if(arr[i] mod 2 = 2) then
                begin
                    tong_:=tong_+arr[i];
                end
            end
            return tong_;
        end
        Procedure main();
        var k: array[1 .. 10] of integer;
        begin
            putIntLn(sum_even_element_array(k));
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,268))
    def test_all_269(self):
        input = """
        function sum_2_int(a,b:integer):integer;
        begin
            return a+b;
        end
        Procedure main();
        begin
            putIntLn(sum_2_int(1,2));
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,269))

    def test_all_270(self):
        input = """
        function sum_2_int(a,b:integer):integer;
        begin
            return a+b;
        end
        Procedure main();
        begin
            putIntLn(sum_2_int(1,2));
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,270))
    def test_all_271(self):
        input = """
        function div_2_int(a,b:integer):integer;
        begin
            return a/b;
        end
        Procedure main();
        begin
            putIntLn(div_2_int(1,2));
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,271))
    def test_all_272(self):
        input = """
        function mul_2_int(a,b:integer):integer;
        begin
            return a*b;
        end
        Procedure main();
        begin
            putIntLn(mul_2_int(1,2));
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,272))
    def test_all_273(self):
        input = """
        function sub_2_int(a,b:integer):integer;
        begin
            return a---b;
        end
        Procedure main();
        begin
            putIntLn(sum_2_int(1,2));
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,273))

    def test_all_274(self):
        input = """
        function sum_2_int(a,b:integer):integer;
        begin
            return a+b;
        end
        Procedure main();
        begin
            if(a-b = c-d) then
            begin
            end
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,274))
    def test_all_275(self):
        input = """
        Function kt(n:integer):boolean;
        var i,d:integer;
        begin
            kt:=false;
            d:=0;
            For i:=1 to n do
                if n mod i=0 then inc(d);
            if d=2 then kt:=true;
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,275))
    def test_all_276(self):
        input = """
        Procedure main();
        var n: integer;
            m,tong,i: integer;
        BEGIN
            
            write("Nhap n:"); readln(n);
            write("Nhap m: "); readln(m);
            for i:=1 to m do
            begin
                tong:=tong+(n mod 10);
                n:=n div 10;
            end
            
        END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,276))
    def test_all_277(self):
        input = """
        procedure main();
        var a,b,c,cubic_sum,num:integer;
        begin
            for a:=1 to 9 do
                for b:=0 to 9 do
                begin
                    for c:=0 to 9 do
                    begin
                    cubic_sum:=(a*a*a)+(b*b*b)+(c*c*c);
                    num:=(100*a)+(10*b)+c;
                        if (cubic_sum=num) then writeln(num);
                    end
                end
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,277))
    def test_all_278(self):
        input = """
        procedure main();
        var iterations:integer;
            phi1,phi2:real;
        begin
            phi1:=1;
            iterations:=0;
            
            while(abs(phi1-phi2)<epsilon) do
            begin
                phi2:=phi1;
                phi1:=sqrt(1+phi1);
                iterations:=iterations+1;
            end
            putIntLn("aaa : ",phi1);
            putIntLn("aaa : ",iterations);
            //writeln("Found: ",phi1);
            //writeln("dkdkdkdkL ",iterations);
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,278))
    def test_all_279(self):
        input = """
        function factorial(n:integer):integer;
        var i:integer;
            prod:integer;
        begin
            prod:=1;
            for i:=1 to n do prod:=prod*i;
            factorial:=prod;
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,279))

    def test_all_280(self):
        input = """
        function power(x:real;y:integer):real;
        var p:real;
            i:integer;
        begin
            p:=1;
            for i:=1 to y do p:=p*x;
            power:=p;
        end
        procedure main();
        var x:real;
            y:integer;
        begin
            putIntLn("aaa : ",power(x,y));
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,280))
    def test_all_281(self):
        input = """
        function isPrime(n:integer):boolean;
        var i:integer;
            isDiv:boolean;
        begin
            if (n=1) then isPrime:=false;
            else
            BEGIN
                isDiv:=false;
                for i:=2 to trunc(sqrt(n)) do
                   if ((n mod i)=0) then isDiv:=true;
                if (isDiv) then isPrime:=false;
                else isPrime:=true;
            END
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,281))
    def test_all_282(self):
        input = """
        procedure main(n:integer);
        begin
            if(a>b)then a:=b;
            else
            begin
                a:=-b;
            end
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,282))
    def test_all_283(self):
        input = """
        procedure main();
        var sum,i:integer;
        begin
            sum:=0;
            for i:=1 to 10 do sum:=sum+i;
            writeln(sum);
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,283))
    def test_all_284(self):
        input = """
        procedure main();
        Var a,b,x:real;
        Begin
        putIntLn("Nhap a: ");readln(a);
        putIntLn("Nhap a: "); 
        If(a=0) then
        If(b=0) then putIntLn("phuong trinh co vo so nghiem "); Else 
        putIntLn("phuong trinh vo nghiem ");
        Else
        Writeln("Phuong trinh co nghiem x=",-b/a); 
        End"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,284))
    def test_all_285(self):
        input = """
        function factorial(n:integer):integer;
        var i:integer;
            prod:integer;
        begin
            prod:=1;
            for i:=1 to n do prod:=prod*i*i*i*i*i;
            factorial:=prod;
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,285))
    def test_all_286(self):
        input = """
        procedure main();
        var ArrInt : array[1 .. 250] of integer;   
                    n,i,x : integer;
                    a: integer; 
        BEGIN
        write("Nhap so phan tu: ");
        for i:=1 to n do
            begin
                write("Phan tu thu ",i,"= ");
                readln(a[i]);
            end
            writeln("Cac so chinh phuong co trong mang:");
            for i:=1 to n do
            begin
            x:=trunc(sqrt(a[i]));
                if sqr(x)=a[i] then
                write(a[i]);
            end
        END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,286))
    def test_all_287(self):
        input = """
        procedure main();
        var n: string;
            m,i,a,tong: integer;
        BEGIN
           write("Nhap so n: "); readln(n);
           write("Nhap m: "); readln(m);
           for i:= length(n) downto length(n)-m+1 do
             begin
                 val(n[i],a);
                 tong:=tong+a;
             end
           write(tong);
        END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,287))
    def test_all_288(self):
        input = """
        var s,n,j,i:integer;
            a:Array[1 .. 100] of integer;
        Procedure print();
        var j:integer;
        begin
            For j:=1 to n do write(a[j]," ");
        end
        Procedure Deq(i:integer);
        var j,k,d:integer;
        begin
            For j:=0 to 1 do
                begin
                d:=0;
                a[i]:=j;
                if i=n then
                For k:=1 to n do
                    begin
                    if (a[k]=0) and (a[k+1]=1) then inc(d);
                    if d=2 then  print();
                    end
                else Deq(i+1);
            end
          end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,288))
    def test_all_289(self):
        input = """
        procedure main();
        var n, i, j, count: integer;
        begin
            write("Nhap N (N>=1): "); readln(n);
            for i:=1 to n do
            begin
                j:=i;
                while j mod 5 = 0 do
                begin
                    j:=j div 5;
                    count:=count+1;
                end
            end
            write(" So chu so 0 cuoi cua ",n,"! la: ",count);
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,289))
    def test_all_290(self):
        input = """
        procedure main();
        var a,b:integer;
             bo:boolean;
        begin
            write("Nhap nam :");readln(b);
            if (b mod 100=0) then bo:=(b mod 400)=0 ;else
                                  bo:=(b mod 4   )=0;
            if bo then
                begin
                 while (a>0) and (a<13) do
                    write("Nhap thang :");readln(a);
                end
            if (not bo) then
                begin
                end
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,290))


    def test_all_291(self):
        input = """
        procedure main();
        Var a,b,c : integer;
        Begin
            Write("Nhap vao 3 so : ");Readln(a,b,c);
            If a>b then
            Begin
                a := a + b;
                b := a - b;
                a := a - b;
            End
            If b>c then
            Begin
                b := b + c;
                c := b - c;
                b := b - c;
            End
            If a>b then
            Begin
                a := a + b;
                b := a - b;
                a := a - b;
            End
            Writeln("Min = ",a);
            Writeln("Max = ",c);
        End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,291))
    def test_all_292(self):
        input = """
        procedure main();
        Var    St:String;
               dem: Array[1 .. 10] Of string;
               i:string;
               ch:string;
        Begin
            Write("Nhap xau St: "); Readln(St);
            For ch:="A" To "Z" Do dem[ch]:=0;
           
            For ch:="A" To "Z" Do 
                If dem[ch]>0 Then Writeln(ch," : ",dem[ch]);
        End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,292))
    def test_all_293(self):
        input = """
        procedure main();
        VAR i,n :INTEGER;
        BEGIN
            Write ("Nhap n:");
            Readln(n);
            Write (n,"=");
            i:=2;
            While n<>1 do 
            Begin
                WHILE n MOD i <> 0 DO
                    i:=i+1;
                Write(i);
                n:=n DIV i;
                IF n > 1 THEN
                    write ("*");
            end
        END
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,293))
    def test_all_294(self):
        input = """
        procedure main();
        var s:string;
            x,y,z,t:string;
        begin
          write("Nhap vao mot xau: ");
          readln(s);
          z:=length(s);
          for y:=length(s) downto 1 do
          begin
            if ((s[y]=" ")or(y=1)) then 
            begin 
                for t:=y to z do 
                    begin
                    write(s[t]);
                    z:=y;
                    end 
            end
            write(" ");
          end
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,294))
    def test_all_295(self):
        input = """
        procedure main();
        var tcha,tcon,nam,kq:string;
        begin
            write("nhap tuoi con");
            readln(tcon);
            write();readln(tcha);
            while tcha<>2*tcon do
            begin
                nam:=nam+1;
                tcon:=tcon+1;
                tcha:=tcha+1;
            end
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,295))
    def test_all_296(self):
        input = """
        procedure main();
        var x,y,UCLN,BCNN:integer;
        begin
            readln(x,y);
            BCNN:=x*y;
            While x<>y do If x>y then x:=x-y; else y:=y-x;
            UCLN:=x;
            BCNN:=BCNN div UCLN;
            write(UCLN," ",BCNN);
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,296))
    def test_all_297(self):
        input = """
        procedure main();
        VAR thang,i, tn, tn_1, tn_2:INTEGER;
        BEGIN            
            write("Nhap so thang: ");
            readln(thang);
            IF thang>2 THEN
            BEGIN
                tn_2:=1; {Thang dau tien co 1 cap tho}
                tn_1:=1; {Thang thu 2 van co 1 cap tho}
                FOR i:=3 TO thang DO
                BEGIN
                    tn:=tn_1 + tn_2;
                    tn_2:=tn_1;
                    tn_1:=tn;
                END
            END
            ELSE
                tn:=1;
            writeln("So con tho sau ",thang," thang la: ",2*tn);
        END
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,297))
    def test_all_298(self):
        input = """
        procedure main();
        Var a:array[1 .. 100] of integer;
            n,i:integer;
        Begin
          write("Do dai cua mang can nhap?");
          readln(n);
          For i:=1 to n do 
          begin
            write("Phan tu thu ",i,"=?");
            readln(a[i]);
          end
          writeln("Mang dao nguoc la :");
          For i:=n downto 1 do write(a[i]);
        End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,298))
    def test_all_299(self):
        input = """
        VAR n:INTEGER;
        FUNCTION kiemtra(x:INTEGER):BOOLEAN;
        VAR tam,i:INTEGER;
        BEGIN
            tam:=0; kiemtra:=FALSE;
            FOR i:= 1 TO (x DIV 2) DO
            IF x MOD i = 0 THEN tam:=tam+i;
            IF tam = x THEN kiemtra:=TRUE;
        END
        procedure main();
        BEGIN
            writeln("Nhap so can kiem tra ");
            readln(n);
            IF kiemtra(n) THEN writeln("So ",n," la so hoan thien");
            ELSE
            writeln("So ",n," khong phai la so hoan thien");
        END
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,299))
    def test_all_300(self):
        input = """
        Function kt(n:integer):boolean;
        var i,d:integer;
        begin
            kt:=false;
            d:=0;
            For i:=1 to n do
                if n mod i=0 then inc(d);
            if d=2 then kt:=true;
        end
        { abcxyz }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,300))