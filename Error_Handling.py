# Simple Error Handling

try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
except ValueError:
    print("Error: Invalid input, please enter a number.")
# Error Logging Example
except Exception as e:
    print("An error occurred:", e)
    with open("error_log.txt", "a") as log:
        log.write(f"Error: {e}\n")
