lists = [["🍀", "🍀", "🍀"], ["🍀", "🍀", "🍀"], ["🍀", "🍀", "🍀"]]

print("Welcome to Place the Rabbit 🐇🌿\n")
print(f"{lists[0]}\n{lists[1]}\n{lists[2]}\n")

user_input = input("Please choose a row and a column: ")

if len(user_input) == 2 and user_input.isdigit():
    row = int(user_input[0])
    column = int(user_input[1])

    if 1 <= row <= 3 and 1 <= column <= 3:
        lists[row - 1][column - 1] = "🐇"
        print("\nHere's the updated field:\n")
        print(f"{lists[0]}\n{lists[1]}\n{lists[2]}")
    else:
        print("❌ Invalid position! Row and column must be from 1 to 3.")
else:
    print("❌ Invalid input! Please enter exactly two digits like 12 or 33.")
