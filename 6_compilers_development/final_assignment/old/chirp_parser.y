%{
#include "ast.h"
#include <stdio.h>
#include <stdlib.h>
#include <stdarg.h>
void yyerror(char *name, ...);
int yylex(void);
%}

%union {
    struct ast *nested;
    int intVal;
    char *name;
    ntype_t op;
}

%token <intVal> INTEGER
%token <name> NAME
%token <op> CMP
%token EOL YYEOF
%token IF ELIF ELSE WHILE FOR 
%token AND NOT OR


%right '='
%left AND
%left OR
%left NOT
%left CMP
%left '+' '-'
%left '*' '/'

%type <nested> compound_statement statements statement if_statement else_statement elif_statement for_statement while_statement expression assignment arithmetic_expression logical_expression comparison_expression

%start program
%%

program:							  compound_statement YYEOF {
																					if($1 != NULL) {
																						print_ast(stdout, $1, 0);

																						FILE* file_1 = fopen("chirp_out.S", "w");
																						FILE* file_2 = fopen("chirp_tree", "w");

																						if(file_1 == NULL) {
																							printf("Error opening file\n");
																							exit(1);
																						}

																						if(file_2 == NULL) {
																							printf("Error opening file\n");
																							exit(1);
																						}

																						print_asm(file_1, $1);
																						print_ast(file_2, $1, 0);

																						fclose(file_1);
																						
																						treefree($1);
																					}
																					printf("> ");
																				}
									| error YYEOF									{ yyerrok; printf("> ");}
;

compound_statement:				  /* nothing */             { $$ = NULL; }
								| '{' statements '}'    { $$ = $2; }
;

statements:						  /* nothing */             { $$ = NULL; }
								| statement  statements     {
																if($2 == NULL) $$ = $1;
																else $$ = newast(AST_STATEMENTS, $1, $2);
															}
								| expression ';' statements  {
																if($3 == NULL) $$ = $1;
																else $$ = newast(AST_STATEMENTS, $1, $3);
															}
;

statement:			  			  if_statement
								| for_statement
								| while_statement
;

if_statement:			  		  IF expression compound_statement else_statement 		 { $$ = newflow(AST_IF, $2, $3, $4); }
								| IF expression compound_statement elif_statement 		 { $$ = newflow(AST_IF, $2, $3, $4); }
;

else_statement:					  /* null */ 			  { $$ = NULL; }
								| ELSE compound_statement { $$ = $2; }
;

elif_statement:  				  ELIF expression compound_statement else_statement		  { $$ = newflow(AST_IF, $2, $3, $4); }
								| ELIF expression compound_statement elif_statement	 	  { $$ = newflow(AST_IF, $2, $3, $4);  }
;

for_statement:					  FOR '(' expression ';' expression ';' expression ')' compound_statement 			  { $$ = newfor($3, $5, $7, $9); }
;

while_statement:		  WHILE expression compound_statement  { $$ = newflow(AST_WHILE, $2, $3, NULL);  }
;

expression:  			  NAME { $$ = newref($1);              }
						| INTEGER { $$ = newnum($1);              }
						| assignment
						| '(' expression ')' { $$ = $2;                      }
						| logical_expression
						| arithmetic_expression	
						| comparison_expression
;

assignment: 			  NAME '=' expression { $$ = newasgn($1, $3);         }
;

arithmetic_expression:    expression '+' expression { $$ = newast(AST_ADD, $1, $3);     }
						| expression '-' expression { $$ = newast(AST_SUB, $1, $3);     }
						| expression '*' expression { $$ = newast(AST_MUL, $1, $3);     }
						| expression '/' expression { $$ = newast(AST_DIV, $1, $3);     }
;

logical_expression:		  NOT expression { $$ = newast(AST_NOT, $2, NULL); }
						| expression AND expression { $$ = newast(AST_AND, $1, $3);   }
						| expression OR expression	{ $$ = newast(AST_OR, $1, $3);    }
;
	
comparison_expression: 	  expression CMP expression { $$ = newcmp($2, $1, $3);      }
;