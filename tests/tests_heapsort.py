import pytest
from ..src.hw_heapsort.sorts.py import heap_sort, bubble_sort, insertion_sort

# обычные unit тесты и крайние случаи
@pytest.mark.empty
def test_heap_sort_empty():
    """Тест для пустого списка"""
    result = heap_sort([])
    assert result == []


@pytest.mark.single
def test_heap_sort_single():
    """Тест для списка из одного элемента"""
    result = heap_sort([42])
    assert result == [42]


@pytest.mark.sorted
def test_heap_sort_sorted():
    """Тест для уже отсортированного списка"""
    result = heap_sort([1, 2, 3, 4, 5])
    assert result == [1, 2, 3, 4, 5]


@pytest.mark.reversed
def test_heap_sort_reversed():
    """Тест для списка, отсортированного в обратном порядке"""
    result = heap_sort([5, 4, 3, 2, 1])
    assert result == [1, 2, 3, 4, 5]


@pytest.mark.duplicates
def test_heap_sort_with_duplicates():
    """Тест для списка с дубликатами"""
    result = heap_sort([1, 3, 1, 3, 2, 1, 1, 1, 2])
    assert result == [1, 1, 1, 1, 1, 2, 2, 3, 3]

@pytest.mark.negative
def test_heap_sort_negative_num():
    """Тест с отрицательными числами"""
    result = heap_sort([-5, -1, -3, -2, -181818, -4])
    assert result == [-181818, -5, -4, -3, -2, -1]


@pytest.mark.mixed
def test_heap_sort_mixed():
    """Тест с положительными и отрицательными числами"""
    result = heap_sort([250000, -3, 5, -1, 2, -1000, 0, -2])
    assert result == [-1000, -3, -2, -1, 0, 2, 5, 250000]


@pytest.mark.float
def test_heap_sort_floats():
    """Тест с числами с плавающей точкой"""
    result = heap_sort([3.6, 1.2, 4.8, 2.1, 0.5, 2.0])
    assert result == [0.5, 1.2, 2.0, 2.1, 3.6, 4.8]

# тесты для сравнения heapsort и insertion sort и bubble sort
@pytest.mark.all_sorts_empty
def test_all_sorts_empty():
    """Тест для пустого списка"""
    heap_result = heap_sort([])
    insertion_result = insertion_sort([])
    bubble_result = bubble_sort([])
    python_result = sorted([])
    assert heap_result == insertion_result == bubble_result == python_result


@pytest.mark.all_sorts_single
def test_all_sorts_single():
    """Тест для списка из одного элемента"""
    heap_result = heap_sort([52])
    insertion_result = insertion_sort([52])
    bubble_result = bubble_sort([52])
    python_result = sorted([52])
    assert heap_result == insertion_result == bubble_result == python_result


@pytest.mark.all_sorts_sorted
def test_all_sorts_sorted():
    """Тест для уже отсортированного списка"""
    heap_result = heap_sort([1,2,3])
    insertion_result = insertion_sort([1,2,3])
    bubble_result = bubble_sort([1,2,3])
    python_result = sorted([1,2,3])
    assert heap_result == insertion_result == bubble_result == python_result


@pytest.mark.all_sorts_reversed
def test_all_sorts_reversed():
    """Тест для списка, отсортированного в обратном порядке"""
    heap_result = heap_sort([5, 4, 3])
    insertion_result = insertion_sort([5, 4, 3])
    bubble_result = bubble_sort([5, 4, 3])
    python_result = sorted([5, 4, 3])
    assert heap_result == insertion_result == bubble_result == python_result


@pytest.mark.all_sorts_duplicates
def test_all_sorts_with_duplicates():
    """Тест для списка с дубликатами"""
    heap_result = heap_sort([0, 0, 3, 5, 4, 5, 5, 3, 0, 0])
    insertion_result = insertion_sort([0, 0, 3, 5, 4, 5, 5, 3, 0, 0])
    bubble_result = bubble_sort([0, 0, 3, 5, 4, 5, 5, 3, 0, 0])
    python_result = sorted([0, 0, 3, 5, 4, 5, 5, 3, 0, 0])
    assert heap_result == insertion_result == bubble_result == python_result

@pytest.mark.all_sorts_negative
def test_all_sorts_negative_num():
    """Тест с отрицательными числами"""
    heap_result = heap_sort([-762, -10, -387, -37072])
    insertion_result = insertion_sort([-762, -10, -387, -37072])
    bubble_result = bubble_sort([-762, -10, -387, -37072])
    python_result = sorted([-762, -10, -387, -37072])
    assert heap_result == insertion_result == bubble_result == python_result


@pytest.mark.all_sorts_mixed
def test_all_sorts_mixed():
    """Тест с положительными и отрицательными числами"""
    heap_result = heap_sort([100, -1, 0, -387, 153])
    insertion_result = insertion_sort([100, -1, 0, -387, 153])
    bubble_result = bubble_sort([100, -1, 0, -387, 153])
    python_result = sorted([100, -1, 0, -387, 153])
    assert heap_result == insertion_result == bubble_result == python_result


@pytest.mark.all_sorts_float
def test_all_sorts_floats():
    """Тест с числами с плавающей точкой"""
    heap_result = heap_sort([1.0, -1.9, 0.0, -3.8, 153.5])
    insertion_result = insertion_sort([1.0, -1.9, 0.0, -3.8, 153.5])
    bubble_result = bubble_sort([1.0, -1.9, 0.0, -3.8, 153.5])
    python_result = sorted([1.0, -1.9, 0.0, -3.8, 153.5])
    assert heap_result == insertion_result == bubble_result == python_result
