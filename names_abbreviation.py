names = input("Enter first name and last name of your friends (separated by commas): \n").split(", ")
abbreviated_names = []

for name in names:
    full_name = name.strip().split()
    
    if len(full_name) < 2:
        print(f"⚠️ Skipping invalid entry: '{name}' (needs first and last name)")
        continue
    first_name = full_name[0]
    last_name = full_name[1]
    abbreviation = f"{first_name[0].upper()}.{last_name[0].upper()}."
    abbreviated_names.append(abbreviation)

print("\nAbbreviated Names:")
for i in range(len(abbreviated_names)):
    print(names[i])
    print(abbreviated_names[i])
    print()
