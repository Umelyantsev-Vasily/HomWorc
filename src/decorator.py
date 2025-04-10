from functools import wraps


def log(log_fail=None):
    """Декоратор
    log , который автоматически логирует начало и конец выполнения функции,
     а также ее результаты или возникшие ошибки.
     Если filename задан, логи записываются в указанный файл.
    Если filename не задан, логи выводятся в консоль."""

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                # Логирование успешного выполнения
                log_message = f"{func.__name__} ok\n"
                if log_fail:
                    with open(log_fail, "a", encoding="utf-8") as f:
                        f.write(log_message)
                else:
                    print(log_message.strip())
                return result

            except Exception as e:
                # Логирование ошибки
                log_message = f"{func.__name__}, {e}: <<{type(e).__name__}>> " f"Inputs: {args}, {kwargs}\n"
                if log_fail:
                    with open(log_fail, "a", encoding="utf-8") as f:
                        f.write(log_message)
                else:
                    print(log_message.strip())
                raise  # Пробрасываем ошибку дальше

        return wrapper

    return decorator


# Лог положительный в файл
@log("log.txt")
def add(a, b):
    return a + b


add(2, 3)  # Запишет в operations.log: "add ok"


# Лог ошибки в файл
@log("log.txt")
def divide(a, b):
    return a / b


try:
    divide(10, 0)
except ZeroDivisionError:
    pass  # Запишет в operations.log: "divide error: ZeroDivisionError. Inputs: (10, 0), {}"


#
#
# Лог в консоль
@log()  # Без параметра - вывод в консоль
def multiply(x, y):
    return x * y


multiply(3, 4)  # Выведет в консоль: "multiply ok"


# Лог ошибки в консоль
@log()
def divide(a, b):
    return a / b


try:
    divide(10, 0)
except ZeroDivisionError:
    pass  # Запишет в operations.log: "divide error: ZeroDivisionError. Inputs: (10, 0), {}"
