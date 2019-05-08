// 1611089

grammar BKOOL;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}


////////////////// Parser ////////////////////
program: class_decl+ EOF ;

class_decl: CLASS ID (EXTENDS ID)? LP list_of_members? RP ;

list_of_members: (attribute | method)+ ;

attribute: variable_decl | constant_decl ;

constant_decl: STATIC? FINAL type_lit ID OP_BANG exp SEMICOLONE;

variable_decl: STATIC? id_list COLON type_lit SEMICOLONE ;

id_list: ID (COMMA ID)* ;

method: (type_lit | VOID)? STATIC? ID LB list_of_para? RB block_state ;

list_of_para: para (SEMICOLONE para)* ;

para: id_list COLON type_lit;

///////////// TYPE //////////
type_lit: primitive_type | array_type | class_type ;

primitive_type: INT | FLOAT | BOOLEAN | STRING ;

array_type: (ID | primitive_type) LSB (INTEGERLIT | ID) RSB ;

class_type: ID | NIL; 


//////////////////// EXPRESSTION ///////////////////
exp:
	exp1 LESS exp1
	| exp1 GREATER exp1
	| exp1 LESSEQ exp1
	| exp1 GREATEREQ exp1
	| exp1
	;

exp1:
	exp2 EQ exp2
	| exp2 NOTEQ exp2
	| exp2
	;

exp2:
	exp2 OR exp3
	| exp2 AND exp3
	| exp3
	;

exp3:
	exp3 ADD exp4
	| exp3 SUB exp4
	| exp4
	;

exp4:
	exp4 MUL exp5
	| exp4 INTDIV exp5
	| exp4 FLOATDIV exp5
	| exp4 MOD exp5
	| exp5
	;

exp5:
	exp5 CONCAT exp6
	| exp6
	;

exp6:
	NOT exp6
	| exp7
	;

exp7:
	ADD exp7
	| SUB exp7
	| exp8
	;

exp8:
	LSB exp RSB
	| exp9
	;

exp9:
	exp9 DOT exp10
	| exp10
	;

exp10:
	NEW exp10
	| exp11
	;

exp11:
	ID
	| literals
	| index_exp
	| member_access
	| object_creation
	| THIS
	| LB exp? RB
	;

literals:
	INTEGERLIT
	| FLOATLIT
	| BOOLLIT
	| STRINGLIT
	;


index_exp: (ID | member_access) LSB exp RSB; // array_type

member_access:
	instance_attribute
	| static_attribute
	| instance_method
	| static_method
	;

instance_attribute: (ID | THIS) DOT ID LB list_exp? RB DOT ID ; // Xem xet truong hop this.A().B().C()

static_attribute: (ID | THIS) DOT ID ;

object_creation: NEW ID LB list_exp? RB ;


////////////////////  STATEMENT /////////////////
statement:
	match_state
	| unmatch_state
	;

match_state:
	IF exp THEN match_state ELSE match_state
	| other_state
	;

unmatch_state:
	IF exp THEN statement
	| IF exp THEN match_state ELSE unmatch_state
	;

other_state:
	block_state
	| assign_state
	| for_state
	| break_state
	| continue_state
	| return_state
	| method_invo_state
	;

block_state: LP attribute* statement* RP ;

assign_state: lhs ASSIGN exp SEMICOLONE ;

lhs: local_variable | variable_decl | array_type ; // Chu y array

local_variable: THIS DOT ID | ID; ///////////


for_state: 
	FOR scalar_variable ASSIGN exp (TO|DOWNTO) exp DO statement
	;

scalar_variable: ID ;

break_state: BREAK SEMICOLONE ;

continue_state: CONTINUE SEMICOLONE ;

return_state: RETURN exp SEMICOLONE ;

method_invo_state: (instance_method_state | static_method_state) SEMICOLONE ;

instance_method: (ID | THIS) DOT ID LB list_exp? RB DOT ID LB list_exp? RB; // them DOT ID, Chu y +

static_method: (ID | THIS) DOT ID LB list_exp? RB ; // A.B()


///// Them zo phan biet CallStmt voi CallExpr
instance_method_state: (ID | THIS) DOT ID LB list_exp? RB DOT ID LB list_exp? RB;

static_method_state: (ID | THIS) DOT ID LB list_exp? RB ;

list_exp: exp (COMMA exp)* ;




////////////////////////////


BOOLLIT: TRUE | FALSE ;



///////////////// Lexer //////////////////

//////// KeyWord
BOOLEAN: 'boolean';

BREAK: 'break' ;

CLASS: 'class' ;

CONTINUE: 'continue' ;

DO: 'do' ;

ELSE: 'else' ;

EXTENDS: 'extends' ;

FLOAT: 'float' ;

IF: 'if' ;

INT: 'int' ;

NEW: 'new' ;

STRING: 'string' ;

THEN: 'then' ;

FOR: 'for' ;

RETURN: 'return' ;

TRUE: 'true' ;

FALSE: 'false' ;

VOID: 'void' ;

NIL: 'nil' ;

THIS: 'this' ;

FINAL: 'final' ;

STATIC: 'static' ;

TO: 'to' ;

DOWNTO: 'downto' ;


///////////////  OPERATOR
ADD: '+' ;

SUB: '-' ;

MUL: '*' ;

FLOATDIV: '/' ;

INTDIV: '\\' ;  // Hai dau \\ la thanh 1 \

MOD: '%' ;

NOTEQ: '!=' ;

EQ: '==' ;

LESS: '<' ;

GREATER: '>' ;

LESSEQ: '<=' ;

GREATEREQ: '>=' ;

OR: '||' ;

AND: '&&' ;

NOT: '!' ;

CONCAT: '^' ;

ASSIGN: ':=' ;

OP_BANG: '=' ;

//////////////// SEPARATOR
LSB: '[' ;

RSB: ']' ;

LP: '{' ;

RP: '}' ;

LB: '(' ;

RB: ')' ;

SEMICOLONE: ';' ;

COLON: ':' ;

DOT: '.' ;

COMMA: ',' ;


//////////////// LITERAL
INTEGERLIT: [0-9]+ ;

FLOATLIT: 
	[0-9]+ '.' [0-9]* EXPONENT?
	| [0-9]+ EXPONENT
	;

fragment EXPONENT: [Ee] [+-]? [0-9]+ ;

STRINGLIT
    :'"' (EscapeSequence | ~[\\\r\n"])* '"'
    ;

fragment EscapeSequence
    : '\\' [btnfr"\\]
    ;


WS : [ \t\r\n\f]+ -> skip ;

/////// Comment
BLOCKCOMMENT: '/*' .*? '*/' -> skip ;

LINECOMMENT: '%%' ~[\r\n]* -> skip ;



/////// ID
ID: [_A-Za-z][_A-Za-z0-9]* ;

ERROR_CHAR: .
	{
		raise ErrorToken(self.text)
	};

UNCLOSE_STRING
    :  '"' ( ~[\\\r\n"]|EscapeSequence )* ('\n'| EOF)
        {
            if self.text[-1]=='\n':
                 raise UncloseString(self.text[1:-1])
            else:
                raise UncloseString(self.text[1:])
        }
    ;

ILLEGAL_ESCAPE
    : '"' (EscapeSequence | ~["\\])*? ([\\] ~[bfrnt"\\])
        {
           raise IllegalEscape(self.text[1:-1]) 
        }
    ;