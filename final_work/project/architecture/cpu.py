# architecture/cpu.py

class CPU:
    def __init__(self):
        """
        Ініціалізує процесор з акумулятором і пам'яттю.
        """
        self.accumulator = 0
        self.memory = {}

    def execute(self, instruction, *args):
        """
        Виконання інструкції.

        :param instruction: Функція інструкції для виконання.
        :param args: Аргументи інструкції.
        """
        instruction(self, *args)
