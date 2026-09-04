# Student Mark System

students = {}

while True:
    print("\n--- Student Mark System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Marks")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        marks = int(input("Enter marks: "))
        students[name] = marks
        print("Student added!")

    elif choice == "2":
        print("All Students:", students)

    elif choice == "3":
        name = input("Enter student name to update: ")
        if name in students:
            marks = int(input("Enter new marks: "))
            students[name] = marks
            print("Marks updated!")
        else:
            print("Student not found!")

    elif choice == "4":
        name = input("Enter student name to delete: ")
        if name in students:
            del students[name]
            print("Student deleted!")
        else:
            print("Student not found!")

    elif choice == "5":
        print("Exiting...")
        break

    else:
        print("Invalid choice!")
