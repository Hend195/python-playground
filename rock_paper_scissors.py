import random

# Available choices
choices = ["Rock", "Paper", "Scissors"]

# Emojis
rock = "✊🪨"
paper = "🫱📄"
scissors = "✌️✂️"

# Welcome message
print("Welcome to the Rock, Paper, Scissors game!")
ask = input("Press Enter to continue or type (Help) for the rules: ").capitalize()

if ask == "Help":
    print("""
    ************ RULES ************

    1) You choose and the computer chooses.
    2) Rock smashes Scissors -> Rock wins.
    3) Scissors cut Paper -> Scissors wins.
    4) Paper covers Rock -> Paper wins.
    """)

# User choice
user_input = input("Enter your choice (Rock, Paper, Scissors): ").capitalize()

if user_input not in choices:
    print("❌ Invalid choice. Please run the program again and choose Rock, Paper, or Scissors.")
else:
    computer_input = random.choice(choices)

    # Show choices with emojis
    if user_input == "Rock":
        print(f"\nYou chose: {rock} (Rock)")
    elif user_input == "Paper":
        print(f"\nYou chose: {paper} (Paper)")
    elif user_input == "Scissors":
        print(f"\nYou chose: {scissors} (Scissors)")

    if computer_input == "Rock":
        print(f"Computer chose: {rock} (Rock)")
    elif computer_input == "Paper":
        print(f"Computer chose: {paper} (Paper)")
    elif computer_input == "Scissors":
        print(f"Computer chose: {scissors} (Scissors)")

    # Decide winner
    if user_input == computer_input:
        print("\n🤝 It's a draw!")
    elif (user_input == "Rock" and computer_input == "Scissors") or \
         (user_input == "Scissors" and computer_input == "Paper") or \
         (user_input == "Paper" and computer_input == "Rock"):
        print(f"\n🎉 You won! {user_input} beats {computer_input}.")
    else:
        print("\nYou lost! {computer_input} beats {user_input}.")