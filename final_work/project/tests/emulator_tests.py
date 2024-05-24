from architecture.emulator import Emulator


def test_emulator():
    emulator = Emulator()

    # Інструкції для тестування
    instructions = [
        ('LOAD', 5), ('STORE', 'a'),
        ('LOAD', 10), ('STORE', 'b'),
        ('LOAD', 'a'), ('ADD', 'b'), ('STORE', 'c')
    ]

    emulator.run(instructions)

    # Перевірка стану пам'яті після виконання інструкцій
    expected_memory = {'a': 5, 'b': 10, 'c': 15}
    assert emulator.cpu.memory == expected_memory, f"Expected {expected_memory}, but got {emulator.cpu.memory}"

    print("Emulator tests passed!")


if __name__ == "__main__":
    test_emulator()
