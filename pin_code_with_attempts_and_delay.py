import time

correct_pin = "1234"  # Stored PIN

while True:
    attempts = 5

    while attempts > 0:
        user_input = input("Enter your 4-digit PIN: ")

        if user_input.isdigit() and len(user_input) == 4:
            if user_input == correct_pin:
                print("✅ Access granted! Welcome 💻")
                exit()  # Exit the whole program
            else:
                attempts -= 1
                print(f"\n❌ Incorrect PIN. You have {attempts} attempt(s) left.\n")
        else:
            print("⚠️ Invalid input! Please enter exactly 4 digits.\n")

    # If user runs out of attempts
    print("🚫 You have used all attempts.")
    print("⏱ Please wait 1 minute before trying again.\n")

    for i in range(60, 0, -1):
        print(f"⌛ Time remaining: {i} seconds", end="\r")
        time.sleep(1)

    print("\n🔁 You can try again now!\n")


