# def function(x, y = 7, *args, **kwargs):
#     print(x, y)
#     print(args)
#     print(kwargs)

# function(2, 3, 4, 5 , 'Yolo', xd = 5, yolo = 7)

# def my_function(x, y):
#     print(x, y)

# l = [1, 2]

# my_function(l[0], l[1])
# my_function(*l)

x = (1, 2, 3, 4, 5)

a, b, c, d, e = x
print(a, b, c, d, e)

a, b, *c = x
print(a, b, c)

a, *_ = x
print(a)