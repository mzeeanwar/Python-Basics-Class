import json

FILE = "profiles.json"

class Profile:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def format(self):
        return {"name": self.name, "age": self.age, "city": self.city}

def save_profile(profile):
    try:
        with open(FILE, "r") as f:
            profiles = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        profiles = []

    profiles.append(profile.format())
    with open(FILE, "w") as f:
        json.dump(profiles, f, indent=4)

# Example usage
p1 = Profile("Zeeshan", 23, "Gujranwala")
save_profile(p1)
print("Profile saved successfully!")
