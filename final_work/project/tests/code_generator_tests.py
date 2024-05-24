from compiler.code_generator import CodeGenerator
from compiler.lexer import Lexer
from compiler.parser import Parser


def test_code_generator():
    source_code = """
    a = 5
    b = 10
    c = a + b
    d = c * 2
    e = c % 3
    f = ~d
    g = d ^ 2
    """

    # Токенізація
    lexer = Lexer(source_code)
    tokens = lexer.tokenize()

    # Парсинг
    parser = Parser(tokens)
    statements = parser.parse()
    print("Parsed statements:", statements)

    # Генерація коду
    code_generator = CodeGenerator()
    instructions = code_generator.generate(statements)

    expected_instructions = [
        ('LOAD', 5), ('STORE', 'a'),
        ('LOAD', 10), ('STORE', 'b'),
        ('LOAD', 'a'), ('ADD', 'b'), ('STORE', 'c'),
        ('LOAD', 'c'), ('MUL', 2), ('STORE', 'd'),
        ('LOAD', 'c'), ('MOD', 3), ('STORE', 'e'),
        ('LOAD', 'd'), ('NEG',), ('STORE', 'f'),
        ('LOAD', 'd'), ('SQR',), ('STORE', 'g')
    ]

    assert instructions == expected_instructions, f"Expected {expected_instructions}, but got {instructions}"
    print("Code generator test passed!")


if __name__ == "__main__":
    test_code_generator()
