import string
x = ""
user_input = input("Enter a sentence: ")
for letter in user_input:
    if letter not in string.punctuation and letter not in "1234567890":
        x += letter
print(x)