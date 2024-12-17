from collections import deque
from typing import Deque


class CircularBufferDeque:
    """Циклический буфер FIFO на основе collections.deque."""

    def __init__(self, capacity: int):
        if capacity <= 0:
            raise ValueError("Размер буфера должен быть больше 0.")
        self.buffer: Deque[int] = deque(maxlen=capacity)

    def enqueue(self, item):
        """Добавить элемент в буфер."""
        if self.is_full():
            raise OverflowError("Буфер заполнен.")
        self.buffer.append(item)

    def dequeue(self):
        """Извлечь элемент из буфера."""
        if self.is_empty():
            raise IndexError("Буфер пуст.")
        return self.buffer.popleft()

    def is_empty(self):
        """Проверка пуст ли буфер."""
        return not self.buffer

    def is_full(self):
        """Проверка заполнен ли буфер."""
        return len(self.buffer) == self.buffer.maxlen

    def __str__(self):
        return str(list(self.buffer))
