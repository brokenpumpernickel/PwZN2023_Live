class AgeDescriptor:
    def __get__(self, instance, owner):
        print('get')
        return instance._age
    def __set__(self, instance, value):
        print('set', value)
        if value < 0:
            instance._age = 0
        else:
            instance._age = value

class Student:
    age = AgeDescriptor()
    
    def __init__(self, age):
        self.age = age
    
    def print_age(self):
        print(self.age)

s1 = Student(40)
s1.age = -30
s1.print_age()
