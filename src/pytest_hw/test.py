# Сортировка кучей
def heapify(arr, n, i):
    max_index = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[max_index]:
        max_index = left

    if right < n and arr[right] > arr[max_index]:
        max_index = right

    if max_index != i:
        arr[i], arr[max_index] = arr[max_index], arr[i]
        heapify(arr, n, max_index)


def heapsort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

    return arr


# Вспомогательные функции для тестов
def is_sorted(arr): #Проверка на отсортированность
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))

#Проверка на равенство двух массивов (для тестов с другими сортировками)
def arrays_equal(a, b):
    return a == b


# Тесты

# Самый базовый простой случай
def test():
    print("Тест 1")
    arr = [64, 1, 25, 0, 20, 22, 21, 9]
    arr_copy = arr.copy()

    heapsort(arr_copy)

    assert is_sorted(arr_copy)
    print("Пройдено")

# Повтор элементов в тесте
def test_repeat_num():
    print("Тест 2:")
    arr = [5, 1, 8, 1, 2, 8, 5, 1, 1]
    arr_copy = arr.copy()

    heapsort(arr_copy)

    assert is_sorted(arr_copy)
    print("Пройдено")

# Тест с отриц числами
def test_negative_num():
    print("Тест 3:")
    arr = [6, -5, -10000, -8, 0, 3, 8, -23, 9, -9]
    arr_copy = arr.copy()

    heapsort(arr_copy)

    assert is_sorted(arr_copy)
    print("Пройдено")


# Крайние случаи
# Тест с уже отсортированным массивом
def test_already_sorted():
    print("Тест 4:")
    arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    arr_copy = arr.copy()

    heapsort(arr_copy)

    assert is_sorted(arr_copy)
    print("Пройдено")

# Тест с отсортированным массивом наоборот
def test_reverse_sorted():
    print("Тест 5:")
    arr = [6, 5, 4, 3, 2, 1, 0]
    arr_copy = arr.copy()

    heapsort(arr_copy)

    assert is_sorted(arr_copy)
    print("Пройдено")

# Тест с одним элементом
def test_one_element():
    print("Тест 6")
    arr = [52]
    arr_copy = arr.copy()

    heapsort(arr_copy)

    assert is_sorted(arr_copy)
    assert arr_copy[0] == 52
    print("Пройдено")

# Тест с пустым массивом
def test_empty():
    print("Тест 7:")
    arr = []

    heapsort(arr)

    assert is_sorted(arr)
    print("Пройдено")


# PROPERTY-BASED ТЕСТЫ с другими сортировками для сравнения
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def test_bubble_sort():
    print("Тест 8:")
    arr = [666, 52, 34, 5, 12, 22, 11, 0, 6, 20]

    heap_result = arr.copy()
    bubble_result = arr.copy()

    heapsort(heap_result)
    bubble_sort(bubble_result)

    assert arrays_equal(heap_result, bubble_result)
    print("Пройдено")


def test_insertion_sort():
    print("Тест 9:")
    arr = [5, 21, 8, 10, 0, 91, 3, 78, 4, 0, 1, 2]

    heap_result = arr.copy()
    insertion_result = arr.copy()

    heapsort(heap_result)
    insertion_sort(insertion_result)

    assert arrays_equal(heap_result, insertion_result)
    print("Пройдено")



print("Запуск тестов:")
print(" ")
# Обычные тесты
test()
test_repeat_num()
test_negative_num()
test_already_sorted()
test_reverse_sorted()
test_one_element()
test_empty()


# Property-based тесты с другими сортировками
test_bubble_sort()
test_insertion_sort()

