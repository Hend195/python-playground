try:
    num = int(input("Enter a random number: "))
    if num > 0:
        print("The number is Positive")
    elif num == 0:
        print("The number is Zero")
    else:
        print("The number is Negative")
except ValueError:
    print("❌ Invalid input! Please try again and enter a valid number.")
