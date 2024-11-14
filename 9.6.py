class Restaurant:
    def __init__(self,name,cuisine):
     self.name = name
     self.cuisine = cuisine
    
    def describe_restaurant(self):
       print(f"{self.name} is name")
       print(f"{self.name} is {self.cuisine} type")

    def open_restaurant(self):
       print(f"{self.name} is open")

class IceCreamStand(Restaurant):
   def __init__(self,name,cuisine):
     self.name = name
     super().__init__(name,cuisine)
     self.flavor=['vanilla','butterscotch']

   def flavors(self):
      print(f"Flavors are : ")
      for flavor in self.flavor:
         print(flavor)

myIce = IceCreamStand('McD','US')
myIce.describe_restaurant()
myIce.flavors()