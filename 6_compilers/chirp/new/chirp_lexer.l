%{
#include "ast.h"
#include <stdio.h>
#include "chirp_parser.tab.h"
%}

%option noyywrap

%x COMMENT

%%

[0-9][a-zA-Z][a-zA-Z0-9]* { yyerror("Variable name cannot start with a digit!");}
[0-9]+          { yylval.intVal = atoi(yytext); return INTEGER; }


"+" |
"-" |
"*" |
"/" | 
"=" |  
"," | 
";" | 
"(" | 
")"            { return yytext[0]; }


">"                 { yylval.typeToken = AST_GT; return CMP; }
"<"                 { yylval.typeToken = AST_LT; return CMP; }
"!="                { yylval.typeToken = AST_NEQ; return CMP; }
"=="                { yylval.typeToken = AST_EQ; return CMP; }
">="                { yylval.typeToken = AST_GTE; return CMP; }
"<="                { yylval.typeToken = AST_LTE; return CMP; }


"если"              { return IF;     }
"иначе"             { return ELSE;   }
"пока"              { return WHILE;  }
"для"               { return FOR;    }
"иначе если"        { return ELIF;   }
"начпрог"           { return START;   }
"конпрог"           { return FINISH;   }
"нач"               { return START_STATEMENT;   }
"кон"               { return FINISH_STATEMENT;    }
"чирп"              { return CHIRP;    }

"и"                 { return AND;   }
"или"               { return OR;    }
"не"                { return NOT;   }

"правда"            { yylval.intVal = 1; return INTEGER; }
"ложь"              { yylval.intVal = 0; return INTEGER;  }


"/*"                { BEGIN(COMMENT); }
<COMMENT>"*/"       { BEGIN(INITIAL); }
<COMMENT>.          { }
<COMMENT>\n         { }
<COMMENT><<EOF>>    { yyerror("ERROR: Unterminated comment!"); }

"//".*              

[a-zA-Z][a-zA-Z0-9]*    { yylval.name = strdup(yytext); return NAME; }


[ \t]+                  {  }
\\\n                    {printf("c> "); } 
\n                      {  }

.                       { printf("Unexpected character: %c\n", yytext[0]); }

%%
