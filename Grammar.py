'''Este arquivo define a gramática e as regras de produção:'''


import ply.yacc as yacc
from lexer import tokens

class Grammar:

    def __init__(self) -> None:
        self.__terminals = {}
        self.__nonterminals = {}
        self.__productions = {}
        self.__id = 0

    def add_terminal(self, x: str) -> int:
        if x in self.__nonterminals:
            raise ValueError()
        self.__terminals[x] = self.__id
        self.__id = self.__id+1
        return self.__terminals[x]

    def add_nonterminal(self, X: str):
        if X in self.__terminals:
            raise ValueError()
        self.__nonterminals[X] = self.__id
        self.__id = self.__id + 1
        return self.__nonterminals[X]

    def grammar(self, S: str) -> None:
        self.add_nonterminal(S)

    def add_production(self, A: str, rhs: list) -> int:
        self.__productions[self.__id] = {'lhs': '', 'rhs': []}
        self.__productions[self.__id]['lhs'] = A
        self.__productions[self.__id]['rhs'] = rhs
        self.__id = self.__id+1
        return self.__id - 1

    def terminals(self) -> iter:
        return iter(self.__terminals)

    def nonterminals(self) -> iter:
        return iter(self.__nonterminals)

    def productions(self) -> iter:
        return iter(self.__productions)

    def is_terminal(self, X: str) -> bool:
        return X in self.__terminals

    def rhs(self, p: int) -> list:
        return self.__productions[p]['rhs']

    def lhs(self, p: int) -> str:
        return self.__productions[p]['lhs']

    def productions_for(self, A: str) -> list:
        l = []
        for k, v in self.__productions.items():
            if v['lhs'] == A:
                l.append(k)
        return l

    def occurrences(self, X: str) -> list:
        l = []
        for k, v in self.__productions.items():
            for i, rhs in enumerate(v['rhs']):
                if rhs == X:
                    l.append((k, i))
        return l

    def production(self, O: tuple[int, int]) -> int:
        return O[0]

    def tail(self, p: int, i: int) -> list:
        return self.__productions[p]['rhs'][i+1:]

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
