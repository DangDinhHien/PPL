grammar MP;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}


///////////////////////////// Parser ////////////////////////////
program: (var_decl | func_decl | proc_decl)+ EOF;



//////////////// var declare ////////////
var_decl: VAR (list_vardecl SEMI)+ ;

list_vardecl: IDENTIFIER (COMMA IDENTIFIER)* COLON type_a ; // Chú ý kiểu type bị trùng trong .G4

type_a: primitive_type | compound_type ;

primitive_type: STRING | BOOLEAN | INTEGER | REAL ;

compound_type: ARRAY LSB SUB? INT_LIT DD SUB? INT_LIT RSB OF primitive_type ;

////////////// function declare ///////////
func_decl: FUNCTION IDENTIFIER LB listpara? RB COLON type_a SEMI var_decl? comp_statement? ;

listpara: list_vardecl (SEMI list_vardecl)* ;

////////////// procedure declare ///////////
proc_decl: PROCEDURE IDENTIFIER LB listpara? RB SEMI var_decl? comp_statement? ;

///////////// statement ////////////


statement:	match_statement | unmatch_statement ;

///////////// match_statement ///////////
match_statement: 
	IF expression THEN match_statement ELSE match_statement 
	| other ;

other:
	assignment_state
	| while_state
	| for_state
	| break_state
	| continue_state
	| return_state
	| comp_statement // Them vao
	| with_state
	| call_state SEMI // CHú ý thêm semi vô nếu call mà là state thì thêm còn là index thì ko có.
	;

assignment_state:
	// (IDENTIFIER|index_expression) (ASSIGN (IDENTIFIER|index_expression))* ASSIGN expression SEMI
	(lhs ASSIGN)+ expression SEMI
	;


while_state:
	WHILE expression DO statement
	;

for_state:
	FOR IDENTIFIER ASSIGN expression (TO|DOWNTO) expression DO statement
	;

break_state: BREAK SEMI;

continue_state: CONTINUE SEMI;

return_state: RETURN expression? SEMI;

with_state: WITH listpara SEMI DO statement ;

call_state: IDENTIFIER LB list_expression? RB ; // Cân nhắc SEMI



//////////// unmatch_statement /////////
unmatch_statement: 
	IF expression THEN statement
	| IF expression THEN match_statement ELSE unmatch_statement
	;

comp_statement: BEGIN (statement)* END ; // Bỏ SEMI vì nếu statement = compound thì false

/////////////// expression ///////////
expression: 
	expression AND THEN expression1
	| expression OR ELSE expression1
	| expression1
	;

expression1:
	expression2 EQ expression2
	| expression2 NOTEQ expression2
	| expression2 LESS expression2
	| expression2 GREATER expression2
	| expression2 LEQ expression2
	| expression2 GEQ expression2
	| expression2
	;

expression2:
	expression2 ADD expression3
	| expression2 SUB expression3
	| expression2 OR expression3
	| expression3
	;

expression3:
	expression3 DIVISION expression4
	| expression3 MUL expression4
	| expression3 DIV expression4
	| expression3 MOD expression4
	| expression3 AND expression4
	| expression4
	;

expression4:
	SUB expression4
	| NOT expression4
	| expression5
	;

expression5:
	expression6 LSB expression RSB
	| expression6
	;

expression6:
	IDENTIFIER
	| literal
	| call_state
	| LB expression RB
	;

literal:
	INT_LIT | BOOL_LIT | REAL_LIT | STRING_LIT
	;

index_expression: 
	(IDENTIFIER|call_state) LSB expression RSB // nếu 2 cái exp thì sẽ bị error đệ quy trái.
	;

list_expression: expression (COMMA expression)* ;


lhs: (IDENTIFIER|index_expression) ;


fragment A : ('a' | 'A') ;
fragment B : ('b' | 'B') ;
fragment C : ('c' | 'C') ;
fragment D : ('d' | 'D') ;
fragment E : ('e' | 'E') ;
fragment F : ('f' | 'F') ;
fragment G : ('g' | 'G') ;
fragment H : ('h' | 'H') ;
fragment I : ('i' | 'I') ;
fragment J : ('j' | 'J') ;
fragment K : ('k' | 'K') ;
fragment L : ('l' | 'L') ;
fragment M : ('m' | 'M') ;
fragment N : ('n' | 'N') ;
fragment O : ('o' | 'O') ;
fragment P : ('p' | 'P') ;
fragment Q : ('q' | 'Q') ;
fragment R : ('r' | 'R') ;
fragment S : ('s' | 'S') ;
fragment T : ('t' | 'T') ;
fragment U : ('u' | 'U') ;
fragment V : ('v' | 'V') ;
fragment W : ('w' | 'W') ;
fragment X : ('x' | 'X') ;
fragment Y : ('y' | 'Y') ;
fragment Z : ('z' | 'Z') ;


