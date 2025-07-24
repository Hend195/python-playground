def play_game():
    print("""
                                                  ███████▀▀▀▀▀▀▀▀▀▀▀▀▀███████
                                                  ████▀░░░░░░░░░░░░░░░░░▀████
                                                  ███│░░░░░░░░░░░░░░░░░░░│███
                                                  ██░└┐░░░░░░░░░░░░░░░░░┌┘░██
                                                  ██░░└┐░░░░░░░░░░░░░░░┌┘░░██
                                                  ██░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██
                                                  ██▌░│██████▌░░░▐██████│░▐██
                                                  ███░│▐███▀▀░░▄░░▀▀███▌│░███
                                                  ██▀─┘░░░░░░░▐█▌░░░░░░░└─▀██
                                                  ██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██
                                                  ████▄─┘██▌░░░░░░░▐██└─▄████
                                                  █████░░▐█─┬┬┬┬┬┬┬─█▌░░█████
                                                  ████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████
                                                  █████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████
                                                  ███████▄░░░░░░░░░░░▄███████
                                                  ██████████▄▄▄▄▄▄▄██████████

    ░█──░█ ░█▀▀▀ ░█─── ░█▀▀█ ░█▀▀▀█ ░█▀▄▀█ ░█▀▀▀ 　 ▀▀█▀▀ ░█▀▀▀█ 　 ░█▀▄▀█ ░█──░█ 　 ▀█▀ ░█▀▀▀█ ░█─── ─█▀▀█ ░█▄─░█ ░█▀▀▄ █ 
    ░█░█░█ ░█▀▀▀ ░█─── ░█─── ░█──░█ ░█░█░█ ░█▀▀▀ 　 ─░█── ░█──░█ 　 ░█░█░█ ░█▄▄▄█ 　 ░█─ ─▀▀▀▄▄ ░█─── ░█▄▄█ ░█░█░█ ░█─░█ ▀ 
    ░█▄▀▄█ ░█▄▄▄ ░█▄▄█ ░█▄▄█ ░█▄▄▄█ ░█──░█ ░█▄▄▄ 　 ─░█── ░█▄▄▄█ 　 ░█──░█ ──░█── 　 ▄█▄ ░█▄▄▄█ ░█▄▄█ ░█─░█ ░█──▀█ ░█▄▄▀ ▄
    """)

    print("There are two doors in front of you.\n🚪 A red door and 🚪 a blue door.\n")

    door = input("Which door do you want to open? (red/blue):\n> ").strip().lower()

    if door == "red":
        print("\nGreat! You entered a room. \nYou found three boxes: 🎁 White, 🎁 Black, 🎁 Green.\n")

        box = input("Which box do you open? (white/black/green):\n> ").strip().lower()

        if box == "white":
            print("\nOops! You opened a box filled with snakes! \nGame Over! 🐍🐍🐍")
        elif box == "black":
            print("\nOops! You opened a box filled with spiders! \nGame Over! 🕷️🕸️")
        elif box == "green":
            print("\n🎉 Congratulations! You found the treasure! 💰💰💰")
        else:
            print("\n🚫 Invalid choice! Please choose white, black, or green.")

    elif door == "blue":
        print("\nOops! You chose the crocodile door. \nGame Over! 🐊🐊🐊")

    else:
        print("\n🚫 Invalid choice! Please choose red or blue.")


# Main loop
while True:
    play_game()
    again = input("\n🔁 Do you want to play again? (yes/no):\n> ").strip().lower()
    if again != "yes":
        print("\nThe game ended👋🏝️")
        break
