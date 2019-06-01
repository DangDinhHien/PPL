//TRAN QUANG NHAT - 1612402
grammar MP;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

//program : declarationProgram mainProgram declarationProgram EOF;
program : (variableDeclaration|functionDeclaration|procedureDeclaration)+ EOF;
//mainProgram
//	: (PROCEDURE|FUNCTION) identifier LB formalParameterList? RB SEMI? variableDeclaration* BEGIN statements* END 
//	;

identifier
	: IDENT
	;

variableDeclaration 
	: VAR (varList)+
	;

varList
	: IDENT (COMMA IDENT)* COLON types SEMI
	;

functionDeclaration
	: FUNCTION IDENT LB formalParameterList? RB COLON types SEMI variableDeclaration? compoundStatement
	;
	
procedureDeclaration
	: PROCEDURE IDENT LB formalParameterList? RB SEMI variableDeclaration? compoundStatement
	;

formalParameterList 
//	: identifierList COLON types (SEMI identifierList COLON types)*
	: listParam (SEMI listParam)*
	;

listParam	
	: IDENT (COMMA IDENT)* COLON types
	;

formalParameterSection
	: parameterGroup
	;

parameterGroup
	: identifierList COLON types
	;

identifierList
	: IDENT (COMMA IDENT)* 
	;

primitiveTypes
	:( BOOLEAN | INTEGER | STRING | REAL )
	;

compoundTypes
	: ARRAY LSB (SUB? unsignedInteger) DDOT (SUB? unsignedInteger) RSB OF primitiveTypes
	;

types
	: primitiveTypes
	| compoundTypes
	;

statements
	: ifStatement
	| assignment
	| whileStatement
	| forStatement
	| continueandbreak
	| returnStatement
	| compoundStatement
	| withdoStatement
	| callStatement
	;

whileStatement
	: WHILE expression DO statements
	;

forStatement
	: FOR identifier Assign expression (TO|DOWNTO) expression DO statements
	;	

ifStatement
	: IF expression THEN statements (ELSE statements)?
	;

returnStatement
	: RETURN SEMI
	| RETURN expression SEMI
	;

callStatement
	: identifier LB (expression (COMMA expression)*)? RB SEMI
	;

compoundStatement
	: BEGIN (statements)* END
	;

withdoStatement
	: WITH formalParameterList SEMI DO statements
	;

continueandbreak
	: (continueStatement | breakStatement)
	;

continueStatement
	: CONTINUE SEMI
	;

breakStatement
	: BREAK SEMI
	;

assignment
	: (leftHandSides Assign)+ rightHandSides SEMI
	;

rightHandSides
	: expression
	;

expression
	: expression (andthen | orelse) expression1
	| expression1
	;

andthen	
	: AND THEN
	;

orelse	
	: OR ELSE
	;

expression1
	: simpleExpression1 (EQ|NOTEQ|LESS|GREATER|LEQ|GEQ) simpleExpression1
	| simpleExpression1
	;

simpleExpression1
	: simpleExpression1 (PLUS|SUB|OR) simpleExpression2 
	| simpleExpression2 
	;

simpleExpression2
	: simpleExpression2 (DI|MUL|DIV|MOD|AND) prefixExpression 
	| prefixExpression 
	;
	
prefixExpression
	: (SUB|NOT) prefixExpression
	| factor
	;

relationalOperator
	: EQ	
	| NOTEQ
	| LESS
	| GREATER
	| LEQ	
	| GEQ	
	;

additiveoperator
	: PLUS
	| SUB
	| OR
	;

multiplicativeoperator
	: DI	
	| MUL
	| DIV
	| MOD
	| AND
	;

factor
	: identifier
	| literals
	| indexExpression
	| LB expression RB
	| invocationExpression
	| boolean
	;


leftHandSides
	: identifier
	| indexExpression
	;


Assign
	: COLON EQ
	;

scalarVariable
	: identifier 
	;

indexExpression
	: indexArray 
	| indexFunctionArray
	;

indexArray
	: identifier LSB index RSB
	;

index
	: unsignedInteger
	| indexExpression
	| expression
	;

indexFunctionArray
	: functionCall LSB index RSB
	;

invocationExpression
	: identifier LB (expression (COMMA expression)*)? RB
	;

functionCall
	: identifier LB (expression (COMMA expression)*)? RB 
	;

actualParameter
	: expression
	;

literals
	: unsignedInteger
	| unsignedReal
	| string
	;

unsignedInteger
	: NUM_INT
	;

unsignedReal
	: NUM_REAL
	;

sign
	: PLUS
	| SUB
	;

boolean 
	: TRUE
	| FALSE
	;

string
	: STRING_LITERAL
	;

fragment A
   : ('a' | 'A')
   ;


fragment B
   : ('b' | 'B')
   ;


fragment C
   : ('c' | 'C')
   ;


fragment D
   : ('d' | 'D')
   ;


fragment E
   : ('e' | 'E')
   ;


fragment F
   : ('f' | 'F')
   ;


fragment G
   : ('g' | 'G')
   ;


fragment H
   : ('h' | 'H')
   ;


fragment I
   : ('i' | 'I')
   ;


fragment J
   : ('j' | 'J')
   ;


