import re
import json

FILE = "student.json"

def register_user(name, email, password):
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        print("Invalid email format!")
        return
    if len(password) < 6:
        print("Password must be at least 6 characters!")
        return

    try:
        with open(FILE, "r") as f:
            users = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        users = []

    users.append({"name": name, "email": email, "password": password})

    with open(FILE, "w") as f:
        json.dump(users, f, indent=4)

    print("Registration successful!")

# Example usage
register_user("Ali", "ali@example.com", "secure123")
