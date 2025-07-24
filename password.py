correct_pass = "A0B0C0"
attempts = 3

while attempts > 0:
    password = input("Enter The Password: \n")
    if password == correct_pass:
        print("Access granted! \nWelcome 💻")
        break
    else:
        attempts -= 1
        print(f"Incorrect Password! You have {attempts} attempt(s) left, try again.\n")

if attempts == 0:
    print("❌ Access denied. Please try again later.")
