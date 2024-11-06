while(True):
    Name = input("What is your name: ")
    age = float(input(f"Hi, {Name} What is your age: "))
    if age < 3:
        print(f"Congrats! {Name} your ticket is free")
    # elif  3 <= age <= 12:
    elif age < 12 >= 3:
        print(f"{Name} your ticket is 10$")
    elif age >= 12:
        print(f"{Name} your ticket is 15$")
    quit = input("do you want to quit, press Y else enter ").strip().lower()
    if (quit== "y"):
        exit()