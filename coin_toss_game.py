import random

print("\nWelcome to the coin toss game!\n")

# Toss result: 1 -> HEADS, 2 -> TAILS
coin_result = {1: "HEADS", 2: "TAILS"}
random_number = random.randint(1, 2)
computer_toss = coin_result[random_number]

user_input = input("Please type Heads or Tails: \n").upper()

if user_input in ["HEADS", "TAILS"]:
    if user_input == computer_toss:
        print(f"Perfect answer! 🥳 It was really {user_input}")
    else:
        print(f"Oops! Wrong answer! ❌\nThe Computer's toss result was: {computer_toss}😆")
else:
    print("⚠️ Invalid input, please try again.")

