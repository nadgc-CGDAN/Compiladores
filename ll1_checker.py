from collections import defaultdict
from grammar import Grammar

class LL1GrammarChecker:

    def __init__(self, grammar):
        self.grammar = grammar
        self.first = defaultdict(set)
        self.follow = defaultdict(set)
        self.calculate_first()
        self.calculate_follow()

    def calculate_first(self):
        # Cálculo do conjunto FIRST para cada não terminal
        for nt in self.grammar.nonterminals():
            self.first[nt] = self.first_of(nt)

    def first_of(self, symbol):
        if symbol in self.grammar.terminals():
            return {symbol}
        first_set = set()
        for prod in self.grammar.productions_for(symbol):
            rhs = self.grammar.rhs(prod)
            if len(rhs) == 0:
                first_set.add('ε')
            else:
                for s in rhs:
                    f = self.first_of(s)
                    first_set.update(f - {'ε'})
                    if 'ε' not in f:
                        break
                else:
                    first_set.add('ε')
        return first_set

    def calculate_follow(self):
        # Regra 1: Coloca $ no FOLLOW do símbolo inicial
        start_symbol = list(self.grammar.nonterminals())[0]
        self.follow[start_symbol].add('$')
        
        # Aplicando regras de FOLLOW
        while True:
            updated = False
            for nt in self.grammar.nonterminals():
                for prod in self.grammar.productions_for(nt):
                    trailer = self.follow[nt]
                    for symbol in reversed(self.grammar.rhs(prod)):
                        if symbol in self.grammar.nonterminals():
                            before_update = len(self.follow[symbol])
                            self.follow[symbol].update(trailer)
                            if 'ε' in self.first[symbol]:
                                trailer = trailer.union(self.first[symbol] - {'ε'})
                            else:
                                trailer = self.first[symbol]
                            if len(self.follow[symbol]) > before_update:
                                updated = True
                        else:
                            trailer = self.first_of(symbol)
            if not updated:
                break

    def is_ll1(self):
        # Verifica se a gramática é LL(1) baseando-se nos conjuntos FIRST e FOLLOW
        for nt in self.grammar.nonterminals():
            first_sets = []
            for prod in self.grammar.productions_for(nt):
                rhs_first = self.first_of_rhs(self.grammar.rhs(prod))
                for f in first_sets:
                    if f & rhs_first:
                        return False  # Conflito encontrado
                first_sets.append(rhs_first)
                
                if 'ε' in rhs_first:
                    follow_set = self.follow[nt]
                    if follow_set & rhs_first:
                        return False  # Conflito ε-FOLLOW
        return True

    def first_of_rhs(self, rhs):
        if len(rhs) == 0:
            return {'ε'}
        first_set = set()
        for symbol in rhs:
            f = self.first_of(symbol)
            first_set.update(f - {'ε'})
            if 'ε' not in f:
                break
        else:
            first_set.add('ε')
        return first_set
