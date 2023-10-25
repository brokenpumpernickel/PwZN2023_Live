def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before function call")
        func(*args, **kwargs)
        print("After function call")
    return wrapper

@my_decorator
def my_function(x, y, z):
    print("Hello World!", x + y + z)

# my_function = my_decorator(my_function)

my_function(4, 6, 1)