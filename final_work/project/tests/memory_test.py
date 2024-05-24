from architecture.memory import Memory


def test_memory():
    memory = Memory()

    # Тестування збереження та завантаження значення
    memory.store('a', 10)
    assert memory.load('a') == 10, f"Expected 10, but got {memory.load('a')}"

    # Тестування завантаження значення за замовчуванням
    assert memory.load('b') == 0, f"Expected 0, but got {memory.load('b')}"

    print("Memory tests passed!")


if __name__ == "__main__":
    test_memory()
