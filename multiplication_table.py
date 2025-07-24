print("\n*** Welcome to the multiplication table ***\n")

number = input("Enter a number to see its multiplication table: ")

if number.isdigit():
    number = int(number)
    print(f"\nMultiplication Table for {number}:\n")
    for i in range(1, 11):
        result = number * i
        print(f"{number} * {i} = {result}")
else:
    print("❌ Invalid input. Please enter a valid number.")