'''
Gramática para uma linguagem simples.

'''

'''
1. Especificação da Gramática Atual
'''
'''Primeiro, temos as seguintes regras gramaticais:'''

Start → stmt $
Stmt → id assign E
Stmt → if lparen E rparen Stmt else Stmt fi
Stmt → if lparen E rparen Stmt fi
Stmt → while lparen E rparen do Stmt od
Stmt → begin Stmts end
Stmts → Stmts semi Stmt
Stmts → Stmt
E → E plus T
E → T
T → id
T → num



'''Regras de Declaração e Expressão Lógica:'''

Dccl → int id | float id;
Assign → id = expr;
Expr → Expr logic | Expr A;
Expr logic → ! Expr logic
Expr logic → Expr logic AND Expr logic
Expr logic → Expr logic OR Expr logic
Expr logic → (Expr logic)
Expr logic → Expr A OR Expr A



'''2. Identificação de Recursão à Esquerda'''

'''A recursão à esquerda ocorre quando uma produção de uma gramática tem uma regra onde o lado direito começa com o próprio não terminal do lado esquerdo. Neste caso, identificamos as seguintes regras com recursão à esquerda:'''

E → E plus T
Expr → Expr logic | Expr A
Expr logic → Expr logic AND Expr logic
Expr logic → Expr logic OR Expr logic


'''3. Eliminação da Recursão à Esquerda'''

Para E → E plus T | T

'''Identificamos a recursão à esquerda: E → E plus T'''
'''Criamos uma nova regra substituta E':'''

E → T E'
E' → plus T E' | ε
Para Expr → Expr logic | Expr A

'''Identificamos a recursão à esquerda: Expr → Expr logic
Criamos uma nova regra substituta Expr':'''

Expr → Expr A Expr'
Expr' → logic Expr' | ε

Para Expr logic → Expr logic AND Expr logic | Expr logic OR Expr logic | ! Expr logic | (Expr logic)

Identificamos a recursão à esquerda: Expr logic → Expr logic AND Expr logic e Expr logic → Expr logic OR Expr logic

Criamos uma nova regra substituta Expr logic':
Expr logic → ! Expr logic | (Expr logic) Expr logic'
Expr logic' → AND Expr logic Expr logic' | OR Expr logic Expr logic' | ε

'''Gramática Ajustada Sem Recursão à Esquerda'''

Regras Ajustadas:
Start → Stmt $
Stmt → id assign E | if lparen E rparen Stmt else Stmt fi | if lparen E rparen Stmt fi | while lparen E rparen do Stmt od | begin Stmts end
Stmts → Stmts semi Stmt | Stmt
E → T E'
E' → plus T E' | ε
T → id | num
Expr → Expr A Expr'
Expr' → logic Expr' | ε
Expr logic → ! Expr logic | (Expr logic) Expr logic'
Expr logic' → AND Expr logic Expr logic' | OR Expr logic Expr logic' | ε
Dccl → int id | float id;
Assign → id = expr;