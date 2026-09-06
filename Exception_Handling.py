# Multiple Exception Handling

try:
    numbers = [1, 2, 3]
    index = int(input("Enter index: "))
    print("Value:", numbers[index])
except (IndexError, ValueError) as e:
    print("Caught Exception:", e)
