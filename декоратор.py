def my_decorator(func):
    def wrapper():
        print("Старт")
        func()
        print("Финиш")
    return wrapper


@my_decorator
def test():
    print("Тест выполняется")


test()