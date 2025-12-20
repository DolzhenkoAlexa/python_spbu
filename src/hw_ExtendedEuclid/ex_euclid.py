def extended_algorithm(a, b):
    """
    Расширенный алгоритм Евклида.
    Возвращает (gcd, x, y) такой что: a*x + b*y = gcd(a, b)
    """
    if b == 0:
        if a >= 0:
            return (a, 1, 0)
        else:
            return (-a, -1, 0)  # НОД всегда неотрицательный

    # Рекурсивный вызов
    gcd, prev_x, prev_y = extended_algorithm(b, a % b)

    x = prev_y
    y = prev_x - (a // b) * prev_y

    return (gcd, x, y)

gcd, x, y = extended_algorithm(240, -46)
print(f"НОД(240, -46) = {gcd}")
