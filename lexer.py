'''Este arquivo contém a definição do lexer (analisador léxico):'''

import ply.lex as lex

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
