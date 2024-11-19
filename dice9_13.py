from random import randint
class Die:
    def __init__(self,side=6):
        self.side = side

    def roll_die(self):
        no = self.side
        nu = randint(1,no)
        print(f"the random no is {nu}")

result  = Die()
i= 1
while (i <= 6):
 result.roll_die()
 i+=1
print("Now it is 10 sided die")
result1  = Die(10)
i= 1
while (i <= 10):
 result1.roll_die()
 i+=1
print("Now it is 20 sided die")
result2  = Die(20)
i= 1
while (i <= 10):
 result2.roll_die()
 i+=1