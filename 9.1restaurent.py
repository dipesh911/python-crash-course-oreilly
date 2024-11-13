class Restaurant:
    def __init__(self,name,cuisine):
     self.name = name
     self.cuisine = cuisine
    
    def describe_restaurant(self):
       print(f"{self.name} is name")
       print(f"{self.name} is {self.cuisine} type")

    def open_restaurant(self):
       print(f"{self.name} is open")
       
myRest = Restaurant('Haldiram','Indian')
DrishiRest=Restaurant('Mcd','US')

myRest.describe_restaurant()
myRest.open_restaurant()
DrishiRest.describe_restaurant()
DrishiRest.open_restaurant()
