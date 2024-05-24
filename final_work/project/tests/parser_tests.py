from compiler.lexer import Lexer
from compiler.parser import Parser


def test_parser():
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

    parser = Parser(tokens)
    statements = parser.parse()

    expected_statements = [
        ('ASSIGN', 'a', ('NUMBER', 5)),
        ('ASSIGN', 'b', ('NUMBER', 10)),
        ('ASSIGN', 'c', ('PLUS', ('IDENTIFIER', 'a'), ('IDENTIFIER', 'b'))),
        ('ASSIGN', 'd', ('MUL', ('IDENTIFIER', 'c'), ('NUMBER', 2))),
        ('ASSIGN', 'e', ('MOD', ('IDENTIFIER', 'c'), ('NUMBER', 3))),
        ('ASSIGN', 'f', ('NEG', ('IDENTIFIER', 'd'))),
        ('ASSIGN', 'g', ('SQR', ('IDENTIFIER', 'd')))
    ]

    assert statements == expected_statements, f"Expected {expected_statements}, but got {statements}"
    print("Parser test passed!")


if __name__ == "__main__":
    test_parser()
