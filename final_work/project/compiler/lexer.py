# compiler/lexer.py

class Lexer:

    def __init__(self, source_code):
        """
        Ініціалізує лексер з вихідним кодом.

        :param source_code: Вихідний код програми як рядок.
        """
        self.source_code = source_code
        self.tokens = []
        self.current_char = None
        self.current_pos = -1
        self.advance()

    def advance(self):
        """
        Переміщається до наступного символу у вихідному коді.
        """
        self.current_pos += 1
        self.current_char = self.source_code[self.current_pos] if self.current_pos < len(self.source_code) else None

    def tokenize(self):
        """
        Розбиває вихідний код на токени.

        :return: Список токенів.
        """
        while self.current_char is not None:
            if self.current_char.isspace():
                self.advance()
            elif self.current_char.isdigit():
                self.tokens.append(self.create_number())
            elif self.current_char.isalpha():
                self.tokens.append(self.create_identifier())
            elif self.current_char == '+':
                self.tokens.append(('PLUS', self.current_char))
                self.advance()
            elif self.current_char == '-':
                self.tokens.append(('MINUS', self.current_char))
                self.advance()
            elif self.current_char == '*':
                self.tokens.append(('MUL', self.current_char))
                self.advance()
            elif self.current_char == '/':
                self.tokens.append(('DIV', self.current_char))
                self.advance()
            elif self.current_char == '%':
                self.tokens.append(('MOD', self.current_char))
                self.advance()
            elif self.current_char == '=':
                self.tokens.append(('EQ', self.current_char))
                self.advance()
            elif self.current_char == '!':
                self.advance()
                if self.current_char == '=':
                    self.tokens.append(('NEQ', '!='))
                    self.advance()
                else:
                    self.tokens.append(('ERROR', '!'))
            elif self.current_char == '^':
                self.tokens.append(('SQR', self.current_char))
                self.advance()
            elif self.current_char == '~':
                self.tokens.append(('NEG', self.current_char))
                self.advance()
            else:
                self.tokens.append(('UNKNOWN', self.current_char))
                self.advance()
        return self.tokens

    def create_number(self):
        """
        Створює токен для чисел.

        :return: Токен для числа.
        """
        num_str = ''
        while self.current_char is not None and self.current_char.isdigit():
            num_str += self.current_char
            self.advance()
        return ('NUMBER', int(num_str))

    def create_identifier(self):
        """
        Створює токен для ідентифікаторів.

        :return: Токен для ідентифікатора.
        """
        id_str = ''
        while self.current_char is not None and self.current_char.isalnum():
            id_str += self.current_char
            self.advance()
        return ('IDENTIFIER', id_str)
