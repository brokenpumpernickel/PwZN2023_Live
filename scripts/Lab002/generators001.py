# def my_generator():
#     yield 'xD'
#     yield 'YOLO'
#     yield 'LOL'

# print(type(my_generator))
# print(type(my_generator()))

# for i in my_generator():
#     print(i)

def my_range(maxiter):
    i = 0
    while i < maxiter:
        yield i, i
        i += 1

for i in my_range(10):
    print(i)

print(list(my_range(10)))