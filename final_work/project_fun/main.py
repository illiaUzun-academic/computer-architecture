from compiler.lexer import Lexer
from compiler.parser import Parser
from compiler.code_generator import CodeGenerator
from architecture.emulator import Emulator


def read_program(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


if __name__ == "__main__":
    program_files = ["examples/program_1.isir", "examples/program_2.isir", "examples/program_3.isir"]

    for program_file in program_files:
        print(f"Виконання програми з файлу: {program_file}")
        source_code = read_program(program_file)

        lexer = Lexer(source_code)
        tokens = lexer.tokenize()

        parser = Parser(tokens)
        statements = parser.parse()

        code_generator = CodeGenerator()
        instructions = code_generator.generate(statements)
        print("Згенеровані інструкції:", instructions)

        emulator = Emulator()
        emulator.run(instructions)
        print("Стан пам'яті:", emulator.cpu.memory)
        print("-" * 50)
