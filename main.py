import timeit
import random


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    # Спочатку об'єднайте менші елементи
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Якщо в лівій або правій половині залишилися елементи,
    # додайте їх до результату
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged


def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst


def timsort(arr):
    return sorted(arr)


# Тестові дані
test_data = {
    'small': [random.randint(0, 100) for _ in range(100)],
    'medium': [random.randint(0, 100) for _ in range(1000)],
    'large': [random.randint(0, 100) for _ in range(10000)]
}

# Вимірюємо час виконання для кожного алгоритму на кожному наборі даних
for size, data in test_data.items():
    print(f"Results for {size} dataset:")
    for algorithm in [merge_sort, insertion_sort, timsort]:
        time_taken = timeit.timeit(lambda: algorithm(data.copy()), number=1)
        print(f"{algorithm.__name__}: {time_taken:.6f} seconds")
    print()
