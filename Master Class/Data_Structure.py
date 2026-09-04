# Lists
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")   # Create/Update
print(fruits)
fruits.remove("banana")   # Delete
print(fruits)

# Tuples (immutable)
coordinates = (10, 20)
print("Tuple:", coordinates)

# Sets (unique values)
numbers = {1, 2, 3, 3}
numbers.add(4)
print("Set:", numbers)

# Dictionaries
student = {"name": "Ali", "age": 20}
student["grade"] = "A"   # Add
print(student)
del student["age"]       # Delete
print(student)
