from grammar import Grammar
from ll1_checker import LL1GrammarChecker

def main():
    # Criação de uma gramática de exemplo
    g = Grammar()
    g.grammar("S")
    g.add_terminal("a")
    g.add_terminal("b")
    g.add_nonterminal("A")
    g.add_production("S", ["a", "A"])
    g.add_production("A", ["b"])

    # Verificação se a gramática é LL(1)
    checker = LL1GrammarChecker(g)
    if checker.is_ll1():
        print("A gramática é LL(1).")
    else:
        print("A gramática NÃO é LL(1).")

if __name__ == "__main__":
    main()
