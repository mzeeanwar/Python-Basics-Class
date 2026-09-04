# For loop example
for i in range(1, 6):
    print("For loop iteration:", i)

# While loop example
count = 1
while count <= 5:
    print("While loop iteration:", count)
    count += 1

# Break and Continue example
for i in range(1, 10):
    if i == 5:
        break   # stops the loop completely
    if i % 2 == 0:
        continue  # skips even numbers
    print("Odd number:", i)
