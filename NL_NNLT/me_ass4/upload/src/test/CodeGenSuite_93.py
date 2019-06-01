import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    
    def test93(self):
        """Simple program: int main() {} """
        input = """
        function f():integer;
        begin
            return 4;
        end
        procedure main(); 
        var i:integer;
        begin 
            for i:=0 downto -f() do
                putInt(i);
        end"""
        expect = "0-1-2-3-4"
        self.assertTrue(TestCodeGen.test(input,expect,593))
    

    
    
