import ply.lex as lex
import ply.yacc as yacc

# Definição dos tokens
tokens = (
    'ID', 'NUM',
    'ASSIGN', 'PLUS',
    'LPAREN', 'RPAREN',
    'IF', 'ELSE', 'FI',
    'WHILE', 'DO', 'OD',
    'BEGIN', 'END',
    'SEMI',
    'INT', 'FLOAT',
    'AND', 'OR', 'NOT'
)

# Palavras reservadas
reserved = {
    'if': 'IF',
    'else': 'ELSE',
    'fi': 'FI',
    'while': 'WHILE',
    'do': 'DO',
    'od': 'OD',
    'begin': 'BEGIN',
    'end': 'END',
    'int': 'INT',
    'float': 'FLOAT',
    'and': 'AND',
    'or': 'OR',
    'not': 'NOT',
}

# Definição dos tokens
t_ASSIGN = r'='
t_PLUS = r'\+'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_SEMI = r';'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t

def t_NUM(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Ignorar espaços em branco
t_ignore = ' \t'

# Tratamento de erros
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Construção do lexer
lexer = lex.lex()

# Definição das regras de gramática ajustadas
def p_start(p):
    '''start : stmt'''

def p_stmt(p):
    '''stmt : ID ASSIGN E
            | IF LPAREN E RPAREN stmt ELSE stmt FI
            | IF LPAREN E RPAREN stmt FI
            | WHILE LPAREN E RPAREN DO stmt OD
            | BEGIN stmts END'''

def p_stmts(p):
    '''stmts : stmts SEMI stmt
             | stmt'''

def p_E(p):
    '''E : T E_prime'''

def p_E_prime(p):
    '''E_prime : PLUS T E_prime
               | empty'''

def p_T(p):
    '''T : ID
         | NUM'''

def p_expr(p):
    '''expr : expr_A expr_prime'''

def p_expr_prime(p):
    '''expr_prime : LOGIC expr_prime
                  | empty'''

def p_expr_A(p):
    '''expr_A : T'''

def p_expr_logic(p):
    '''expr_logic : NOT expr_logic
                  | LPAREN expr_logic RPAREN expr_logic_prime
                  | T expr_logic_prime'''

def p_expr_logic_prime(p):
    '''expr_logic_prime : AND expr_logic expr_logic_prime
                        | OR expr_logic expr_logic_prime
                        | empty'''

def p_empty(p):
    '''empty :'''
    pass

# Regras de declaração e atribuição (ajustadas para uso)
def p_dccl(p):
    '''dccl : INT ID
            | FLOAT ID'''

def p_assign(p):
    '''assign : ID ASSIGN expr'''

# Tratamento de erros de sintaxe
def p_error(p):
    print("Syntax error in input!")

# Construção do parser
parser = yacc.yacc()

# Exemplo de uso
data = '''
int x;
x = 3 + 5;
if (x > 0) x = x + 1 fi;
'''

# Parseando a entrada
result = parser.parse(data, lexer=lexer)
print(result)
