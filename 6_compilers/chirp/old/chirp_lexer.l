%{
#include "ast.h"
#include <stdio.h>
#include "chirp_parser.tab.h"
%}

%option noyywrap

%x COMMENT

%%

[-+]?[0-9]+ { yylval.intVal = atoi(yytext); return INTEGER; }


"есл" {return IF;}
"иес" {return ELIF;}
"ина" {return ELSE;}

"пок" {return WHILE;}

"цик" {return FOR;}

"и" {return AND;}
"или" {return OR;}
"не" {return NOT;}

">" { yylval.op = AST_GT; return CMP; }
"<" { yylval.op = AST_LT; return CMP; }
"!=" { yylval.op = AST_NEQ; return CMP; }
"==" { yylval.op = AST_EQ; return CMP; }
">=" { yylval.op = AST_GTE; return CMP; }
"<=" { yylval.op = AST_LTE; return CMP; }

"+" |
"-" |
"*" |
"/" |
"=" |
"," |
";" |
"(" |
")" |
"[" |
"]" { return yytext[0]; }

"фолс" {yylval.intVal = 0; return INTEGER;};
"тру" {yylval.intVal = 1; return INTEGER;};


"/*"                { BEGIN(COMMENT); }
<COMMENT>"*/"       { BEGIN(INITIAL); }
<COMMENT>.          { }
<COMMENT>\n         { }
<COMMENT><<EOF>>    { yyerror("Unterminated comment!"); }

"//".*              /* single line comment */

[a-zA-Z][a-zA-Z0-9] { yylval.name = strdup(yytext); return NAME; }

[ \t]+                  { /* ignore whitespace */ }
\\\n                    {printf("c> "); }  /* ignore line continuation */
\n                      {  }

.                       { printf("Unexpected character found: %c\n", yytext[0]); }

%%