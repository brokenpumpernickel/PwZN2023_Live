def my_decorator(x = 6, y = 8):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print("Before function call", x, y)
            func(*args, **kwargs)
            print("After function call", x, y)
        return wrapper
    return decorator

@my_decorator(1, 2)
def my_function(x, y, z):
    print("Hello World!", x + y + z)

# my_function = my_decorator(x, y, z, e)(my_function)

my_function(4, 6, 1)