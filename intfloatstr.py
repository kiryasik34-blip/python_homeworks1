# ЗАДАЧА 2.0 (САМЫЙ ЛЕГКИЙ УРОВЕНЬ)
# Цель: просто увидеть, что декоратор работает.
#
# 1) Напиши декоратор trace_start(func)
# 2) Внутри wrapper:
#    - печатай строку: start
#    - вызывай исходную функцию
#    - возвращай результат исходной функции
# 3) Примени декоратор к функции hello(), которая возвращает "hi"
# 4) Вызови: print(hello())
#
# Ожидаемый вывод:
# start
# hi
#
# Подсказка:
# - пока без имени функции
# - просто фиксированная строка "start"

def trace_start(func):
    def wrapper(*args, **kwargs):
        print("start")
        res = func(*args,**kwargs)
        return res
    return wrapper

@trace_start
def hello(a):
    return a
print(hello(a="hi"))
# цув
