# File Handling Example

# Write to file
with open("students.txt", "w") as f:
    f.write("Ali - 85\nSara - 90\nShan - 78\n")

# Read from file
with open("students.txt", "r") as f:
    content = f.read()
    print("File Content:\n", content)

# Append to file
with open("data.txt", "a") as f:
    f.write("New entry added!\n")
