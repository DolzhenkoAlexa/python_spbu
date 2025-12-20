def queens_counter(board_size):
    # Множества для отслеживания занятых позиций - столбцы и диагонали (/ и \)
    columns = set()
    diag1 = set()
    diag2 = set()

    # Рекурсивно размещает ферзей построчно, используя метод возврата.
    def backtrack(row):
        # Базовый случай: все строки успешно заполнены
        if row == board_size:
            return 1
        count = 0

        # Перебираем все возможные столбцы в текущей строке
        for col in range(board_size):
            # Проверяем, атакует ли текущая позиция уже размещенных ферзей
            if col in columns or (row + col) in diag1 or (row - col) in diag2:
                continue

            # Размещаем ферзя в текущей позиции
            columns.add(col)
            diag1.add(row + col)
            diag2.add(row - col)

            # Рекурсивно размещаем ферзей в следующих строках
            count += backtrack(row + 1)

            # Убираем ферзя для проверки других позиций (backtracking)
            columns.remove(col)
            diag1.remove(row + col)
            diag2.remove(row - col)
        return count

    # Начинаем рекурсивный поиск с первой строки (индекс 0)
    return backtrack(0)

n = int(input("Введите n до 14 включительно: "))
result = queens_counter(n)
print(f"Количество расстановок {n} ферзей: {result}")
