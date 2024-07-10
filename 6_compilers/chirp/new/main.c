#include <stdio.h>

#define FILE_MODE_ARG_COUNT 2
#define INTERACTIVE_MODE_ARG_COUNT 1

#define ERROR -1

extern int yyparse(void);

extern FILE *yyin;

#ifdef YYDEBUG
    extern int yydebug;
#endif

int main(int argc, char **argv){

    #ifdef YYDEBUG
        yydebug = 1;
    #endif

    if (argc > FILE_MODE_ARG_COUNT)
    {
        printf("ERROR: %s <input_file>. Incorrect input. Number of args must be 1 or 2.\n", argv[0]);
        return ERROR;
    }

    if (argc == INTERACTIVE_MODE_ARG_COUNT)
    {
        printf("Interactive mode ON\nTo execute code press Ctrl+D\n");
        yyin = stdin;
        printf(">>> ");
        return yyparse();
    }

    yyin = fopen(argv[1], "r");
    
    if (!yyin)
    {
        printf("ERROR: cannot open file %s\n", argv[1]);
        return ERROR;
    }

    printf(">>> ");
    return yyparse();
}