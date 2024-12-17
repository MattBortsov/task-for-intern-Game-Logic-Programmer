class CircularBuffer:
    """Циклический буфер на основе списка."""

    def __init__(self, capacity: int):
        if capacity <= 0:
            raise ValueError('Размер буфера должен быть положительным числом.')
        self.buffer = [None] * capacity
        self.capacity = capacity
        self.head = 0
        self.tail = 0
        self.size = 0

    def enqueue(self, item):
        """Добавить элемент в буфер."""
        if self.is_full():
            raise OverflowError('Буфер заполнен.')
        self.buffer[self.tail] = item
        self.tail = (self.tail + 1) % self.capacity
        self.size += 1

    def dequeue(self):
        """Извлечь элемент из буфера."""
        if self.is_empty():
            raise IndexError('Буфер пуст.')
        item = self.buffer[self.head]
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return item

    def is_empty(self):
        """Проверка пуст ли буфер."""
        return self.size == 0

    def is_full(self):
        """Проверка заполнен ли буфер."""
        return self.size == self.capacity

    def __str__(self):
        return str([
            self.buffer[
                (self.head + i) % self.capacity
                ] for i in range(self.size)
            ])
