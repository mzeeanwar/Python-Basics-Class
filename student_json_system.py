import json

FILE = "student.json"

# Load existing data
def load_students():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

# Save data
def save_students(students):
    with open(FILE, "w") as f:
        json.dump(students, f, indent=4)

# Add student
def add_student(name, age, marks):
    students = load_students()
    students.append({"name": name, "age": age, "marks": marks})
    save_students(students)
    print("Student added!")

# View students
def view_students():
    students = load_students()
    for s in students:
        print(f"Name: {s['name']}, Age: {s['age']}, Marks: {s['marks']}")

# Update student marks
def update_marks(name, new_marks):
    students = load_students()
    for s in students:
        if s["name"] == name:
            s["marks"] = new_marks
            save_students(students)
            print("Marks updated!")
            return
    print("Student not found!")

# Delete student
def delete_student(name):
    students = load_students()
    students = [s for s in students if s["name"] != name]
    save_students(students)
    print("Student deleted!")

# Menu-driven system
while True:
    print("\n--- Student JSON Management ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Marks")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        n = input("Name: ")
        a = int(input("Age: "))
        m = int(input("Marks: "))
        add_student(n, a, m)
    elif choice == "2":
        view_students()
    elif choice == "3":
        n = input("Enter name: ")
        m = int(input("Enter new marks: "))
        update_marks(n, m)
    elif choice == "4":
        n = input("Enter name: ")
        delete_student(n)
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Invalid choice!")
