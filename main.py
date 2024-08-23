from grammar import Grammar

def main():
    test_strings = [
        "x = 5",
        "if (x + 1) y = 10 else z = 15 fi",
        "while (x + 1) do y = 20 od",
        "begin x = 5; y = 10 end"
    ]

    for s in test_strings:
        print(f"Testando a string: '{s}'")
        lexer.input(s)
        for token in lexer:
            print(token)
        parser.parse(s)
        print("Análise concluída.\n")

if __name__ == '__main__':
    principal()