class Users:
    def __init__(self,first_name ,last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def describe_user(self):
        print(f"{self.first_name} {self.last_name} is {self.age} years old")
    def greet_user(self):
        print(f"{self.first_name} Hey how r u, welcome")
        
drishi = Users('Drishi','Jukaria',3)
druhi = Users('Druhi','Jukaria',8)

drishi.describe_user()
drishi.greet_user()

druhi.describe_user()
druhi.greet_user()