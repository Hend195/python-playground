age = int(input("Enter your age: \n"))

if age >= 18:
    licence = input("Do you have a driver's license? (yes/no): \n").strip().lower()

    if licence == "yes":
        print("✅ Good, you're allowed to drive! 🚗")
    elif licence == "no":
        print("❌ Sorry, you're not allowed to drive without a license.")
    else:
        print("⚠️ Invalid input. Please enter 'yes' or 'no'.")
else:
    print("⛔ Sorry, you're underage. You're not allowed to drive.")
