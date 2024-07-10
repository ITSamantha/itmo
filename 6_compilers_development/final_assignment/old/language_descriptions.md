# Шаг №1
Разработка описания языка в терминах КС грамматики. Определение лексического состава языка.

## Расширенные формы Бэксуса-Науэра (РБНФ)
Метаязык, предложенный Бэкусом и Науром, использует следующие обозначения:
- символ «::=» отделяет левую часть правила от правой (читается:«определяется как»);
- нетерминалы обозначаются произвольной символьной строкой, заключенной в угловые скобки «<» и «>»;
- терминалы - это символы, используемые в описываемом языке;
- правило может определять порождение нескольких альтернативных цепочек, отделяемых друг от друга символом вертикальной черты «|» (читается: «или»).

Для повышения удобства и компактности описаний, в РБНФ вводятся следующие дополнительные конструкции (метасимволы):
- квадратные скобки «[» и «]» означают, что заключенная в них синтаксическая конструкция может отсутствовать;
- фигурные скобки «{» и «}» означают повторение заключенной в них синтаксической конструкции ноль или более раз;
- сочетание фигурных скобок и косой черты «{/» и «/}» используется для обозначения повторения один и более раз;
- круглые скобки «(» и «)» используются для ограничения альтернативных конструкций.

Для языка Chirp реализована следующая РБНФ:
```
<digit> :: = 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9

<letter> :: = a | b | c | d | e | f | g | h | i | j | k | l | m | n | o | p | r | s | t | u | v | w | x | y | z |
              A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | R | S | T | U | V | W | X | Y | Z

<sign> :: = + | -

<arithmetic_operator> :: = + | - | * | / | %

<binary_logical_oprator> :: = and | or
<unary_logical_operator> :: = not

<assignment_operator> :: =  :=

<key_words> :: = var | if | elif | else | while | for | print | begin | end | start| finish | chirp

<int> :: = [<sign>] <number> 
<bool> :: = true | false

<type_definition> :: = int | bool
<type> ::= <int> | <bool>

<identifier> :: = <letter> { <letter> | <digit> }
<variable_declaration> :: = var <identifier> {, <identifier>} : <type_definition> ;

<number> :: = {/ <digit> /}

<expression> :: =  	<type> |
			<identifier> |
			(<expression>) |
			<expression> <arithmetic_operator> <expression> |
			<unary_logical_operator> <expression> |  
			<expression> <binary_logical_operator> <expression>

<assignment> :: = 	<identifier> <assignment_operator> <expression> ;

<conditional_statement> :: = if (<expression>) <compound_statement> { elif (<expression>) <compound_ statement> } {else <compound_statement> }

<loop_statement> :: = <while_statement> | <for_statement>
<while_statement> :: = while (<expression>) <compound_ statement>
<for_statement> :: = for (<assignment>; <expression>; <expression>)  <compound_ statement>

<print_statement> :: = print(<expression>) ;

<simple_statement> :: =	<assignment> | <variable_declaration> | <print_statement>
<structured_statement> :: = <conditional_statement> | <loop_statement> 

<statement>  :: = <simple_statement> | <structured_statement> 
			
<compound_statement> :: = begin <statement> {; <statement>} end;

<program> :: = 		chirp 
				start
					<compound_statement>
				finish

<single_comment> :: =  // <comment_text> 
<multi_comment> :: =  /* <comment_text>  */
<comment_text> :: = { ANY_ASCII_CHAR }
```

## Описание языка в терминах КС грамматики


## Лексический состав языка
