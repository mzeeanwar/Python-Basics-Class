# Default arguments
def power(base, exp=2):
    return base ** exp

print(power(4))       # 16 (default exp=2)
print(power(4, 3))    # 64

# *args → variable number of positional arguments
def total_sum(*args):
    return sum(args)

print(total_sum(1, 2, 3, 4, 5))   # 15

# **kwargs → variable number of keyword arguments
def student_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

student_info(name="Zeeshan", age=23, grade="A")
