# Object-Oriented Programming Basics

class Student:
    def __init__(self, name, age, grade):   # constructor
        self.name = name
        self.age = age
        self.grade = grade

    def display_info(self):                 # method
        print(f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}")

# Create object
s1 = Student("Zeeshan", 23, "A")
s1.display_info()
