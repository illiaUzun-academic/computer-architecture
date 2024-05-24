# main.py

from architecture.emulator import Emulator
from compiler.compiler import Compiler


def read_program(file_path):
    with open(file_path, 'r') as file:
        return file.read()


if __name__ == "__main__":
    # Шлях до файлу програми
    program_files = ["examples/program_1.isir", "examples/program_2.isir", "examples/program_3.isir"]

    for program_file in program_files:
        print(f"Виконання програми з файлу: {program_file}")
        source_code = read_program(program_file)

        # Компіліяція вихідного коду
        compiler = Compiler(source_code)
        instructions = compiler.compile()
        print("Згенеровані інструкції:", instructions)

        # Запуск емулятора
        emulator = Emulator()
        emulator.run(instructions)
        print("Стан пам'яті:", emulator.cpu.memory)
        print("-" * 50)