fragment K
   : ('k' | 'K')
   ;


fragment L
   : ('l' | 'L')
   ;


fragment M
   : ('m' | 'M')
   ;


fragment N
   : ('n' | 'N')
   ;


fragment O
   : ('o' | 'O')
   ;


fragment P
   : ('p' | 'P')
   ;


fragment Q
   : ('q' | 'Q')
   ;


fragment R
   : ('r' | 'R')
   ;


fragment S
   : ('s' | 'S')
   ;


fragment T
   : ('t' | 'T')
   ;


fragment U
   : ('u' | 'U')
   ;


fragment V
   : ('v' | 'V')
   ;


fragment W
   : ('w' | 'W')
   ;


fragment X
   : ('x' | 'X')
   ;


fragment Y
   : ('y' | 'Y')
   ;


fragment Z
   : ('z' | 'Z')
   ;

TO
	: T O
	;

ADD
	: A D D
	;

MOD 	
	: M O D
	;

OR
	: O R
	;

PROCEDURE
	: P R O C E D U R E
	;

FUNCTION
	: F U N C T I O N
	;

OF 
    : O F
	;

INTEGER
	: I N T E G E R
	;

REAL
	: R E A L
	;

AND
	: A N D
	;

THEN
	: T H E N
	;

STRING
	: S T R I N G
	;

BOOLEAN
	: B O O L E A N
	;

VAR
	: V A R
	;

ARRAY
	: A R R A Y
	;

BREAK 
	: B R E A K 
	;

CONTINUE
	: C O N T I N U E 
	;

FOR
	: F O R 
	;

DOWNTO 
	: D O W N T O
	;

DO
	: D O
	;

IF
	: I F
	;

ELSE 
	: E L S E
	;

RETURN
	: R E T U R N
	;

WHILE
	: W H I L E
	;

BEGIN
	: B E G I N
	;

END
	: E N D
	;

TRUE
	: T R U E
	;

FALSE
	: F A L S E 
	;

WITH
	: W I T H
	;
NOT
	: N O T
	;
DIV
	: D I V
	;



PLUS	: '+'	;

SUB		: '-'	;

MUL 	: '*'	;

DI		: '/'	;

/*
LOGNOT	: NOT	;

LOGMOD	: MOD	;

LOGOR	: OR	;

LOGAND	: AND	;
*/

NOTEQ	: '<>'	;

EQ		: '='	;

LESS	: '<'	;

GREATER	: '>'	;

LEQ		: '<='	;

GEQ		: '>='	;

LSB		: '['	;

RSB		: ']'	;

COLON	: ':'	;

LB 		: '('	;

RB 		: ')'	;

SEMI	: ';'	;

DDOT 	: '..'	;

COMMA	: ','	;

LK 		: '{'	;

RK 		: '}'	;

WS
	: [ \r\n\f\t\b] ->skip
	;

Blockcomment1 		
	: '(*' .*? '*)' -> skip
	;

Blockcomment2
	: '{' .*? '}' -> skip
	;

Linecomment
	: '//' ~[\n\r]* -> skip
	;

Whitespace
	: [ ]+ -> skip
	;

IDENT
	: ('a' .. 'z' | 'A' .. 'Z'|'_') ('a' .. 'z' | 'A' .. 'Z' | '0' .. '9' | '_')*
	;

STRING_LITERAL
	: '"' (~["\\\r\n] | EscapeSequence)* '"'
	{
		s=self.text[1:-1]
		self.text = s	
	}
	;

fragment EscapeSequence
	: '\\' [bfrnt"'\\]
	;

NUM_INT
	: ('0' .. '9') +
	;

NUM_REAL
    : ('0' .. '9') + (('.' ('0' .. '9') + (EXPONENT)?)? | EXPONENT)
	| ('0' .. '9') '.' ('0' .. '9')?
	| '.' ('0' .. '9') EXPONENT?
    ;

fragment EXPONENT
   : ('e'|'E') ('+' | '-')? ('0' .. '9') +
   ;

ERROR_TOKEN
	: . 
	{
		raise ErrorToken(self.text)
	}
	;

UNCLOSE_STR
	: '"' ('\\'[bfrnt'"\\]|~[\r\n\\"])*
	{
		raise UncloseString(self.text[1:])
	}
	;
	//Khong co \r\n\ va " sau cung, 

ILLEGAL_ESP
	: '"' (('\\'[bfrnt\\'"]|~[\n\r\\"]))* ('\\'(~[bfrnt'\\"]))
	{
		raise IllegalEscape(self.text[1:])
	}
	;

/*
//Lexer rule matches all two-symbol sequences start with a backslash and all sequences that do not contain backslashes
ILLEGAL_ESCAPE
//	: '"' ('\\' ~[btnfr"'\\] | ~'\\')* '"'
	: '"' ('\\' [btnfr"])*
	{
		raise IllegalEscape(self.text)
	}
	;

UNCLOSED_STRING
//	: '"' ('\\'[bfrnt'\\])*
	: '"' ( '\\' [btnfr"'\\] | ~[\b\t\f\r\n\\"] )* 
	{
		raise UncloseString(self.text)
	}
	;

ERROR_TOKEN
	: . 
	{
		raise ErrorToken(self.text)
	}
	;
*/
