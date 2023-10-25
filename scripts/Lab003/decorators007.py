# class FunctionObject:
#    def __call__(self, x):
#       print('Hello from function object', x)

# o = FunctionObject()
# o(8)

class ObjectDecorator:
   def __init__(self, func):
      self.func = func
      self.counter = 0

   def __call__(self, *args, **kwargs):
      print('Hello from decorator object', self.counter)
      self.counter += 1
      self.func(*args, **kwargs)

@ObjectDecorator
def my_function():
    print("Hello World!")

my_function()
my_function()
my_function()
my_function()
my_function()
my_function()