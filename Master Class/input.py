# Program: Simple Calculator and Basics

# --- Print messages using print() ---
print("Welcome to the Python Basics Class")
print("This is a simple calculator program")

# --- Read input from the user ---
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# --- Use basic arithmetic operators ---
print("\nArithmetic Operations:")
print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2 if num2 != 0 else "Error: Division by zero")

# --- Simple Calculator Program ---
print("\n--- Calculator Menu ---")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter your choice (1-4): ")

if choice == "1":
    print("Result:", num1 + num2)
elif choice == "2":
    print("Result:", num1 - num2)
elif choice == "3":
    print("Result:", num1 * num2)
elif choice == "4":
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error: Division by zero")
else:
    print("Invalid choice!")
