def curry(func, arity):
    if type(arity) != int:
        raise TypeError("Ошибка: Арность должна быть целым числом (int)")
    if arity < 0:
        raise ValueError("Ошибка: Арность должна быть положительной")
    def curried(*args):
        if len(args) == arity:
            return func(*args)
        elif len(args) > arity:
            raise ValueError("Ошибка: Ожидалась другое количество аргументов")
        else:
            def next_step(*new_args):
                return curried(*(args + new_args))
            return next_step
    
    return curried


def uncurry(func_curry, arity):
    if type(arity) != int:
        raise TypeError("Ошибка: Арность должна быть целым числом (int)")
    if arity < 0:
        raise ValueError("Ошибка: Арность должна быть положительной")
    
    def uncurried(*args):
        if len(args) != arity:
            raise ValueError("Ошибка: Ожидалась другое количество аргументов")
        
        result = func_curry
        for a in args:
            result = result(a)
        return result
    
    return uncurried
    