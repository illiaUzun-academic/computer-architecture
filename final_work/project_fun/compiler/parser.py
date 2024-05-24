# compiler/parser.py

class Parser:
    def __init__(self, tokens):
        """
        Ініціалізує парсер з токенами.

        :param tokens: Список токенів.
        """
        self.tokens = tokens
        self.current_token = None
        self.current_pos = -1
        self.advance()

    def advance(self):
        """
        Переміщається до наступного токену.
        """
        self.current_pos += 1
        self.current_token = self.tokens[self.current_pos] if self.current_pos < len(self.tokens) else None

    def parse(self):
        """
        Основний цикл для парсингу токенів у дерево розбору.

        :return: Список операторів (дерево розбору).
        """
        statements = []
        while self.current_token is not None:
            statement = self.parse_statement()
            if statement:
                statements.append(statement)
            else:
                self.advance()  # Перехід до наступного токену, щоб уникнути зациклення
        return statements

    def parse_statement(self):
        """
        Парсинг окремих операторів.

        :return: Оператор (дерево розбору).
        """
        if self.current_token and self.current_token[0] == 'IDENTIFIER':
            identifier = self.current_token[1]
            self.advance()
            if self.current_token and self.current_token[0] == 'EQ':
                self.advance()
                expr = self.parse_expression()
                return ('ASSIGN', identifier, expr)
        return None

    def parse_expression(self):
        """
        Парсинг виразів.

        :return: Вираз (дерево розбору).
        """
        left = self.parse_term()
        while self.current_token is not None and self.current_token[0] in ('PLUS', 'MINUS'):
            op = self.current_token
            self.advance()
            right = self.parse_term()
            left = (op[0], left, right)
        return left

    def parse_term(self):
        """
        Парсинг термів.

        :return: Терм (дерево розбору).
        """
        left = self.parse_factor()
        while self.current_token is not None and self.current_token[0] in ('MUL', 'DIV', 'MOD'):
            op = self.current_token
            self.advance()
            right = self.parse_factor()
            left = (op[0], left, right)
        return left

    def parse_factor(self):
        """
        Парсинг факторів.

        :return: Фактор (дерево розбору).
        """
        token = self.current_token
        if token[0] in ('NUMBER', 'IDENTIFIER'):
            self.advance()
            if self.current_token is not None and self.current_token[0] == 'SQR':
                self.advance()
                return ('SQR', token)
            return token
        elif token[0] == 'SQR':
            self.advance()
            factor = self.parse_factor()
            return ('SQR', factor)
        elif token[0] == 'NEG':
            self.advance()
            factor = self.parse_factor()
            return ('NEG', factor)
        return None
