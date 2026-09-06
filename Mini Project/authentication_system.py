import json

FILE = "student.json"

def login(email, password):
    try:
        with open(FILE, "r") as f:
            users = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        print("No users registered yet!")
        return

    for user in users:
        if user["email"] == email and user["password"] == password:
            print("Login successful! Welcome,", user["name"])
            return
    print("Login failed! Invalid credentials.")

# Example usage
login("ali@example.com", "secure123")
