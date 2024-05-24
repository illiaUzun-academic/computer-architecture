from compiler.lexer import Lexer


def test_lexer():
    source_code = """
    a = 5
    b = 10
    c = a + b
    d = c * 2
    e = c % 3
    f = ~d
    g = d ^ 2
    """

    lexer = Lexer(source_code)
    tokens = lexer.tokenize()
    expected_tokens = [
        ('IDENTIFIER', 'a'), ('EQ', '='), ('NUMBER', 5),
        ('IDENTIFIER', 'b'), ('EQ', '='), ('NUMBER', 10),
        ('IDENTIFIER', 'c'), ('EQ', '='), ('IDENTIFIER', 'a'),
        ('PLUS', '+'), ('IDENTIFIER', 'b'),
        ('IDENTIFIER', 'd'), ('EQ', '='), ('IDENTIFIER', 'c'),
        ('MUL', '*'), ('NUMBER', 2),
        ('IDENTIFIER', 'e'), ('EQ', '='), ('IDENTIFIER', 'c'),
        ('MOD', '%'), ('NUMBER', 3),
        ('IDENTIFIER', 'f'), ('EQ', '='), ('NEG', '~'), ('IDENTIFIER', 'd'),
        ('IDENTIFIER', 'g'), ('EQ', '='), ('IDENTIFIER', 'd'), ('SQR', '^'), ('NUMBER', 2)
    ]

    assert tokens == expected_tokens, f"Expected {expected_tokens}, but got {tokens}"
    print("Lexer test passed!")


if __name__ == "__main__":
    test_lexer()
