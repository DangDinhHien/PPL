
import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program1(self):
        input = """class Rectangle extends Shape {
					
				}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))

    def test_simple_program2(self):
        input = """class Rectangle extends Shape {
					static final int numOfShape = 0;
				}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,202))

    def test_simple_program3(self):
        input = """class Shape {
					static final int numOfShape = 0;
				}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,203))

    def test_simple_program4(self):
        input = """class Shape {
					static final int numOfShape = 0;
					final int immuAttribute = 0;
					length,width: float;
				}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,204))

    def test_simple_program5(self):
        input = """class Shape {
					final int My1stCons = 1 + 5;
					static final int My2ndCons = 2;
				}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,205))

    def test_simple_program6(self):
        input = """class Shape {
					my1stVar: int;
					myArrayVar: int[5];
					static my2ndVar, my3rdVar: Shape;
					static my2ndArray, my3rdArray: Shape[6];
				}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,206))
    
    def test_simple_program7(self):
        input = """class Shape {
        				float getArea(){
						}
					}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,207))

    def test_simple_program8(self):
        input = """class Shape {
        				float getArea(){
        					return this.length*this.width;
						}
					}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,208))

    def test_simple_program9(self):
        input = """class Shape {
        				void static getArea(a, b, c: int){
        					return this.length*this.width;
						}
					}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,209))

    def test_simple_program10(self):
        input = """class Shape {
        				void static getArea(a, b, c: int){
        					return this.length*this.width;
						}
					}
					class abc {
        				my1stVar: int;
						myArrayVar: int[5];
						static my2ndVar, my3rdVar: Shape;
						static my2ndArray, my3rdArray: Shape[6];
					}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,210))

    def test_simple_program11(self):
        input = """class abc {
        				void static getArea(a, b, c: int){
        					return a;
						}
					}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,211))

    def test_simple_program12(self):
        input = """class abc {
        				string getArea(a, b, c: int){
        					return abae[1+2];
						}
					}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,212))

    def test_simple_program13(self):
        input = """class abc {
        				void getArea(a, b, c: string){
        					return b[[4]];
						}
					}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,213))

    def test_simple_program14(self):
        input = """class abc {
        				void static getArea(length,width:float){
        					{
        						this.length := length;
        						this.length := length;
        					}
						}
					}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,214))

    def test_simple_program15(self):
        input = """class abc {
        				void static getArea(length,width:float){
								%%start of declaration part
								r,s:float;
								a,b:int[5];
								%%list of statements
								r := r ;
								s:=r*r*this.myPI;
								a[0]:= 2.0;
						}
					}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,215))

    def test_simple_program16(self):
        input = """class abc {
        				void static getArea(length,width:float){
							this.aPI := 3.14;
							value := x.foo(5);
							l[3] := value * 2;
						}
					}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,216))

    def test_simple_program17(self):
        input = """class abc {
        				void static getArea(length,width:float){
							if a > 1 then
								io.write("Suy nua thi");
							else
								io.write("Anh sai roi");
						}
					}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,217))

    def test_simple_program18(self):
        input = """class abc {
        				void static getArea(length,width:float){
							if a == 1 then
								io.write("Suy nua thi");
								if b < 0 then
									b := c + 3;
								else
									b[1] := a;
						}
					}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,218))

    def test_simple_program19(self):
        input = """class abc {
        				void static getArea(length,width:float){
							if a <= b + c then
								value := x.foo(5);
								l[3] := value * 2;
								io.write("Suy nua thi");
								if b < 0 then
									b := c + 3;
								else
									b[1] := a;
						}
					}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,219))

    def test_simple_program20(self):
        input = """class abc {
        				void static getArea(length,width:float){
							if a[3] == 1 then
								io.write("Suy nua thi");
								if b < 0 then
									b := c + 3;
								else
									b[1] := a;
									io.write("Phia sau mot co gai");
						}
					}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,220))

    def test_simple_program21(self):
        input = """class abc {
        				void static getArea(length,width:float){
							for x := 5 downto 2 do
								io.writeIntLn(x);
						}
					}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,221))

    def test_simple_program22(self):
        input = """class abc {
        				void static getArea(length,width:float){
							for x := 5 downto 2 do
								io.writeIntLn(x);
							for i := 1 to 100 do {
								io.writeIntLn(i);
								Intarray[i] := i + 1;
							}
						}
					}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,222))

    def test_simple_program23(self):
        input = """class abc {
        				void static getArea(length,width:float){
							for x := 5 downto 2 do
								io.writeIntLn(x);
								break;
							for i := 1 to 100 do {
								break;
								io.writeIntLn(i);
								Intarray[i] := i + 1;
							}
						}
					}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,223))

    def test_simple_program24(self):
        input = """class abc {
        				void static getArea(length,width:float){
							for x := 5 downto 2 do
								io.writeIntLn(x);
								if x == 3 then
									break;
							for i := 1 to 100 do {
								io.writeIntLn(i);
								Intarray[i] := i + 1;
							}
						}
					}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,224))

    def test_simple_program25(self):
        input = """class abc {
        				void static getArea(length,width:float){
							for x := 5 downto 2 do
								io.writeIntLn(x);
							for i := 1 to 100 do {
								io.writeIntLn(i);
								Intarray[i] := i + 1;
								if (a*3 < 10) then
									continue;
							}
						}
					}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,225))

    def test_simple_program26(self):
        input = """class abc {
        				string static getArea(length,width:float){
							for x := 5 downto 2 do
								io.writeIntLn(x);
							for i := 1 to 100 do {
								io.writeIntLn(i);
								Intarray[i] := i + 1;
							}

							return this.a;
						}
					}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,226))

    def test_simple_program27(self):
        input = """class abc {
        				int static getArea(length,width:float){
							for x := 5 downto 2 do
								io.writeIntLn(x);
							for i := 1 to 100 do {
								if a < 1 then
									continue;
								else
									break;
								io.writeIntLn(i);
								Intarray[i] := i + 1;
							}

							return 0;
						}
					}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,227))

    def test_simple_program28(self):
        input = """class abc {
        				void static getArea(){
							for x := 5 downto 2 do
								Sha.getString();
								io.writeIntLn(x);
							for i := 1 to 100 do {
								io.writeIntLn(i);
								Intarray[i] := i + 1;
							}
						}
					}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,228))

    def test_simple_program29(self):
        input = """class abc {
        				int static getArea(length,width:float){
							for x := 5 downto 2 do
								io.writeIntLn(x);
							for i := 1 to 100 do {
								io.writeIntLn(i);
								Intarray[i] := i + 1;
							}
							return a.getNumber(10);
						}
					}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,229))

    def test_simple_program30(self):
        input = """class abc {
        				void static getArea(length,width:float){
        					b.getMax(a[5]);
							for x := 5 downto 2 do
								io.writeIntLn(x);
							for i := 1 to 100 do {
								io.writeIntLn(i);
								Intarray[i] := i + 1;
							}
						}
					}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,230))

    def test_simple_program31(self):
        input = """class abc {
        				int  Mouse(a,b : int){
        					b.getMax("anhmuonemsongsao");
							return 0;
						}
					}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,231)) 

    def test_simple_program32(self):
        input = """class abc {
        				int  Mouse(a,b : int){
        					b.getMax("anhmuonemsongsao", a + b / 10);
							return 0;
						}
					}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,232))

    def test_simple_program33(self):
        input = """class abc {
        				int  Mouse(a,b : int){
        					b.getMax("nobody","anhmuonemsongsao");
							return 0;
						}
					}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,233))

    def test_simple_program34(self):
        input = """class abc {
        				int  Mouse(a,b : int){
        					b.getMax("anhmuonemsongsao","kietlac", a%10);
							return 0;
						}
					}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,234))

    def test_simple_program35(self):
        input = """class Rau {
        				int  Mouse(a,b : int){
        					b.getMax(c.giet(), 10);
							return 0;
						}
					}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,235))

    def test_simple_program36(self):
        input = """class abc {
        				int  Mouse(a,b : int){
        					b.getMax(b, -a);
							return 0;
						}
					}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,236))

    def test_simple_program37(self):
        input = """class abc {
        				int  Mouse(a,b : int){
        					b.getMax(c.getT(e, a));
							return 0;
						}
					}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,237))

    def test_simple_program38(self):
        input = """class abc {
        				int  Mouse(a,b : int){
        					b.getMax("e", a*10/b);
							return this.t;
						}
					}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,238))

    def test_simple_program39(self):
        input = """class abc {
        				int  Cat(a,b : int){
        					b.getMax(Cat.e(), "anh");
							return 0;
						}
					}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,239))

    def test_simple_program40(self):
        input = """class abc {
        				int  Mouse(a,b : int){
        					b.getMax(-z, 10);
        					a := -temp;
							return 0;
						}
					}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,240))

    def test_simple_program41(self):
        input = """class abc {
        				int  Mouse(a,b : int){
        					b.getMax(--z, 10);
							return 0;
						}
					}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,241))

    def test_simple_program42(self):
        input = """class abc {
        				int  Dog(a,b : int){
        					b.getMax(Cat.getName(), Mouse.getName());
							return 0;
						}
					}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,242))

    def test_simple_program43(self):
        input = """class abc {
        				int  Mouse(a,b : int){
        					b.getMax(a[i], b[j], c[z]);
							return 0;
						}
					}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,243))

    def test_simple_program44(self):
        input = """class Example1 {
					int factorial(n:int){
						if n == 0 then return 1; 
						else return n * this.factorial(n - 1);
					}
					void main(){
						x:int;
						x := io.readInt();
						io.writeIntLn(this.factorial(x));
					}
				}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,244))

    def test_simple_program45(self):
        input = """class Example1 {
					int factorial(n:int){
						if n == 0 then return 1; 
						else return n * this.factorial(n - 1);
						break;
					}
					void main(){
						x:int;
						x := io.read("Nhap vao");
						x := io.readInt();
						io.writeIntLn(this.factorial(x));
					}
				}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,245))

    def test_simple_program46(self):
        input = """class Example1 {
					int factorial(n:int){
						if n == 0 then return 1; 
						else return n * this.factorial(n - 1) \\ 10 + (1 - 4);
						break;
					}
				}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,246))

    def test_simple_program47(self):
        input = """class Example1 {
					int factorial(n:int){
						if n * 1.6e-1 == 0 then return 1; 
						else return n * this.factorial(n - 1);
						break;
					}
				}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,247))

    def test_simple_program48(self):
        input = """class Rectangle extends Shape {
						float getArea(){
							return this.length*this.width;
						}
				}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,248))

    def test_simple_program49(self):
        input = """class Example2 {
					void main(){
						s:Shape;
						s := new Rectangle(3,4);
						io.writeFloatLn(s.getArea());
						s := new Triangle(3,4);
						io.writeFloatLn(s.getArea());
					}
				}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,249))

    def test_simple_program50(self):
        input = """class Shape {
					length,width:float;
					float getArea() {}
					Shape(length,width:float){
						this.length := length;
						this.width := width;
					}
				}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,250))

    def test_simple_program51(self):
        input = """class abc {
        				string static getArea(length,width:float){
							for x := 5 + a.getT() downto 2 do
								io.writeIntLn(x);
							for i := 1 - b.getN() to 100 do {
								io.writeIntLn(i);
								Intarray[i] := i + 1;
							}

							return this.a;
						}
					}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,251))

    def test_simple_program52(self):
        input = """class abc {
        				string static getArea(length,width:float){
							for x := 5*ee.g(a,b) downto 2 do
								io.writeIntLn(x);
							for i := 1 to 100 do {
								io.writeIntLn(i);
								Intarray[i] := i + 1;
							}

							return this.a;
						}
					}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,252))

    def test_simple_program53(self):
        input = """class abc {
        				int static getArea(length,width:float){
							for x := 5 + b * 2 % 10 downto 2 do
								io.writeIntLn(x);
							for i := 1 to 100 do {
								io.writeIntLn(i);
								Intarray[i] := i + 1;
							}

							return this.a;
						}
					}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,253))

    def test_simple_program54(self):
        input = """class abc {
        				float static getArea(length,width:float){
							for x := 5 downto 2 do
								io.writeIntLn(x);
							for i := 1 - b to 100 do {
								io.writeIntLn(i);
								Intarray[i] := i + 1;
								if a != 1 then
									return t;
							}

							return this.a;
						}
					}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,254))

    def test_simple_program55(self):
        input = """class Example1 {
					int factorial(n:int){
						if n * 1.6e-1 == 0 then return 1; 
						else return n * this.factorial(n - 1);
						break;
					}
				}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,255))

    def test_simple_program56(self):
        input = """class Example1 {
					int factorial(n:int){
						if n * 1.6e-1 == 0 || a / 5 + 4 then return 1; 
						else return n * this.factorial(n - 1);
						break;
					}
				}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,256))

    def test_simple_program57(self):
        input = """class Example1 {
					int factorial(n:int){
						if (n == 0 || k <= 4) && m > 5 then return 1; 
						else return n * this.factorial(n - 1);
						break;
					}
				}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,257))

    def test_simple_program58(self):
        input = """class Example1 {
					int factorial(n:int){
						if n * 1.6e-1 == 0 || a < b + 34 then return 1; 
						else return n * this.factorial(n - 1, "bae");
						break;
					}
				}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,258))

    def test_simple_program59(self):
        input = """class Example1 {
					int factorial(n:int){
						if n * 1.6e-1 == 0 && (a - b == 2) then return 1; 
						else return n * this.factorial(n - 1);
						break;
					}
				}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,259))

    def test_simple_program60(self):
        input = """class Example1 {
					int factorial(n:int){
						if n * 1.6e-1 == 0 then return 1; 
						else return n.get("hahahh") * this.factorial(n - 1);
						break;
					}
				}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,260))

    def test_simple_program61(self):
        input = """class Example1 {
					int factorial(n:int){
						if n * 1.6e-1 == 0 && (!a - !b == 2) then return 1; 
						else return n * this.factorial(n - 1);
						break;
					}
				}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,261))

    def test_simple_program62(self):
        input = """class abc {
        				void static getArea(length,width:float){
        					{
        						this.length := length;
        						this.length := ! length;
        					}
						}
					}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,262))

    def test_simple_program63(self):
        input = """class abc {
        				void static getArea(length,width:float){
        					{
        						this.length := length;
        						this.length := ! length;
        						a := a + [a + 1];
        						return a;
        						
        					}
						}
					}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,263))

    def test_simple_program64(self):
        input = """class abc {
        				void static getArea(length,width:float){
        					{
        						this.length := length;
        						this.length := ! length;
        						a := a + [a + Mouse.get()];
        						return a;
        						
        					}
						}
					}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,264))

    def test_simple_program65(self):
        input = """class abc {
        				void static getArea(length,width:float){
        					{
        						this.length := length;
        						this.length := ! length;
        						a := a + [a + b % 10];
        						return a;
        						
        					}
						}
					}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,265))

    def test_simple_program66(self):
        input = """class abc {
        				void getArea(a, b, c, d:string){
        					{
        						this.length := length;
        						this.length := ! length;
        						a := a + [a + b % 10];
        						if(a == b) then
        							io.write("ABC");
        						return a;
        						
        					}
						}
					}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,266))

    def test_simple_program67(self):
        input = """class abc {
        				void getArea(a, b, c, d:string){
        					{
        						this.length := -length;
        						this.length := !length;
        						a := a + [a + b % 10];
        						if(a == b) then
        							io.write("ABC");
        						return a;
        						
        					}
						}
					}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,267))

    def test_simple_program68(self):
        input = """class abc {
        				void getArea(a, b, c, d:string){
        					{
        						this.length := length;
        						this.length := ! length;
        						a := a + [a + b % 10];
        						if(a == b) then
        							io.write("ABC");
        						else
        							io.read();
        						return a*a*b-5;
        						
        					}
						}
					}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,268))

    def test_simple_program69(self):
        input = """class abc {
        				void getArea(a, b, c, d:string){
        					{
        						this.length := length;
        						this.length := ! length;
        						a := a + [a + b % 10];
        						if(a == b) then
        							io.write("ABC");
        							for a := 1*b.get("length") to 100 do
        								tong := tong + 1;
        						return tong;
        						
        					}
						}
					}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,269))

    def test_simple_program70(self):
        input = """class abc {
        				void getArea(a, b, c, d:string){
        					{
        						this.length := length;
        						this.length := ! length;
        						a := a + [a + b % 10];
        						if(a == b) then
        							io.write("ABC");
        							break;
        						return a;
        						
        					}
						}
					}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,270))

    def test_simple_program71(self):
        input = """class abc {
        				void static getArea(length,width:float){
							if a == 1 then
								io.write("Suy nua thi");
								if b < 0 then
									b := c + 3;
								else
									b[1] := a.get();

								this.valid := a;

							return temp;
						}
					}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,271))

    def test_simple_program72(self):
        input = """class abc {
        				void static getArea(length,width:float){
							if a == 1 then
								io.write("Suy nua thi");
								if b < 0 then
									b := c + 3;
								else
									b[1] := a;
									for x := 5 downto 2 do
									io.writeIntLn(x);
						}
					}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,272))

    def test_simple_program73(self):
        input = """class abc {
        				void static getArea(length,width:float){
							if a == 1 then
								io.write("Suy nua thi");
								if b < 0 then
									b := c + 3;
								else
									b[1] := a;
									for i := 1 to 100 do {
										io.writeIntLn(i);
										Intarray[i] := i + 1;
									}
						}
					}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,273))

    def test_simple_program74(self):
        input = """class abc {
        				string static getArea(length,width:float){
							if a == 1 then
								io.write("Suy nua thi");
								if b < 0 then
								{	b := c + 3;
									this.aPI := 3.14;
									value := x.foo(5, "ertys");
									l[3] := value * 2;
								}
								else
									b[1] := a;

							return "MMMMMM";
						}
					}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,274))

    def test_simple_program75(self):
        input = """class abc {
        				void static getArea(length,width:float){
							if a == 1 then
								io.write("Suy nua thi");
								if b < 0 then
									b := c.get("Mouse") + 3 - c.get("Cat");
								else
									b[1] := a;
						}
					}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,275))

    def test_simple_program76(self):
        input = """class Example2 {
					void main(){
						s:Shape;
						s := new Rectangle("et",4);
						io.writeFloatLn(s.getArea());
						s := new Triangle(3,4);
						io.writeFloatLn(s.getArea());
					}
				}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,276))

    def test_simple_program77(self):
        input = """class Example2 {
					void main(){
						s:Shape;
						s := new Rectangle(3,4, 0);
						io.writeFloatLn(s.getArea());
						this.B := new Triangle(3,4, "TAnv");
						io.writeFloatLn(s.getArea());
					}
				}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,277))

    def test_simple_program78(self):
        input = """class Example2 {
					void main(){
						s:Shape;
						s := new Rectangle(r.getVa(),4);
						io.writeFloatLn(s.getArea());
						s := new Triangle(3,4);
						io.writeFloatLn(s.getArea());
					}
				}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,278))

    def test_simple_program79(self):
        input = """class Example2 {
					void main(){
						s:Shape;
						s := new Rectangle(3,4,Mouse.get("Anh"));
						io.writeFloatLn(s.getArea());
						s := new Triangle(3,4);
						io.writeFloatLn(s.getArea());
					}
				}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,279))

    def test_simple_program80(self):
        input = """class Example2 {
					void main(){
						s:Shape;
						s := new Rectangle(b, e, f);
						io.writeFloatLn(s.getArea());
						s := new Triangle();
						io.writeFloatLn(s.getArea());
					}
				}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,280))

    def test_simple_program81(self):
        input = """class Shape {
        				void static getArea(a, b, c: int){
        					if (a < (b - c)) then
        						return a;
        					return this.length*this.width;
						}
					}
					class abc {
        				my1stVar: int;
						myArrayVar: int[5];
						static my2ndVar, my3rdVar: Shape;
						static my2ndArray, my3rdArray: Shape[6];
					}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,281))

    def test_simple_program82(self):
        input = """class Shape {
        				void static getArea(a, b, c: int){
							my1stVar := 10000;
        					return this.length*this.width;
						}
					}
					class abc {
        				my1stVar: int;
						myArrayVar: int[5];
						static my2ndVar, my3rdVar: Shape;
						static my2ndArray, my3rdArray: Shape[6];
					}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,282))

    def test_simple_program83(self):
        input = """class Shape {
        				void static getArea(a, b, c: int){
        					if(a==1) then 
        						return 0;
        					return this.getArea(a-1, b-2, c-3);
						}
					}
					class abc {
        				my1stVar: int;
						myArrayVar: int[5];
						static my2ndVar, my3rdVar: Shape;
						static my2ndArray, my3rdArray: Shape[6];
					}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,283))

    def test_simple_program84(self):
        input = """class Shape {
        				void static getArea(a, b, c: int){
        					if((a == 1) || (b == 10)) then
        						return this.getArea(a/10, b/10,c);
        					return this.length*this.width;
						}
					}
					class abc {
        				my1stVar: int;
						myArrayVar: int[5];
						static my2ndVar, my3rdVar: Shape;
						static my2ndArray, my3rdArray: Shape[6];
					}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,284))

    def test_simple_program85(self):
        input = """class Shape {
        				void static getArea(a, b, c: int){
        					for i := a + b to c * c do{
        						if(i == 10) then continue;

        						a := a + 10;
        					}
        					return a;
						}
					}
					class abc {
        				my1stVar: int;
						myArrayVar: int[5];
						static my2ndVar, my3rdVar: Shape;
						static my2ndArray, my3rdArray: Shape[6];
					}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,285))

    def test_simple_program86(self):
        input = """class abc {
        				void static getArea(length,width:float){
								%%start of declaration part
								r,s:float;
								a,b:string[5];
								%%list of statements
								r := this.length ;
								s:=r*r*this.myPI;
								a[0]:= 2.0;
						}
					}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,286))

    def test_simple_program87(self):
        input = """class abc {
        				void static getArea(length,width:float){
								%%start of declaration part
								r,s:float;
								a,b:int[5];
								%%list of statements
								r := r ;
								s:=r*r*this.myPI("Ne", a);
								a[0]:= 2.0;
						}
					}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,287))

    def test_simple_program88(self):
        input = """class abc {
        				void static getArea(length,width:float){
								%%start of declaration part
								r,s:float;
								a,b:int[5];
								%%list of statements
								r := r ;
								s:=r*r*this.myPI;
								a[0]:= 2.0;

								return this.length;
						}
					}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,288))

    def test_simple_program89(self):
        input = """class abc {
        				void static getArea(length,width:float){
								%%start of declaration part
								r,s:string;
								a,b:int[5];
								%%list of statements
								r := r ;
								s:=r*r*this.myPI;
								a[0]:= 2.0;
						}
					}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,289))

    def test_simple_program90(self):
        input = """class abc {
        				void static getArea(length,width:float){
								%%start of declaration part
								r,s:float;
								a,b:int[5];
								%%list of statements
								r := r ;
								s:=r*r*this.myPI % 10;
								a[0]:= 2.0;
						}
					}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,290))

    def test_simple_program91(self):
        input = """class abc {
        				float static getArea(a,b,c:string){
							for x := 5 downto 2 do
								Sha.getString();
								io.writeIntLn(x);
							for i := 1 to 100 do {
								io.writeIntLn(i);
								Intarray[i] := i + 1;
								a := 5;
							}

							return 0;
						}
					}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,291))

    def test_simple_program92(self):
        input = """class abc {
        				void static getArea(){
							for x := 5 downto 2 do
								Sha.getString();
								io.writeIntLn(x);
							for i := 1 to 100 do {
								io.writeIntLn(i);
								Intarray[i] := i + 1;
								if (i == 10) then
									a := 3;
									continue;
							}
						}
					}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,292))

    def test_simple_program93(self):
        input = """class abc {
        				void static getArea(){
							for x := 5*a.get("bet") downto 2 do
								Sha.getString();
								io.writeIntLn(x);
							for i := 1 to 100 do {
								io.writeIntLn(i);
								Intarray[i] := i + 1;
							}
						}
					}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,293))

    def test_simple_program94(self):
        input = """class abc {
        				void static getArea(){
							for x := 5 downto 1 - 10/5 do
								Sha.getString();
								io.writeIntLn(x);
								if(x > 1) then
									x := x*2;
							for i := 1 to 100 do {
								io.writeIntLn(i);
								Intarray[i] := i + 1;
							}
						}
					}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,294))

    def test_simple_program95(self):
        input = """class abc {
        				int static getArea(a,b:int){
							for x := 5 downto 2 do
								a := a/10;
								Sha.getString();
								io.writeIntLn(x);
							for i := 1 to 100 do {
								b := b+10;
								io.writeIntLn(i);
								Intarray[i] := i + 1;
							}
							return a+b;
						}
					}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,295))

    def test_simple_program96(self):
        input = """class Shape {
        				float getArea(){
        					a := "b";
						}
					}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,296))

    def test_simple_program97(self):
        input = """class Shape {
        				float getArea(){
        					a := 3 - this.N;
        					return a % 10;
						}
					}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,297))

    def test_simple_program98(self):
        input = """class Shape {
        				float getArea(abc, c: int){
        					if(c == 1 && (abc < 1)) then return 0;
        					tong := tong*abc + 1;
        					return this.getArea(abc/2, c-1);
						}
					}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,298))

    def test_simple_program99(self):
        input = """class Shape {
        				float getArea(){
        					this.Temp := 10;
        					return this.Temp;
						}
					}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,299))

    def test_simple_program100(self):
        input = """class Shape {
        				float getArea(){
        					this.getName := this.B;
        					return 0;
						}
					}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,300))
