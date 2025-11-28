import itertools

# Функция для проверки того, что ферзи не бьют друг друга, то есть расстановка валидная
def is_valid(cords, n):
    # Проверяем строки
    for i in range(n):
        for j in range(i + 1, n):
            # Если два ферзя в одной строке
            if cords[i][0] == cords[j][0]:
                return False
            # Если два ферзя в одном столбце
            if cords[i][1] == cords[j][1]:
                return False
            # Если два ферзя на одной диагонали
            if abs(cords[i][0] - cords[j][0]) == abs(cords[i][1] - cords[j][1]):
                return False
    return True

def queens_counter(n):
    count = 0 # Счетчик правильных расстановок ферзей

    # Генерируем все возможные наборы из N различных клеток
    all_cells = [(i, j) for i in range(n) for j in range(n)]

    # Возьмем все расстановки без повторяющихся клеток
    for cords in itertools.combinations(all_cells, n):
        if is_valid(cords, n):
            count += 1
    return count

n = int(input("Введите n: ")) # Можно до 6-ти, 7 уже не тянет (ждала больше минуты)
result = queens_counter(n)
print(f"Количество расстановок {n} ферзей: {result}")