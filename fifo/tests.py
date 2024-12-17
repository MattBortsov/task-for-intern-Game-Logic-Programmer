from fifo_deque import CircularBufferDeque
from fifo_list import CircularBuffer


def test_circular_buffers():
    print("Тестирование буфера на основе списка:")
    cb1 = CircularBuffer(3)
    cb1.enqueue(1)
    cb1.enqueue(2)
    cb1.enqueue(3)
    print(cb1)
    cb1.dequeue()
    cb1.enqueue(4)
    print(cb1)

    print("\nТестирование буфера на основе deque:")
    cb2 = CircularBufferDeque(3)
    cb2.enqueue(1)
    cb2.enqueue(2)
    cb2.enqueue(3)
    cb2.enqueue(4)
    print(cb2)
    cb2.dequeue()
    cb2.enqueue(4)
    print(cb2)


test_circular_buffers()
