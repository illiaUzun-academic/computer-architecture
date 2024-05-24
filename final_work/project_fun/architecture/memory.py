# architecture/memory.py

class Memory:
    def __init__(self):
        """
        Ініціалізує пам'ять.
        """
        self.storage = {}

    def load(self, identifier):
        """
        Завантаження значення з пам'яті.

        :param identifier: Ідентифікатор пам'яті.
        :return: Значення з пам'яті або 0, якщо ідентифікатор не знайдено.
        """
        return self.storage.get(identifier, 0)

    def store(self, identifier, value):
        """
        Збереження значення у пам'ять.

        :param identifier: Ідентифікатор пам'яті.
        :param value: Значення для збереження.
        """
        self.storage[identifier] = value
