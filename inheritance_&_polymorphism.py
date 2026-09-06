# Inheritance, Encapsulation, Polymorphism

class Student:
    def __init__(self, name, age, grade):
        self.__name = name        # encapsulated (private attribute)
        self.age = age
        self.grade = grade

    def get_name(self):           # getter
        return self.__name

    def display_info(self):
        print(f"Student: {self.__name}, Age: {self.age}, Grade: {self.grade}")

# Subclass Teacher inherits Student
class Teacher(Student):
    def __init__(self, name, age, subject):
        super().__init__(name, age, "N/A")   # call parent constructor
        self.subject = subject

    # Polymorphism: override display_info
    def display_info(self):
        print(f"Teacher: {self.get_name()}, Age: {self.age}, Subject: {self.subject}")

# Create objects
s1 = Student("Sara", 21, "B")
t1 = Teacher("Shan", 35, "Mathematics")

s1.display_info()   # Student version
t1.display_info()   # Teacher version (polymorphic)
