#pragma once

#include <stdio.h>

/* interface to the lexer */
extern int yylineno; /* from lexer */
void yyerror(char *s, ...);

/* symbol table */
struct symbol
{ /* a variable name */
    char *name;
    int offset;
};

/* simple symtab of fixes size */
#define NHASH 9997
struct symbol symtab[NHASH];

struct symbol *lookup(char *);
struct symbol *define_sym(char *);

typedef enum ntype
{
    AST_IF,
    AST_WHILE,
    AST_FOR,

    AST_EQ,
    AST_NEQ,
    AST_LT,
    AST_LTE,
    AST_GT,
    AST_GTE,

    AST_ADD,
    AST_SUB,
    AST_MUL,
    AST_DIV,

    AST_AND,
    AST_OR,
    AST_NOT,

    AST_NUM,
    AST_REF,
    AST_ASGN,
    AST_STATEMENTS
} ntype_t;

static char *node2str[] = {
    [AST_IF] = "IF",        [AST_WHILE] = "WHILE", [AST_FOR] = "FOR", [AST_EQ] = "==",     [AST_NEQ] = "!=",
    [AST_LT] = "<",         [AST_LTE] = "<=",      [AST_GT] = ">",    [AST_GTE] = ">=",    [AST_ADD] = "+",
    [AST_SUB] = "-",        [AST_MUL] = "*",       [AST_DIV] = "/",   [AST_AND] = "AND",   [AST_OR] = "OR",
    [AST_NOT] = "NOT",      [AST_NUM] = "NUM",     [AST_REF] = "REF", [AST_ASGN] = "ASGN", [AST_STATEMENTS] = "STATEMENTS"
};

/* nodes in the abstract syntax tree */
struct ast
{
    ntype_t nodetype;
    struct ast *l;
    struct ast *r;
};

struct numval
{
    ntype_t nodetype; /* type K for constant */
    int number;
};

struct flow
{
    ntype_t nodetype; /* type I or W */
    struct ast *cond; /* condition */
    struct ast *tl;   /* then or do list */
    struct ast *el;   /* optional else list */
};

struct for_loop
{
    ntype_t nodetype;
    struct ast *init;
    struct ast *cond;
    struct ast *inc;
    struct ast *tl;
};

struct symref
{
    ntype_t nodetype; /* type N */
    struct symbol *s;
};

struct symasgn
{
    ntype_t nodetype; /* type = */
    struct symbol *s;
    struct ast *v; /* value */
};

/* build an AST */

struct ast *newast(ntype_t nodetype, struct ast *l, struct ast *r);

struct ast *newcmp(ntype_t cmptype, struct ast *l, struct ast *r);

struct ast *newflow(ntype_t nodetype, struct ast *cond, struct ast *tl, struct ast *el);

struct ast *newfor(struct ast *init, struct ast *cond, struct ast *inc, struct ast *tl);

struct ast *newnum(int d);

struct ast *newref(char *s);

struct ast *newasgn(char *s, struct ast *v);

/* print an AST */

void print_ast(FILE *stream, struct ast *ast, int level);
void print_asm(FILE *stream, struct ast *ast);

/* delete and free an AST */

void treefree(struct ast *);

/* interface to the lexer */

extern int yylineno; /* from lexer */
void yyerror(char *s, ...);
