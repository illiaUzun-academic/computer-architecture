# architecture/instruction_set.py

class InstructionSet:
    def __init__(self):
        """
        Ініціалізує набір інструкцій.
        """
        self.instructions = {
            'LOAD': self.load,
            'STORE': self.store,
            'ADD': self.add,
            'SUB': self.sub,
            'MUL': self.mul,
            'DIV': self.div,
            'SQR': self.sqr,
            'MOD': self.mod,
            'NEG': self.neg
        }

    def load(self, cpu, value):
        """
        Завантаження значення у акумулятор процесора.

        :param cpu: Процесор.
        :param value: Значення для завантаження.
        """
        if isinstance(value, str):
            value = cpu.memory.get(value, 0)
        cpu.accumulator = value

    def store(self, cpu, identifier):
        """
        Збереження значення з акумулятора у пам'ять.

        :param cpu: Процесор.
        :param identifier: Ідентифікатор пам'яті.
        """
        cpu.memory[identifier] = cpu.accumulator

    def add(self, cpu, value):
        """
        Додавання значення до акумулятора.

        :param cpu: Процесор.
        :param value: Значення для додавання.
        """
        if isinstance(value, str):
            value = cpu.memory.get(value, 0)
        cpu.accumulator += value

    def sub(self, cpu, value):
        """
        Віднімання значення від акумулятора.

        :param cpu: Процесор.
        :param value: Значення для віднімання.
        """
        if isinstance(value, str):
            value = cpu.memory.get(value, 0)
        cpu.accumulator -= value

    def mul(self, cpu, value):
        """
        Множення акумулятора на значення.

        :param cpu: Процесор.
        :param value: Значення для множення.
        """
        if isinstance(value, str):
            value = cpu.memory.get(value, 0)
        cpu.accumulator *= value

    def div(self, cpu, value):
        """
        Ділення акумулятора на значення.

        :param cpu: Процесор.
        :param value: Значення для ділення.
        """
        if isinstance(value, str):
            value = cpu.memory.get(value, 0)
        cpu.accumulator /= value

    def sqr(self, cpu):
        """
        Піднесення значення у акумуляторі до квадрату.

        :param cpu: Процесор.
        """
        cpu.accumulator **= 2

    def mod(self, cpu, value):
        """
        Залишок від ділення значення у акумуляторі на задане значення.

        :param cpu: Процесор.
        :param value: Значення для операції залишку від ділення.
        """
        if isinstance(value, str):
            value = cpu.memory.get(value, 0)
        cpu.accumulator %= value

    def neg(self, cpu):
        """
        Зміна знаку значення у акумуляторі на протилежний.

        :param cpu: Процесор.
        """
        cpu.accumulator = -cpu.accumulator
