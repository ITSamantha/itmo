%{
#include "ast.h"
#include <stdio.h>
#include <stdlib.h>
#include <stdarg.h>
void yyerror(char *s, ...);
int yylex(void);
%}

%union {
    struct ast *nested;
    int intVal;
    char *name;
    ntype_t typeToken;
}



%token <intVal> INTEGER
%token <name> NAME
%token EOL YYEOF
%token IF ELSE WHILE FOR ELIF
%token START FINISH START_STATEMENT FINISH_STATEMENT CHIRP

%right '='

%left OR
%left AND
%left NOT

%left <typeToken> CMP

%left '+' '-'
%left '*' '/'

%type <nested> expression statements statement if_statement elif_statement else_statement for_statement while_statement logical_operations aritmetic_operations comparison_operations

%start chirp
%%

chirp: CHIRP START statements FINISH YYEOF   {
                                            if($3 != NULL) {
                                                print_ast(stdout, $3, 0);

                                                FILE* file1 = fopen("chirp_out.S", "w");
                                                FILE* file2 = fopen("chirp_tree", "w");

                                                if(file1 == NULL) {
                                                    printf("ERROR: Can not open file!\n");
                                                    exit(1);
                                                }

                                                if(file2 == NULL) {
                                                    printf("ERROR: Can not open file!\n");
                                                    exit(1);
                                                }

                                                print_asm(file1, $3);
                                                print_ast(file2, $3, 0);

                                                fclose(file1);

                                                treefree($3);
                                            }
                                            printf(">>> ");
                                        }
    | error YYEOF                    { yyerrok; printf(">>> ");}
    ;


statement:    if_statement
            | while_statement
            | for_statement
            ;


for_statement : FOR '(' expression ';' expression ';' expression ')' START_STATEMENT statements FINISH_STATEMENT { $$ = newfor($3, $5, $7, $10); }
;

while_statement: WHILE expression START_STATEMENT statements FINISH_STATEMENT                        { $$ = newstatement(AST_WHILE, $2, $4, NULL);  }
;


if_statement: IF expression START_STATEMENT statements FINISH_STATEMENT else_statement              { $$ = newstatement(AST_IF, $2, $4, $6); }
    | IF expression START_STATEMENT statements FINISH_STATEMENT elif_statement                      { $$ = newstatement(AST_IF, $2, $4, $6); }
    ;


elif_statement: ELIF expression START_STATEMENT statements FINISH_STATEMENT else_statement          { $$ = newstatement(AST_IF, $2, $4, $6); }
    | ELIF expression START_STATEMENT statements FINISH_STATEMENT elif_statement                    { $$ = newstatement(AST_IF, $2, $4, $6); }
    ;


else_statement:                                           { $$ = NULL; }
    | ELSE START_STATEMENT statements FINISH_STATEMENT                             { $$ = $3; }
    ;


statements:                                          { $$ = NULL; }
            | expression ';' statements                      {
                                                    if($3 == NULL) $$ = $1;
                                                    else $$ = newast(AST_STATEMENTS, $1, $3);
                                                }
            | statement statements                         {
                                                    if($2 == NULL) $$ = $1;
                                                    else $$ = newast(AST_STATEMENTS, $1, $2);
                                                }
    ;


expression:   comparison_operations                       
            | aritmetic_operations
            | logical_operations
            | '(' expression ')'                       { $$ = $2;                      }
            | INTEGER                            { $$ = newnum($1);              }
            | NAME                              { $$ = newref($1);              }
            | NAME '=' expression                      { $$ = newasgn($1, $3);         }
            ;



logical_operations:   expression AND expression                       { $$ = newast(AST_AND, $1, $3);   }
                    | expression OR expression                        { $$ = newast(AST_OR, $1, $3);    }
                    | NOT expression                                  { $$ = newast(AST_NOT, $2, NULL); }
;

aritmetic_operations:     expression '+' expression                       { $$ = newast(AST_ADD, $1, $3);     }
                        | expression '-' expression                       { $$ = newast(AST_SUB, $1, $3);     }
                        | expression '*' expression                       { $$ = newast(AST_MUL, $1, $3);     }
                        | expression '/' expression                       { $$ = newast(AST_DIV, $1, $3);     }
;

comparison_operations: expression CMP expression                       { $$ = newcmp($2, $1, $3);      }  
;

%%