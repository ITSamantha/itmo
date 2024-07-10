#include <stdio.h>

extern int yyparse(void);

extern FILE *yyin;

#ifdef YYDEBUG
    extern int yydebug;
#endif

#define ERROR -1
#define INCORRECT_ARG_COUNT 2
#define FILE_ARG_COUNT 1

int main(int argc, char **argv)
{
    #ifdef YYDEBUG
        yydebug = 1;
    #endif

    if (argc > INCORRECT_ARG_COUNT)
    {
        printf("Input data error. Too many arguments.");
        return ERROR;
    }

    if (argc == FILE_ARG_COUNT)
    {
        printf("Interactive mode\nTo execute press Ctrl+D\n");
        yyin = stdin;
        printf("> ");
        return yyparse();
    }

    yyin = fopen(argv[1], "r");

    if (!yyin)
    {
        printf("Error: cannot open file %s\n", argv[1]);
        return ERROR;
    }

    printf("> ");
    
    return yyparse();
}