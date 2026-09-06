# File Handling Example

# Create and write to students.txt
with open("students.txt", "w") as f:
    f.write("Ali - 85\n")
    f.write("Sara - 90\n")
    f.write("Zeeshan - 78\n")

# Read from students.txt
with open("students.txt", "r") as f:
    print("Students File Content:\n", f.read())

# Create and append to data.txt
with open("data.txt", "a") as f:
    f.write("New entry added!\n")

# Read from data.txt
with open("data.txt", "r") as f:
    print("Data File Content:\n", f.read())
