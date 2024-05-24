from architecture.cpu import CPU
from architecture.instruction_set import InstructionSet


def test_cpu():
    cpu = CPU()
    instr = InstructionSet()

    # Тестування виконання інструкцій
    instr.load(cpu, 5)
    assert cpu.accumulator == 5, f"Expected 5, but got {cpu.accumulator}"

    instr.store(cpu, 'a')
    assert cpu.memory['a'] == 5, f"Expected 5, but got {cpu.memory['a']}"

    print("CPU tests passed!")


if __name__ == "__main__":
    test_cpu()
