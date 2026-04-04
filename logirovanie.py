def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Функция {func.__name__} вызвана")
        return func(*args, **kwargs)
    return wrapper


@logger
def add(a, b):
    return a + b


print(add(2, 3))