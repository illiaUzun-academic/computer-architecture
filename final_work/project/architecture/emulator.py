# architecture/emulator.py

from .cpu import CPU
from .instruction_set import InstructionSet
from .memory import Memory


class Emulator:
    def __init__(self):
        """
        Ініціалізує емулятор.
        """
        self.cpu = CPU()
        self.memory = Memory()
        self.instruction_set = InstructionSet()

    def run(self, instructions):
        """
        Запуск емуляції програми.

        :param instructions: Список інструкцій для виконання.
        """
        for instruction in instructions:
            instr_name, *args = instruction
            instr_func = self.instruction_set.instructions[instr_name]
            self.cpu.execute(instr_func, *args)
