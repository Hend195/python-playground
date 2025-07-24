done_tasks = []
ongoing_tasks = []
tasks = input("Enter your tasks separated by commas: ").split(", ")
for task in tasks:
    check = input(f"\n{task}\nDid you finish {task} already? (yes/no)\n").lower()
    if check == "yes":
        print("Nice job!")
        done_tasks.append(task)
    else:
        print("Try not to put it off")
        ongoing_tasks.append(task)
    print("-----------------")
ask = input("Dou you want to see your today's progress? (Yes/No)  ").lower()
if ask == "yes":
    print(f"\n                                ******* Done Tasks *******\n\n{done_tasks}\n                                ******* Ongoing Tasks *******\n\n{ongoing_tasks}")
else:
    input("Press Enter to Exit...")