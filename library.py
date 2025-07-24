library = []
wishlist = []

print("""
📚 Welcome to Your Personal Library Tracker! 📖

 ┄┄┄┄┄┄┄✦ . 　⁺ 　 . ✦ . 　⁺ 　 . ✦✩₊˚.⋆📚📖📚⋆⁺₊✧✦ . 　⁺ 　 . ✦ . 　⁺ 　 . ✦┄┄┄┄┄┄┄
""")

# Adding books to library
book = input("Enter the name of a book you own: \n")
if book:
    library.append(book)

book = input("Enter the name of another book you own (or press 'Enter' to skip): \n")
if book:
    library.append(book)

print(f"\n📘 Your Library: {library}\n")

# Adding to wishlist
book = input("Enter the name of a book you wish to have in the future: \n")
if book:
    wishlist.append(book)

book = input("Enter another book you wish to have in the future (or press 'Enter' to skip): \n")
if book:
    wishlist.append(book)

print(f"\n📗 Your Wishlist: {wishlist}\n")

# Moving from wishlist to library
book = input("Enter the name of a book from your wishlist that you've acquired (or press 'Enter' to skip): \n")
if book:
    if book in wishlist:
        wishlist.remove(book)
        library.append(book)
    else:
        print("❌ This book is not in your Wishlist.")

# Donating a book
book = input("Enter the name of a book from your library you wish to donate (or press 'Enter' to skip): \n")
if book:
    if book in library:
        library.remove(book)
        print(f"📤 You donated: {book}")
    else:
        print("❌ This book is not in your Library.")

# Final status
print(f"\n📘 Final Library: {library}")
print(f"📗 Final Wishlist: {wishlist}")
