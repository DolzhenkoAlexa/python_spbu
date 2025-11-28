# Функция для проверки того, что ферзи не бьют друг друга, то есть расстановка валидная
def is_valid(cords, n):
    # Проверяем строки и столбцы
    rows = [q[0] for q in cords]
    columns = [q[1] for q in cords]
    if len(set(rows)) != n or len(set(columns)) != n:
        return False

    # Проверяем диагонали
    for i in range(n):
        for j in range(i + 1, n):
            if abs(cords[i][0] - cords[j][0]) == abs(cords[i][1] - cords[j][1]):
                return False
    return True


def queens_counter(row, n, placed_queens):
    count = 0
    if row == n: # Если дошли до конца доски, то завершаем
        if is_valid(placed_queens, n):
            return 1
        return 0

    for column in range(n):
        if (row, column) not in placed_queens: # Проверка, чтобы не было двух (0,1)
            new = placed_queens + [(row, column)]
            count += queens_counter(row + 1, n, new)
    return count


def count_queens_recursive(n):
    return queens_counter(0, n, [])


n = int(input("Введите n: ")) #Можно до 7-ми быстро, 8 выдает у меня за секунд 15
result = count_queens_recursive(n)
print(f"Количество расстановок {n} ферзей: {result}")