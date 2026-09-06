# Multiplication Table with Exception Handling
try:
    num = int(input("Enter a number: "))
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")
except ValueError:
    print("Invalid input! Please enter a number.")
