# ЗАДАЧА 2.1 (чуть сложнее)
# Цель: добавить имя функции в лог.
#
# 1) На базе trace_start сделай декоратор trace_name(func)
# 2) Внутри wrapper печатай:
#    start <имя_функции>
# 3) Затем вызывай исходную функцию и возвращай ее результат
# 4) Примени к функции:
#    def add(a, b): return a + b
# 5) Вызови:
#    print(add(2, 3))
#
# Ожидаемая идея вывода:
# start add
# 5
#
# Подсказка:
# - имя функции: func.__name__

def trace_start(func):
    def wrapper(*args, **kwargs):
        print(f"start {func.__name__}")
        res = func(*args,**kwargs)
        return res
    return wrapper

@trace_start
def add(a, b):
    return a+b
print(add(a=2, b=3))