import tkinter as tk
from tkinter import messagebox
import random

def choose_person():
    names_input = entry.get()
    names = names_input.split(", ")
    if not names or names == [""]:
        messagebox.showwarning("Input Error", "Please enter names separated by a comma and a space.")
        return
    chosen = random.choice(names)
    messagebox.showinfo("Result 🎉", f"Please ask ({chosen}) to take their wallet out 💳")

# Create main window
window = tk.Tk()
window.title("Who's Wallet? 💸")
window.geometry("400x200")

# Instruction label
label = tk.Label(window, text="Enter names separated by a comma and a space:", font=("Arial", 12))
label.pack(pady=10)

# Input field
entry = tk.Entry(window, width=50)
entry.pack(pady=5)

# Button to choose a person
button = tk.Button(window, text="Who's paying? 🤑", command=choose_person)
button.pack(pady=20)

# Run the application
window.mainloop()
