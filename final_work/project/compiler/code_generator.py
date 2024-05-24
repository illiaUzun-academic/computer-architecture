# compiler/code_generator.py

class CodeGenerator:
    def __init__(self):
        """
        Ініціалізує генератор коду.
        """
        self.instructions = []

    def generate(self, statements):
        """
        Генерація інструкцій з дерева розбору.

        :param statements: Список операторів (дерево розбору).
        :return: Список згенерованих інструкцій.
        """
        for statement in statements:
            if statement[0] == 'ASSIGN':
                identifier = statement[1]
                expr = statement[2]
                if expr[0] in ('PLUS', 'MINUS', 'MUL', 'DIV', 'SQR', 'MOD', 'NEG'):
                    self.generate_expression(expr)
                    self.instructions.append(('STORE', identifier))
                else:
                    value = self.evaluate_expression(expr)
                    self.instructions.append(('LOAD', value))
                    self.instructions.append(('STORE', identifier))
        return self.instructions

    def generate_expression(self, expr):
        """
        Генерація інструкцій для арифметичних операцій.

        :param expr: Вираз (дерево розбору).
        """
        if expr[0] == 'PLUS':
            left = self.evaluate_expression(expr[1])
            right = self.evaluate_expression(expr[2])
            self.instructions.append(('LOAD', left))
            self.instructions.append(('ADD', right))
        elif expr[0] == 'MINUS':
            left = self.evaluate_expression(expr[1])
            right = self.evaluate_expression(expr[2])
            self.instructions.append(('LOAD', left))
            self.instructions.append(('SUB', right))
        elif expr[0] == 'MUL':
            left = self.evaluate_expression(expr[1])
            right = self.evaluate_expression(expr[2])
            self.instructions.append(('LOAD', left))
            self.instructions.append(('MUL', right))
        elif expr[0] == 'DIV':
            left = self.evaluate_expression(expr[1])
            right = self.evaluate_expression(expr[2])
            self.instructions.append(('LOAD', left))
            self.instructions.append(('DIV', right))
        elif expr[0] == 'SQR':
            value = self.evaluate_expression(expr[1])
            self.instructions.append(('LOAD', value))
            self.instructions.append(('SQR',))
        elif expr[0] == 'MOD':
            left = self.evaluate_expression(expr[1])
            right = self.evaluate_expression(expr[2])
            self.instructions.append(('LOAD', left))
            self.instructions.append(('MOD', right))
        elif expr[0] == 'NEG':
            value = self.evaluate_expression(expr[1])
            self.instructions.append(('LOAD', value))
            self.instructions.append(('NEG',))

    def evaluate_expression(self, expr):
        """
        Оцінка виразу та генерація відповідних інструкцій.

        :param expr: Вираз (дерево розбору).
        :return: Значення виразу.
        """
        if expr is None:
            raise ValueError("Invalid expression")
        if expr[0] == 'NUMBER':
            return expr[1]
        elif expr[0] == 'IDENTIFIER':
            return expr[1]
        else:
            raise ValueError(f"Unknown expression type: {expr[0]}")
