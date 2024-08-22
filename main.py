from grammar import Grammar

def main():
    # Criação da gramática
    G = Grammar()
    
    # Definição do símbolo inicial da gramática
    G.grammar('S')
    
    # Adicionando não terminais
    G.add_nonterminal('A')
    G.add_nonterminal('B')
    
    # Adicionando terminais
    G.add_terminal('a')
    G.add_terminal('b')
    G.add_terminal('c')
    
    # Adicionando produções
    G.add_production('S', ['A', 'B', 'c'])
    G.add_production('A', ['a'])
    G.add_production('A', ['c'])
    G.add_production('A', [])
    G.add_production('B', ['b'])
    G.add_production('B', ['c'])
    G.add_production('B', [])
    
    # Exibição das produções adicionadas
    print("Produções:")
    for p_id in G.productions():
        lhs = G.lhs(p_id)
        rhs = G.rhs(p_id)
        print(f"{lhs} -> {' '.join(rhs) if rhs else 'ε'}")

if __name__ == '__main__':
    main()
