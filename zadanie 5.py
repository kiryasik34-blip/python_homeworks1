import json
from functools import wraps


def to_json(func): #получается задаем функцию
    @wraps(func) #оборачиваем в пленочку суету в этой функции
    def wrapper(*args, **kwargs): #аргикваргикоргив
        result = func(*args, **kwargs)
        return json.dumps(result) #выводим рез-т в виде джейсона стетхема
    return wrapper


@to_json #тут мы по сути вызваои нашу обертку
def get_data_1():
    return {"penis": 2}

@to_json
def get_data_2():
    return {"noga":41}

print(get_data_1(),get_data_2())