import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_first_test(self):
        input = """procedure main(); 
                    begin

                    end
                    var a: real;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,200))
    def test_simple_program(self):
        input = """procedure main(); 
                    begin end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))
    def test_simple_program1(self):
        input = """Procedure main(); var a : real; begin  end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,202))
    def test_simple_program2(self):
        input = """
                    function lol(a,b : integer; c: real):real;
                        var x,y : integer;
                        begin
                        END
                    Procedure main();
                    var a : real; 
                    begin 
                        a:=6*7;
                    end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,203))
    def test_simple_program3(self):
        input = """procedure lol(a,b : integer; c: real);
                        var x,y : integer;
                        begin
                        END
                    Procedure main();
                    var a : real; 
                    begin 
                    end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,204))
    def test_simple_program4(self):
        input = """
                    procedure lol(a,b : integer; c: real);
                        var x,y : integer;
                        begin
                        end
                    Procedure main();
                    var a : real; 
                    begin 
                        
                    end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,205))
    def test_simple_program5(self):
        input = """Procedure main();
                    var a : array [1 .. 4] of integer;                
                    begin 
                    end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,206))
    def test_simple_program6(self):
        input = """Procedure main();
                   begin 
                        a:=3;
                        a:=k:=3;
                   end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,207))
    def test_simple_program7(self):
        input = """Procedure main();
                    begin 
                        a[2] := k[2] := kmg[4] := -10;
                    end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,208))
    def test_simple_program8(self):
        input = """Procedure main();
                    begin 
                        a[k[2]] := LOLP[2222] := 2*3-6/2;
                    end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,209))
    def test_simple_program9(self):
        input = """Procedure main();
                    begin 
                        conoichaydi(x,s,3+2);
                    end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,210))
    def test_simple_program10(self):
        input = """procedure foo(k : array[1 .. 4] of integer);
                            var x : real;
                            begin
                                phu(2); 
                            end
                    Procedure main();
                    var a:integer;
                    d: array [1 .. 5] of real;
                   begin 
                        
                    end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,211))
    def test_simple_program11(self):
        input = """procedure foo(k : array[1 .. 4] of integer);
                            var x : real;
                            begin
                                phu(2); 
                                //skipasdksadsad;sadkledf;

                            end
                    Procedure main();
                    var a:integer;
                    d: array [1 .. 5] of real;
                    begin 
                        
                        
                    end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,212))
    def test_simple_program12(self):
        input = """ procedure foo(k : array[1 .. 4] of integer);
                            var x : real;
                            begin
                                phu(2); 
                            end
                    Procedure main();
                    var k:array[1 .. 5] of integer;
                    begin 
                        foo(k);
                    end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,213))
    def test_simple_program13(self):
        input = """ function abc(k:real;asd:integer):integer;
                        var a:integer;
                        begin
                            a:=5;
                            c:=b-5;
                        end
                    Procedure main();
                    var m,n:integer;
                    begin 
                        m := n := 4;
                        abc(m,n);  
                    end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,214))
    def test_simple_program14(self):
        input = """ function abc():array[1 .. 4] of real;
                        var a:integer;
                        begin
                            a:=5;
                        end
                    Procedure main();
                    begin 
                        m := n[2] ;
                    end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,215))
    def test_simple_program15(self):
        input = """ function abc():real;
                        var a:integer;
                        begin
                        end
                    Procedure main();
                    begin 
                        ak := dbc(m,n); 
                        asdsad(213902103);
                    end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,216))
    def test_simple_program16(self):
        input = """ var k : real;
                    Procedure main();
                    begin 
                        ns()[2]:=2;
                    end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,217))
    def test_simple_program17(self):
        input = """ var k : real;
                    Procedure main();
                    begin 
                        if (a>2) then b:=2;
                    end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,218))
    def test_simple_program18(self):
        input = """ var k : real;
                    Procedure main();
                    begin 
                        if (a>2) 
                            then b:=2;
                        else
                            b:=3;
                    end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,219))
    def test_simple_program19(self):
        input = """ var k : real;
                    Procedure main();
                    begin 
                        if (a>22) 
                            then b:=2;
                        else
                            if(m>2) then m:=3;
                    end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,220))
    def test_simple_program20(self):
        input = """ var k : real;
                    Procedure main();
                    begin 
                        if a>b then
                            if a>5 then
                                a:=b;
                        else
                            if a>3 then
                                a:=3*2+vcl;
                            else
                                a:=3/2;
                    end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,221))
    def test_simple_program21(self):
        input = """ var k : real;
                    Procedure main();
                    begin 
                        if a>b then
                            if a>5 then
                                a:=b;
                        else
                            if a>3 then
                                a:=3*2+vcl;
                                if(a>4) then
                                    s:=s+1;
                                else
                                    s:=s+2;
                    end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,222))
    def test_simple_program22(self):
        input = """ var k : real;
                    Procedure main();
                    begin 
                        while(true) do
                            a:=a+1;
                    end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,223))
    def test_simple_program23(self):
        input = """ var k : real;
                    Procedure main();
                    begin 
                        while(a = true) do
                            if a>3 then
                                a:=3*2+vcl;
                                if(a>4) then
                                    s:=s+1;
                                else
                                    s:=s+2;
                    end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,224))
    def test_simple_program24(self):
        input = """ var k : real;
                    Procedure main();
                    begin 
                        while(a = true) do
                            if a>3 then
                                a:=3*2+vcl;
                                if(a>4) then
                                    s:=s+1;
                                else
                                    while(k<=3) do a:=a+(2 mod 2);
                    end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,225))
    def test_simple_program25(self):
        input = """ function a():real;
                    var a:integer;
                    begin
                        for a := 2 to 100 do s:=s+1;
                    end
                    Procedure main();
                    begin 
                        while(a = true) do
                            if a>3 then
                                a:=3*2+vcl;
                                if(a>4) then
                                    s:=s+1;
                                else
                                    while(k<=3) do a:=a+(2 mod 2);
                    end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,226))
    def test_simple_program26(self):
        input = """ function a():real;
                    var a:integer;
                    begin
                        for a := 2 to 100 do s:=s+1;
                    end
                    Procedure main();
                    begin 
                        while(a = true) do
                            if a>3 then
                                a:=3*2+vcl;
                                if(a>4) then
                                    s:=s+1;
                                else
                                    while(k<=3) do a:=a+(2 mod 2);
                    end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,227))
    def test_simple_program27(self):
        input = """ function a():real;
                    var a:integer;
                    begin
                        for a := 2 to 100 do s:=s+1;
                    end
                    Procedure main();
                    begin 
                        while(a = true) do
                            if a>3 then
                                a:=3*2+vcl;
                                if(a>4) then
                                    s:=s+1;
                                else
                                    while(k<=3) do a:=a+(2 mod 2);
                                    break;
                    end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,228))
    def test_simple_program28(self):
        input = """ function a():real;
                    var a:integer;
                    begin
                        for a := 2 to 100 do s:=s+1;
                        break;
                    end
                    Procedure main();
                    begin 
                        while(a = true) do
                            if a>3 then
                                a:=3*2+vcl;
                                if(a>4) then
                                    s:=s+1;
                                else
                                    while(k<=3) do a:=a+(2 mod 2);
                                    break;
                    end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,229))
    def test_simple_program29(self):
        input = """ function a():real;
                    var a:integer;
                    begin
                        for a := 2 to 100 do s:=s+1;
                        while (true) do break;
                    end
                    Procedure main();
                    begin 
                        while(a = true) do
                            if a>3 then
                                a:=3*2+vcl;
                                if(a>4) then
                                    s:=s+1;
                                else
                                    while(k<=3) do a:=a+(2 mod 2);
                                    break;
                    end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,230))
    def test_simple_program30(self):
        input = """ function a():real;
                    var a:integer;
                    begin
                        for a := 2 to 100 do s[1]:=s[1]+1;
                    end
                    Procedure main();
                    begin 
                        a(2);
                    end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,231))
    def test_simple_program31(self):
        input = """ procedure a(k:real;x:integer);
                    var a:integer;
                    begin
                        for a := 2 to 100 do s[1]:=s[a]+1;
                        a:=a+1;
                    end
                    Procedure main();
                    begin 
                        a(sdsad,asdasd);
                    end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,232))
    def test_simple_program32(self):
        input = """ procedure a(k:real;x:integer);
                    var a:integer;
                    begin
                        while a<=1000 do s:=s+s[i];
                        if (a<3) then k:=555;
                    end
                    Procedure main();
                    begin 
                        a(sdsad,asdasd);
                    end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,233))
    def test_simple_program33(self):
        input = """ procedure a(k:real;x:integer);
                    var a:integer;
                    begin
                        while a<=1000 do s:=s+s[i];
                        if (a<3) then k:=555;
                    end
                    Procedure main();
                    begin 
                        a(sdsad,asdasd);
                    end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,234))
    def test_simple_program34(self):
        input = """ procedure main();
                    begin
                    end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,235))
    def test_simple_program35(self):
        input = """ procedure main();
                    begin
                    with 
                    a:integer;b:real;
                    do begin
                    s:=a;
                    end
                    end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,236))
    def test_simple_program36(self):
        input = """ procedure main();
                    var main: real;
                    begin
                        
                    end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,237))    
    def test_simple_program37(self):
        input = """ Procedure main();
                    begin 
                        with a,b:real;
                        do s := a+b[i];
                    end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,238))
    def test_simple_program38(self):
        input = """ Procedure main();
                    begin 
                        func(3,a+1,m(2));
                    end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,239))
    def test_simple_program39(self):
        input = """ Procedure main();
                    begin 
                        begin
                            s:=s+1;
                            s:=s*2;
                            a:=-6--5+2;
                        end
                    end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,240))
    def test_simple_program40(self):
        input = """ Procedure main();
                    begin 
                        begin
                            s:=s+1;
                            s:=s*2;
                            a:=-6--5+2-3;
                        end
                    end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,241))
    def test_simple_program41(self):
        input = """ function foo(a,b:integer;c:real):array [1 .. 2] of integer;
                    var x,y:real;
                    begin
                        x:=x+1;
                        return 8*2;
                    end
                    Procedure main();
                    begin 
                    end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,242))
    def test_simple_program42(self):
        input = """ function foo(a,b:integer;c:real):array [1 .. 2] of integer;
                    begin
                        x:=x+1;
                        return 8*2;
                    end
                    Procedure main();
                    begin 
                    end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,243))
    def test_simple_program43(self):
        input = """ function foo(a,b:integer;c:real):array [1-2 .. 3+4] of integer;
                    begin
                        x:=x+1;
                        return 8*2;
                    end
                    Procedure main();
                    begin 
                    end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,244))
    def test_simple_program44(self):
        input = """ function foo(a,b:integer;c:real):array [1-2 .. 3+4] of integer;
                    begin
                        x:=x+1; 
                        begin 
                                s:=6 mod 2;
                        end
                    end
                    Procedure main();
                    var a,b,c:real;d:real;k: array[a .. b] of real;
                    begin   
                    end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,245))
    def test_simple_program45(self):
        input = """ procedure main();
                    begin
                            begin
                                    begin
                                            a:=-5<2;
                                    end
                            end
                    end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,246))
    def test_simple_program46(self):
        input = """ procedure main();
                    begin
                    while (a>3) do
                        s:=a+2; 
                        s:=fun(2)*3;
                    end
                    """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,247))
    def test_simple_program47(self):
        input = """ procedure main();
                    begin
                        z:=-true;
                    end
                    """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,248))
    def test_simple_program48(self):
        input = """ procedure main();
                    begin
                        q := m*2 mod q+1;
                        func("abc",q);
                    end
                    """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,249))
    def test_simple_program49(self):
        input = """ procedure main();
                    begin
                        func("abc",m*2 div q+1);
                    end
                    """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,250))
    def test_simple_program50(self):
        input = """ procedure main();
                    begin
                        if (a > 2) 
                            then b:=2;
                        else
                            b:=3; 
                    end
                    """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,251))
    def test_simple_program51(self):
        input = """ procedure main();
                    begin
                        if (a > true) 
                            then b:=2;
                        else
                            b:=3; 
                    end
                    """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,252))
    def test_simple_program52(self):
        input = """ procedure main();
                    begin
                        if (a = 2) 
                            then b:=2;
                        else
                            if (a =true) 
                                then 
                                    if(a=true) then a:=3;
                    end
                    """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,253))
    def test_simple_program53(self):
        input = """ procedure main();
                    begin
                        if (a = 2) 
                            then b:=2;
                        else
                            if (a =true) 
                                then 
                                    if(a=true) then #a:=3;
                    end
                    """
        expect = "#"
        self.assertTrue(TestParser.test(input,expect,254))
    def test_simple_program54(self):
        input = """ procedure main(m:integer);
                    begin
                        if (a = 2) 
                            then b:=2;
                        else
                            if (a =true) 
                                then 
                                    if(a=true) then a:=3;
                    end
                    """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,255))
    def test_simple_program55(self):
        input = """ procedure main(m:integer);
                    begin
                        if (a = 2) 
                            then b:=2; (*end*)
                        else
                            if (a =true) 
                                then 
                                    if(a=true) then a:=3;
                    end
                    """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,256))
    def test_simple_program56(self):
        input = """ procedure main(m:integer);
                    begin
                        m:= a:= c/100/100/100*1000000;
                    end
                    """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,257))
    def test_simple_program57(self):
        input = """ procedure main(m:integer);
                    begin
                        m := func(a,b,c,d,m)[a+b];
                    end
                    """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,258))
    def test_simple_program58(self):
        input = """ procedure main(m:integer);
                    begin
                        m := func(a,b,c,d,m)[a+b]/c/100/100/100*1000000;
                    end
                    """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,259))
    def test_simple_program59(self):
        input = """ procedure main(m:integer);
                    begin
                        m := func(a,b,c,d,m)[a+b]/c/100/100/100*1000000 - a[--1];
                    end
                    """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,260))
    def test_simple_program60(self):
        input = """ procedure main(m:integer);
                    begin
                        m := func(a,b,c,d,m)[a+b]/c/100/100/100*1000000 - a[--1]*func(func(func(--2)));
                    end
                    """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,261))
    def test_simple_program61(self):
        input = """ procedure main(m:integer);
                    begin
                        while n<100000 do
                            begin
                                n:=n+1;
                                break;
                            end
                    end
                    """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,262))
    def test_simple_program62(self):
        input = """ procedure main(m:integer);
                    begin
                        while n<100000 do
                            begin
                                while true do k:=1;
                            end
                    end
                    """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,263))
    def test_simple_program63(self):
        input = """ procedure main(m:integer);
                    begin
                        while n<100000 do
                            begin
                                while true do 
                                    while (m>1) and (k=true) do z := false;
                            end
                    end
                    """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,264))
    def test_simple_program64(self):
        input = """ procedure main(m:integer);
                    begin
                        for i:=fun(a,b,c) downto l
                        do s:=false;
                    end
                    """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,265))
    def test_simple_program65(self):
        input = """ procedure main(m:integer);
                    begin
                        for i:=fun(a,b,c) downto l
                        do s:=false;
                        m:=s--s;   
                    end
                    """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,266))
    def test_simple_program66(self):
        input = """ procedure main(m:integer);
                    begin
                        for i:=fun(a,b,c) to a[func(2)[2]]
                        do s:=false;
                        func(2)[2]:=s--s;   
                    end
                    """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,267))
    def test_simple_program67(self):
        input = """ procedure main(m:integer);
                    begin
                        for i:=fun(a,b,c) to m+a[2]
                        do s:=false;
                        z[s]:=s--s;   
                    end
                    """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,268))
    def test_simple_program68(self):
        input = """ procedure main(m:integer);
                    begin
                        for i:=fun(a,b,c) to m+a[2]
                        do if(m>2) then z:=--m[fun()];
                        q[a[2]]:=s--s;   
                    end
                    """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,269))
    def test_simple_program69(self):
        input = """ procedure main(m:integer);
                    begin
                        for i:=fun(a,b,c) to m+a[2]
                        do if(m>2) then z:=--m[fun()];
                        s[a] := s--s;   
                        for i:=fun(a,b,c) to m+a[2]
                        do if(m>2) then z:=--m[fun()];
                        z:=s--s;   
                    end
                    """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,270))
    def test_simple_program70(self):
        input = """ function func(a,b,c:real):real;
                    begin
                        if(a+b>c) then z:=1;
                        return z;                           
                    end
                    procedure main(m:integer);
                    begin
                        func(a,b,c);
                    end
                    """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,271))
    def test_simple_program71(self):
        input = """ function func(a,b,c:real):real;
                    begin
                        if(a+b>c) then z:=1;
                        else
                                return --z;                           
                    end
                    procedure main(m:integer);
                    begin
                        func(a,b,c);
                    end
                    """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,272))
    def test_simple_program72(self):
        input = """ function func(a,b,c:real):real;
                    begin
                        if(a+b>c) then return c;
                        else
                                return --z;                           
                    end
                    procedure main(m:integer);
                    begin
                        func(a,b,c);
                    end
                    """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,273))
    def test_simple_program73(self):
        input = """ function func(a,b,c:real):real;
                    begin
                        if(a+b>c) then 
                        begin
                                z:=c[q]-c;
                                return c;
                        end
                        else
                                return --z;                           
                    end
                    procedure main(m:integer);
                    begin
                        func(a,b,c);
                    end
                    """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,274))
    def test_simple_program74(self):
        input = """ procedure main(m:integer);
                    begin
                        with a,b,c,d,e,f,g : real; m:array[func(2) .. func(n)] of real;
                        do
                        func(a,b,m);
                    end
                    """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,275))
    def test_simple_program75(self):
        input = """ procedure main(m:integer);
                    begin
                        with a,b,c,d,e,f,g : real; m:array[func(2) .. func(n)] of real;
                        do
                        begin
                                while true do func(a);
                        end
                    end
                    """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,276))
    def test_simple_program76(self):
        input = """ procedure main(m:integer);
                    begin
                        with a,b,c,d,e,f,g : real; m:array[func(2) .. func(n)] of real;
                        do
                        begin
                                s := a and b or c or d or e and h;
                        end
                    end
                    """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,277))
    def test_simple_program77(self):
        input = """ procedure main(m:integer);
                    begin
                        with a,b,c,d,e,f,g : real; m:array[func(2) .. func(n)] of real;
                        do
                        begin
                                s := not (not b);
                        end
                    end
                    """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,278))
    def test_simple_program78(self):
        input = """ procedure main(m:integer);
                    begin
                        with a,b,c,d,e,f,g : real; m:array[func(2) .. func(n)] of real;
                        do
                        begin
                                while k>z do 
                                        if (a>m) then s:=not s;
                                        begin
                                                s:=--a---s;
                                        end
                        end
                    end
                    """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,279))
    def test_simple_program79(self):
        input = """ procedure main(m:integer);
                    begin
                        with a,b,c,d,e,f,g : real; m:array[func(2) .. func(n)] of real;
                        do
                        begin
                                while k>z do 
                                        if (a>m) then s:=not s;
                                        begin
                                                s := not s and not a;
                                        end
                        end
                    end
                    """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,280))
    """test case la """
    def test_simple_program80(self):
        input = """ procedure main(m:integer);
                    begin
                        while (a=3) and (a=10) and (a=100) do a:=m+1;
                    end
                    """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,281))
    def test_simple_program81(self):
        input = """ procedure main(m:integer);
                    begin
                        a := 1 and 0+1 and 1;
                    end
                    """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,282))
    def test_simple_program82(self):
        input = """ procedure main(m:integer);
                    var a : string;
                    begin
                        a := "mlmlml";
                    end
                    """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,283))
    def test_simple_program83(self):
        input = """ procedure main(m:integer);
                    var a : string;
                    begin
                        
                        a := "mlmlml";
                    end
                    procedure main(m:integer);
                    var a : string;
                    begin
                        
                        a := "mlmlml";
                    end
                    """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,284))
    def test_simple_program83(self):
        input = """ procedure main(m:integer);
                    var a : string;
                    begin
                        
                        a := "mlmlml";
                    end
                    function main(m:integer):integer;
                    var a : string;
                    begin
                        
                        a := "mlmlml";
                    end
                    procedure main(m:integer);
                    var a : string;
                    begin
                        
                        a := "mlmlml";
                    end
                    """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,285))
    def test_simple_program85(self):
        input = """ procedure main(m:integer);
                    var lppl : array[1 .. 30249] of string;
                    begin
                        with a,b,c,d,e,f,g : real; m:array[func(2) .. func(n)] of real;
                        do
                        begin
                                s:=-s-(-b);
                        end
                    end
                    """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,286))
    def test_simple_program86(self):
        input = """ procedure main(m:integer);
                    var lppl : array[1 .. 30249] of string;
                    begin
                            if(a>(b*m)) then
                                    if(a>(b*m)) then
                                            if(a>(b*m)) then
                                                    if(a>(b*m)) then z:=not a;
                                                    else a:=1;                            
                    end
                    """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,287))
    def test_simple_program87(self):
        input = """ procedure main(m:integer);
                    var lppl : array[1 .. 30249] of string;
                    begin
                            if(a>(b*m)) then
                                    if(a>(b*m)) then
                                            if(a>(b*m)) then
                                                    if(a>(b*m)) then z:=not a;
                                                    else a:=a+fun("asd"); 
                                                    (*//asd/as/dasld;k*)                           
                    end
                    """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,288))
    def test_simple_program88(self):
        input = """ procedure main(m:integer);
                    var lppl : array[1 .. 30249] of string;
                    begin
                            if(a>(b*m)) then
                                    if(a>(b*m)) then
                                            if(a>(b*m)) then
                                                    if(a>(b*m)) then l:= not a;
                                                    else a := q; 
                                                    (*//asd/as/dasld;k*)                           
                    end
                    function a():real;
                    var a,b,c,d,e,f : boolean;
                    begin
                            
                            a := b>c;
                            b := c<d;
                            d := e>f;
                    end
                    """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,289))
    def test_simple_program89(self):
        input = """ procedure main(m:integer);
                    var lppl : array[1 .. 30249] of string;
                    begin
                            if(a>(b*m)) then
                                    if(a>(b*m)) then
                                            if(a>(b*m)) then
                                                    if(a>(b*m)) then z:=not a;
                                                    else a:=z; 
                                                    (*//asd/as/dasld;k*)                           
                    end
                    function a():real;
                    var a,b,c,d,e,f : boolean;
                    begin
                            
                            a := b>main(c);
                            b := c<main(a);
                            d := e>main((a),(abc));
                    end
                    """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,290))
    def test_simple_program90(self):
        input = """ procedure main(m:integer);
                    var lppl : array[1 .. 30249] of string;
                    begin
                            if(a>(b*m)) then
                                    if(a>(b*m)) then
                                            if(a>(b*m)) then
                                                    if(a>(b*m)) then k := not a;
                                                    else a:=a+1; 
                                                    (*while true do a*)      
                            while s = a do
                                    m:=2;                     
                    end
                    """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,291))
    def test_simple_program91(self):
        input = """ procedure main(m:integer);
                    var lppl : array[1 .. 30249] of string;
                    begin
                            foo(2)[3] := a[foo(2)[3]] + -3;          
                    end
                    """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,292))
    def test_simple_program92(self):
        input = """ procedure main(m:integer);
                    var lppl : array[1 .. 30249] of string;
                    begin
                            foo(2)[3] := a[foo(2)[3]] + -3;          
                    end
                    """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,293))
    def test_simple_program93(self):
        input = """ procedure main(m:integer);
                    var lppl : array[1 .. 30249] of string;
                    begin
                            foo("ds","as")[3] := a[foo(2)[3]] + -3;        
                    end
                    """  
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,294))
    def test_simple_program94(self):
        input = """ procedure main(m:integer);
                    var lppl : array[1 .. 30249] of string;
                    begin
                            foo("ds","as")[3] := a[foo(2)[3]] + -3;        
                    end
                    """  
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,295))
    def test_simple_program95(self):
        input = """ procedure main(m:integer);
                    var lppl : array[1 .. 30249] of string;
                    begin
                        if(k<>k) then a := false;      
                    end
                    """  
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,296))
    def test_simple_program96(self):
        input = """ procedure main(m:integer);
                    var lppl : array[1 .. 30249] of string;
                    begin
                        putIntLn(sum(m,b,k));   
                    end
                    """  
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,297))
    def test_simple_program97(self):
        input = """ procedure main(m:integer);
                    var lppl : array[1 .. 30249] of string;
                    begin
                        while (true)
                        do if(ar[1]>ar[2]) then index:=1;   
                    end
                    """  
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,298))
    def test_simple_program98(self):
        input = """ procedure main(m:integer);
                    var lppl : array[1 .. 30249] of string;
                    begin
                        while (true)
                        do if(ar[1]>ar[2]) then 
                            begin
                            index:=1;   
                            func((not a));
                            end
                    end
                    """  
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,299))
    def test_final_test(self):
        input = """procedure main(); 
                    var a: array[q[1] .. q[10]] of boolean;
                    begin
                        for i:=1 downto -as[func(a,b,d)] do a[2]:=false;
                    end
                    var a: real;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,200))
    
