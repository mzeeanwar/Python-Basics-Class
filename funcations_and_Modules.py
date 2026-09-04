# Default arguments
def power(base, exp=2):
    return base ** exp

print(power(5))       # 25 (default exp=2)
print(power(5, 3))    # 125

# *args → variable number of positional arguments
def total_sum(*args):
    return sum(args)

print(total_sum(1, 2, 3, 4))   # 10

# **kwargs → variable number of keyword arguments
def student_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

student_info(name="Sara", age=21, grade="A")
