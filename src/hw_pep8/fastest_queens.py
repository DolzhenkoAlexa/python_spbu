def queens_counter(board_size):
    # Множества для отслеживания занятых позиций - столбцы и диагонали (восходящие и нисходящие)
    columns = set()
    rising_diag = set()
    descending_diag = set()

    # Рекурсивно размещает ферзей построчно, используя метод возврата
    def backtrack(row):
        # Все строки успешно заполнены
        if row == board_size:
            return 1
        count = 0

        # Перебираем все возможные столбцы в текущей строке
        for col in range(board_size):
            # Проверяем, атакует ли текущая позиция уже размещенных ферзей
            if col in columns or (row + col) in rising_diag or (row - col) in descending_diag:
                continue

            # Размещаем ферзя в текущей позиции
            columns.add(col)
            rising_diag.add(row + col)
            descending_diag.add(row - col)

            # Рекурсивно размещаем ферзей в следующих строках
            count += backtrack(row + 1)

            # Убираем ферзя для проверки других позиций (backtracking)
            columns.remove(col)
            rising_diag.remove(row + col)
            descending_diag.remove(row - col)
            
        return count

    # Начинаем рекурсивный поиск с первой строки (индекс 0)
    return backtrack(0)

board_size = int(input("Введите n. (Можно до 14 включительно): "))
result = queens_counter(board_size)
print(f"Количество расстановок {board_size} ферзей: {result}")
