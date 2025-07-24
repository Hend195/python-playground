import random
import string

total_length = int(input("Enter the preferred password length \n-> Password length: "))
letters = int(input("Enter the number of letters in the password \n-> Letters count: "))
numbers = int(input("Enter the number of numbers in the password \n-> Numbers count: "))
symbols = int(input("Enter the number of symbols in the password \n-> Symbols count: "))

if total_length != letters + numbers + symbols:
    print("Invalid input. The sum of letters, numbers, and symbols doesn't match the password length.")
else:
    password_chars = []
    password_chars += random.choices(string.ascii_letters, k=letters)
    password_chars += random.choices(string.digits, k=numbers)
    password_chars += random.choices(string.punctuation, k=symbols)

    random.shuffle(password_chars)

    suggested_password = ''.join(password_chars)
    print("\n~~~ Suggested Password ~~~\n" + suggested_password)
