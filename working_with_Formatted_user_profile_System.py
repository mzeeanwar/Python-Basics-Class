# Formatted User Profile System

profiles = []

while True:
    print("\n--- User Profile System ---")
    print("1. Add Profile")
    print("2. View Profiles")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        age = input("Enter age: ")
        city = input("Enter city: ")

        profile = f"Name: {name}, Age: {age}, City: {city}"
        profiles.append(profile)

        # Save to file
        with open("profiles.txt", "a") as f:
            f.write(profile + "\n")

        print("Profile added!")

    elif choice == "2":
        print("\nAll Profiles:")
        for p in profiles:
            print(p)

    elif choice == "3":
        print("Exiting...")
        break

    else:
        print("Invalid choice!")
