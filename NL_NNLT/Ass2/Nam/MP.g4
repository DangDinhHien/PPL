/* 1612131 Tran Hoai Nam */
grammar MP;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}


program  :(variable_decalation|function_declaration|procedure_declaration)+ EOF;

/*---------------------Variable declaration------------------------*/

variable_decalation: VAR (list_of_declaration SEMI)+ ;


list_of_declaration:	list_of_id COLON type_data ;

type_data:	primitive_type
		|compound_type;
primitive_type:	INTTYPE
				|REALTYPE
				|STRINGTYPE
				|BOOLTYPE;	


compound_type:	ARRAYTYPE LSB SUB_OP? INTLIT  D_DOT  SUB_OP? INTLIT RSB OF primitive_type;

list_of_id: ID (COMMA ID)* ;

/*---------------------function and procedure declaration------------------------*/


function_declaration: FUCNTION ID LB (list_of_declaration (SEMI list_of_declaration)*)? RB COLON type_data SEMI variable_decalation? compound_stat;


procedure_declaration: PROCEDURE ID LB (list_of_declaration (SEMI list_of_declaration)*)? RB SEMI  (variable_decalation)? compound_stat;



/*--------------------------------Statment------------------------------------*/



stat: 			match_stat
				|unmatch_stat
				;

match_stat:		IF exp THEN match_stat ELSE match_stat
				|other_stat
				;

other_stat:		assign_stat
				|for_stat
				|while_stat
				|break_stat
				|continue_stat
				|return_stat
				|call_stat
				|with_stat
				|compound_stat
				;

unmatch_stat:	IF exp THEN	stat
				|IF exp THEN match_stat
						ELSE unmatch_stat
				;

assign_stat:	(ID|index_exp) (ASSIGN (ID|index_exp))* ASSIGN exp SEMI
				;



while_stat:		WHILE exp DO stat;	// tuy thuoc vao dac ta co compound_stat? 

for_stat:		FOR ID ASSIGN exp (TO|DOWNTO) exp DO stat;

break_stat:		BREAK SEMI;

continue_stat:	CONTINUE SEMI;

return_stat:	RETURN exp? SEMI; // co the tach thanh 2 loai return neu can thiet

with_stat:		WITH (list_of_declaration SEMI)+ DO stat;

	



call_stat:	ID LB list_of_exp? RB SEMI;


// khong dinh nghia dau SEMI vi no duoc dung trong index_exp
// co the la function_call hoac procedure_call

//compound_stat: BEGIN (stat)? END;
compound_stat: BEGIN (stat)* END;

//statments: (stat)+;	////////////// co can segmi ko

/*--------------------------------Expression------------------------------------*/


exp:			exp AND THEN exp1
				|exp OR ELSE exp1
				|exp1
				;


exp1:			exp2 EQUAL exp2
				|exp2 NOT_EQ_OP exp2
				|exp2 LES_THAN exp2
				|exp2 GRE_THAN exp2
				|exp2 LOE_THAN exp2
				|exp2 GOE_THAN exp2
				|exp2
				;

exp2:			exp2 ADD_OP exp3
				|exp2 SUB_OP exp3
				|exp2 OR exp3			
				|exp3
				;

exp3:			exp3 MUL_OP exp4
				|exp3 DIV_OP exp4
				|exp3 DIV exp4
				|exp3 MOD exp4
				|exp3 AND exp4
				|exp4
				;

exp4:			SUB_OP exp4
				|NOT exp4
				|exp5
				;


exp5:			exp6 LSB exp RSB
				|exp6;
exp6:			ID
				|literals
				|call_exp // function_call
				|LB exp RB
				;


literals:		INTLIT
				|REALLI
T				|BOOLLIT
				|STRINGLIT	
				;		// thieu string_lit


call_exp:ID LB list_of_exp? RB;

index_exp:	(ID|call_exp) LSB exp RSB;	 // an element of array

list_of_exp:	exp (COMMA exp)*;

BOOLLIT:	TRUE|FALSE;	// phai khai bao truoc khi dinh nghia TRUE FALSE



/*-----------------------   Function Call -------------------------*/

	

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



//__________________DATA_TYPE___________________
INTTYPE: 	I N T E G E R ;
REALTYPE:	R E A L ;
BOOLTYPE:	B O O L E A N ;
STRINGTYPE:	S T R I N G ;
ARRAYTYPE:	A R R A Y;


//_______________________________________________
//____________________LEXER______________________
//_______________________________________________



//____________________KEYWORD____________________

VAR:		V A R;
BEGIN:		B E G I N;
END:		E N D;

BREAK: 		B R E A K;
CONTINUE:	C O N T I N U E;
FOR:		F O R;
TO:			T O;
DOWNTO:		D O W N T O;
DO:			D O;
IF:			I F;
THEN:		T H E N;
ELSE:		E L S E;
RETURN:		R E T U R N;
WHILE:		W H I L E;
FUCNTION:	F U N C T I O N;
PROCEDURE:	P R O C E D U R E;
WITH:		W I T H;

TRUE:		T R U E;
FALSE:		F A L S E;
OF:			O F;

//____________________OPERATOR__________________

ADD_OP:		'+';
SUB_OP:		'-';
MUL_OP:		'*';
DIV_OP:		'/';

NOT_EQ_OP:	'<>';
EQUAL:		'=';
LES_THAN:	'<';
GRE_THAN:	'>';
LOE_THAN:	'<=';
GOE_THAN:	'>=';

NOT:		N O T;
AND:		A N D;
OR:			O R;
DIV:		D I V;
MOD:		M O D;








//____________________SEPARATOR_________________

LSB:	'[' ;
RSB: 	']' ;
LB: 	'(' ;
RB: 	')' ;
LP: 	'{';
RP: 	'}';
SEMI: 	';' ;
COLON:	':';
D_DOT:	'..';
COMMA:	',';

ASSIGN: ':=';
//____________________COMMENT_AND_WS_________________

BLOCK_COMMENT1		: '{' .*? '}' -> skip;
BLOCK_COMMENT2		: '(*' .*? '*)' -> skip;
LINE_COMMENT		: '//' ~[\r\n]* -> skip ;

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines








INTLIT: 	[0-9]+ ;

EXPONENT_:('e'|'E') SUB_OP? [0-9]+;

REALLIT	: 	[0-9]+ '.'
	|[0-9]+ '.' [0-9]* EXPONENT_?
	|  '.' [0-9]+ EXPONENT_?
	|  [0-9]+ EXPONENT_		
	;


ID:  ('a' .. 'z' | 'A' .. 'Z'|'_') ('a' .. 'z' | 'A' .. 'Z' | '0' .. '9' | '_')*
   ;


STRINGLIT
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