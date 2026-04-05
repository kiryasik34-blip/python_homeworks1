def log_decorator(func):
    def wrapper(login):
        print(f"Вызов функции: {func.__name__}")
        return func(login)
    return wrapper


@log_decorator
def validate_login(login):

    # 1. Проверка длины
    if len(login) < 5:
        return "Ошибка: слишком короткий логин"

    # 2. Проверка на латиницу + цифры
    for ch in login:
        if not (ch.isascii() and ch.isalnum()):
            return "Ошибка: только латиница и цифры"

    return "Логин валидный"


login = input("Введите логин: ")
print(validate_login(login))