q = True

while q: 
 try:
     no1 = (input("Enter first no or q to quit : "))
     if no1.lower() == 'q':
        print("Exiting the program.")
        break
     no1 = int(no1)
     no2 = (input("Enter Second no or q to quit : "))
     if no2.lower() == 'q':
        print("Exiting the program.")
        break
     no2 = int(no2)
 except ValueError:
     print("Enter only interger")
 else:
     no3 = no1 + no2
     print(f"Sum of {no1} and {no2} is {no3}")