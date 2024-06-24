from functools import wraps


def log(filename):
    '''Декоратор, который будет логировать вызов функции и ее результат в файл или в консоль'''

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                with open(filename, 'a') as f:
                    f.write(f'{func.__name__} ok\n')
                return func(*args, **kwargs)

            except Exception as e:
                error_message = f"{func.__name__} error: {e}. Inputs:{args}, {kwargs}"
                with open(filename, "a") as f:
                    f.write(error_message + "\n")
            return func(*args, **kwargs)

        return wrapper

    return decorator


@log(filename="mylog.txt")
def my_function(x, y):
    return x + y

my_function(1, "2")
