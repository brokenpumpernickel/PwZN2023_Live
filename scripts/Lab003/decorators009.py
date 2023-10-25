# class Student:
#     def __init__(self, age):
#         self.age = age

#     def print_age(self):
#         print(self.age)

# s1 = Student(20)
# s1.age = -30
# s1.print_age()

###

# class Student:
#     def __init__(self, age):
#         self.set_age(age)

#     def get_age(self):
#         print("Getting age")
#         return self._age
#     def set_age(self, age):
#         print("Setting age", age)
#         if age < 0:
#             self._age = 0
#         else:
#             self._age = age

#     def print_age(self):
#         print(self.get_age())

# s1 = Student(20)
# s1.set_age(-30)
# s1.print_age()

class Student:
    def __init__(self, age):
        self.age = age

    @property
    def age(self):
        print("Getting age")
        return self._age
    
    @age.setter
    def age(self, age):
        print("Setting age", age)
        if age < 0:
            self._age = 0
        else:
            self._age = age

    def print_age(self):
        print(self.age)

s1 = Student(20)
s1.age = -30
s1.print_age()