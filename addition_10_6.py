try:
    no1 = int(input("Enter first no : "))
    no2 = int(input("Enter Second no : "))
except ValueError:
    print("Enter only interger")
else:
    no3 = no1 + no2
    print(f"Sum of {no1} and {no2} is {no3}")

