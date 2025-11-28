def queens_counter(n):
    columns = set()
    diag1 = set()
    diag2 = set()

    def backtrack(row):
        if row == n:
            return 1  # нашли +1 решение

        count = 0
        for col in range(n):
            if col in columns or (row + col) in diag1 or (row - col) in diag2:
                continue

            columns.add(col)
            diag1.add(row + col) # диагонали слева направо (/)
            diag2.add(row - col) # диагонали справа налево (\)

            count += backtrack(row + 1)  # суммируем решения из этой ветки

            columns.remove(col)
            diag1.remove(row + col)
            diag2.remove(row - col)

        return count

    return backtrack(0) # Рекурсия 

n = int(input("Введите n: ")) # Можно до 13-ти включительно, 14 выдает меньше чем за полминуты
result = queens_counter(n)
print(f"Количество расстановок {n} ферзей: {result}")