BOOL_LIT: TRUE | FALSE ;

///////////////////////////// Lexer /////////////////////////////////////////////////////////////

// Chu y bo skip len tren dau lexer
// comment
COMMENT1
	: '(*' .*? '*)' -> skip
	;

COMMENT2
	: '{' .*? '}' -> skip
	;

COMMENT3
	: '//' ~[\n\r]* -> skip
	;


// World Space

WS: [ \n\r\t]+ -> skip ; // Phai bo cai nay len tren


// Keywords.
BREAK
	: B R E A K
	;

CONTINUE
	: C O N T I N U E
	;

FOR
	: F O R
	;

TO
	: T O
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

THEN
	: T H E N
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

FUNCTION
	: F U N C T I O N
	;

PROCEDURE
	: P R O C E D U R E
	;

VAR
	: V A R
	;

TRUE
	: T R U E
	;

FALSE
	: F A L S E
	;

ARRAY
	: A R R A Y
	;

OF
	: O F
	;

REAL
	: R E A L
	;

BOOLEAN
	: B O O L E A N
	;

INTEGER
	: I N T E G E R
	;

STRING
	: S T R I N G
	;

NOT
	: N O T
	;

AND
	: A N D
	;

OR
	: O R
	;

DIV
	: D I V
	;

MOD
	: M O D
	;

WITH
	: W I T H
	;

// Operator

ADD: '+' ;

SUB: '-' ;

MUL: '*' ;

DIVISION: '/' ;

// NOT da co o tren.
// mod da co o tren.
// OR, AND da co o tren.
// DIV cung co o tren.

NOTEQ: '<>' ;

EQ: '=' ;

LESS: '<' ;

GREATER: '>' ;

LEQ: '<=' ;

GEQ: '>=' ;

// Separators

LSB: '[' ;
RSB: ']' ;
COLON: ':' ;
LB: '(' ;
RB: ')' ;
SEMI: ';' ;
DD: '..' ;
COMMA: ',' ;
LK: '{' ;
RK: '}' ;

ASSIGN: ':=' ;

// Lưu ý bỏ thứ tự ID bỏ lên trước là sai
// Identifier: khong phan biet hoa thuong, bat dau bang chu hoac '_'
IDENTIFIER
	// : [a-zA-Z_] [a-zA-Z_0-9]*
	: ('a' .. 'z' | 'A' .. 'Z'|'_') ('a' .. 'z' | 'A' .. 'Z' | '0' .. '9' | '_')*
	;

// Literals

INT_LIT: [0-9]+ ;

// xem xet truong hop 1e.11 va 1.e11
REAL_LIT
	: [0-9]+ EXP ('.')? [0-9]* 
	| [0-9]+ ('.')? EXP 
	| [0-9]* ('.')? [0-9]+ EXP
	| [0-9]* ('.')? [0-9]+
	| [0-9]+ ('.')? [0-9]* 
	;

fragment EXP
	: [eE] ('-')? [0-9]+ 
	;



STRING_LIT
    :'"' (EscapeSequence | ~["\\\r\nEOF] )* '"'
        {
            s=self.text[1:-1]   
            self.text=s
        }
    ;
fragment EscapeSequence
    : '\\' [btnfr"'\\]
    ;


ERROR_CHAR: .
	{
		raise ErrorToken(self.text)
	};

UNCLOSE_STRING
    :  '"' ( ~[\\\r\n"EOF]|EscapeSequence )* ('\n'| EOF)
        {
            if self.text[-1]=='\n':
                 raise UncloseString(self.text[1:-1])
            else:
                raise UncloseString(self.text[1:])
        }
    ;
ILLEGAL_ESCAPE
    : '"' (EscapeSequence | ~["\\])*? ([\\] ~[bfrnt'"\\])
        {
           raise IllegalEscape(self.text[1:]) 
        }
        
    ;


