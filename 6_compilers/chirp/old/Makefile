LDFLAGS = -L/opt/homebrew/opt/flex/lib -L/opt/homebrew/opt/bison/lib
CPPFLAGS = -I/opt/homebrew/opt/flex/include

.PHONY: all clean debug graph help
default: all

help:
	@echo MAKEFILE COMMANDS:
	@echo 1. all - build the program (all targets)
	@echo 2. clean - remove the program and temporary files (clean project)
	@echo 3. debug - build the program with debug flags
	@echo 4. graph - generate a graph of the parser
	@echo 5. help - display help for building project

all: clean chirp

chirp: ast.h chirp_parser.tab.c chirp_lexer.c main.c
	gcc -o chirp main.c ast.c chirp_parser.tab.c chirp_lexer.c

chirp_parser.tab.c chirp_parser.tab.h: chirp_parser.y
	bison -d -Wcounterexamples chirp_parser.y

chirp_lexer.c: chirp_lexer.l
	flex -o chirp_lexer.c chirp_lexer.l

graph: chirp_parser.y
	bison -d -Wcounterexamples --graph chirp_parser.y
	dot -Tpng chirp_parser.gv -o chirp_parser.png

clean:
	rm -f chirp chirp_parser.tab.c chirp_parser.tab.h chirp_lexer.c

debug: ast.h chirp_parser.y chirp_lexer.l
	flex -d -o chirp_lexer.c chirp_lexer.l
	bison --debug -d -Wcounterexamples chirp_parser.y
	gcc -o chirp -g -DYYDEBUG=1 main.c ast.c chirp_parser.tab.c chirp_lexer.c