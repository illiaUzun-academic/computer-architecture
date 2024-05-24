# compiler/compiler.py

from .code_generator import CodeGenerator
from .lexer import Lexer
from .parser import Parser


class Compiler:
    def __init__(self, source_code):
        """
        Ініціалізує компілятор з вихідним кодом.

        :param source_code: Вихідний код програми як рядок.
        """
        self.source_code = source_code

    def compile(self):
        """
        Компілює вихідний код у набір інструкцій.

        :return: Згенеровані інструкції.
        """
        # Токенізація вихідного коду
        lexer = Lexer(self.source_code)
        tokens = lexer.tokenize()

        # Парсинг токенів у дерево розбору
        parser = Parser(tokens)
        statements = parser.parse()

        # Генерація інструкцій з дерева розбору
        code_generator = CodeGenerator()
        instructions = code_generator.generate(statements)

        return instructions
