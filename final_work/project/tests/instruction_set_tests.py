class CPU:
    def __init__(self):
        self.accumulator = 0
        self.memory = {}


from architecture.instruction_set import InstructionSet


def test_instruction_set():
    cpu = CPU()
    instr = InstructionSet()

    # Тестування LOAD і STORE
    instr.load(cpu, 5)
    assert cpu.accumulator == 5, f"Expected 5, but got {cpu.accumulator}"
    instr.store(cpu, 'a')
    assert cpu.memory['a'] == 5, f"Expected 5, but got {cpu.memory['a']}"

    # Тестування ADD
    instr.load(cpu, 10)
    instr.add(cpu, 'a')
    assert cpu.accumulator == 15, f"Expected 15, but got {cpu.accumulator}"

    # Тестування SUB
    instr.sub(cpu, 5)
    assert cpu.accumulator == 10, f"Expected 10, but got {cpu.accumulator}"

    # Тестування MUL
    instr.mul(cpu, 2)
    assert cpu.accumulator == 20, f"Expected 20, but got {cpu.accumulator}"

    # Тестування DIV
    instr.div(cpu, 4)
    assert cpu.accumulator == 5, f"Expected 5, but got {cpu.accumulator}"

    # Тестування SQR
    instr.sqr(cpu)
    assert cpu.accumulator == 25, f"Expected 25, but got {cpu.accumulator}"

    # Тестування MOD
    instr.load(cpu, 10)
    instr.mod(cpu, 4)
    assert cpu.accumulator == 2, f"Expected 2, but got {cpu.accumulator}"

    # Тестування NEG
    instr.neg(cpu)
    assert cpu.accumulator == -2, f"Expected -2, but got {cpu.accumulator}"

    print("Instruction set tests passed!")


if __name__ == "__main__":
    test_instruction_set()
