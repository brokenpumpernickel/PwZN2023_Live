# def function():
#     pass

# class Student:
#     pass

# s1 = Student()
# print(s1, type(s1))

###

# class Student:
#     def __init__(self):
#         print('init student')

# s1 = Student()

###

# class Student:
#     classes = []

#     def __init__(self):
#         print('init student')

# s1 = Student()
# print(s1.classes)

# s1.classes.append('Math')
# s1.classes.append('English')
# s1.classes.append('History')
# print(s1.classes)

# s2 = Student()
# print(s2.classes)

# print(Student.__dict__)
# print(s1.__dict__)

###

# class Student:
#     def __init__(self):
#         self.classes = []
#         print('init student')

# s1 = Student()
# print(s1.classes)

# s1.classes.append('Math')
# s1.classes.append('English')
# s1.classes.append('History')
# print(s1.classes)

# s2 = Student()
# print(s2.classes)

# print(Student.__dict__)
# print(s1.__dict__)

###

class Student:
    pass

s1 = Student()
print(s1.__dict__)
s1.name = 'John'
print(s1.name)
print(s1.__dict__)

###

# class Student:
#     def __init__(self):
#         self.classes = []
#         print('init student')

#     def print_classes(self):
#         print(self.classes)

# s1 = Student()
# s1.classes.append('Math')
# s1.classes.append('English')
# s1.classes.append('History')

# s1.print_classes()
# Student.print_classes(s1)
# #print(Student.__dict__)
# Student.__dict__['print_classes'](s1)

###

class Student:
    def __init__(self):
        self.classes = []
        print('init student')

    def print_classes(self):
        print(self.classes)

    def __getitem__(self, key):
        print(key)
        return 'YOLO'
    
s1 = Student()
print(s1['adasdadasdsada'])

