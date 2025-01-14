import random


def quicksort(arr: list[int]) -> list[int]:
    """Алгоритм быстрой сортировки с рандомной опорой."""
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)


arr = [44, 60, 10, 61, 60, 2, 62, 18, 2, 69]
result = quicksort(arr)
print(result)


def quicksort_2(arr: list[int]) -> list[int]:
    """Алгоритм быстрой сортировки с опорой по центру массива."""
    len_array = len(arr)
    if len_array <= 1:
        return arr
    mid_idx = len_array // 2
    pivot = arr[mid_idx]
    left, center, right = partition(arr, pivot)
    return quicksort_2(left) + center + quicksort_2(right)


def partition(arr, pivot):
    """
    Разбивает массив на три разных массива относительно опорного элемента.
    """
    left, center, right = [], [], []
    for i in arr:
        if i < pivot:
            left.append(i)
        elif i > pivot:
            right.append(i)
        else:
            center.append(i)
    return left, center, right


arr = [44, 60, 10, 61, 60, 2, 62, 18, 2, 69]
result = quicksort_2(arr)
print(result)
