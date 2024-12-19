import random


def quicksort(arr):
    """Алгоритм сортировки."""
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)


arr = list(map(int, input().split()))
result = quicksort(arr)
print(result)
