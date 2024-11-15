class Users:
    def __init__(self,first_name ,last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def describe_user(self):
        print(f"{self.first_name} {self.last_name} is {self.age} years old")
    def greet_user(self):
        print(f"{self.first_name} Hey how r u, welcome")

class Admin(Users):
    def __init__(self, first_name, last_name, age):
        super().__init__(first_name, last_name, age)
        self.privileges=['can add post','can delete post','can ban post']

    def show_privileges(self):
        print(f"{self.privileges} are admin's priviliges")

user_admin=Admin('Abc','Def',30)
user_admin.show_privileges()