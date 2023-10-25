def my_decorator(func):
    print('Decorator')
    return func

@my_decorator
def my_function():
    print("Hello World!")

# my_function = my_decorator(my_function)

my_function()