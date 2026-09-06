class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Student: {self.name}, Marks: {self.marks}")

def average_marks(students):
    return sum(s.marks for s in students) / len(students)

students = [Student("Ali", 85), Student("Sara", 90), Student("Shan", 78)]

for s in students:
    s.display()

print("Average Marks:", average_marks(students))
