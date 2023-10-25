from functools import wraps

def my_decorator(func = None, x = 6, y = 8):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print("Before function call", x, y)
            func(*args, **kwargs)
            print("After function call", x, y)
        return wrapper
    if func is None:
        return decorator
    else:
        return decorator(func)

@my_decorator(x = 1, y = 2)
def my_function(x, y, z):
    print("Hello World!", x + y + z)

# my_function = my_decorator(x, y, z, e)(my_function)

my_function(4, 6, 1)
print(my_function.__name__)