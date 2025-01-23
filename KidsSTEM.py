class coffee_item:
        def __init__(self, price_small, brew_type, size):
            self.actual_price = 0
            self.price_small = price_small
            self.price_medium = price_small + .50
            self.price_large = price_small + .75
            self.brew_type = brew_type
            self.size = size
            coffee_size = self.size 
            #This adjusts the 
            match coffee_size: 
              case ("small"):
                    self.actual_price = self.price_small
              case ("medium"):
                      self.actual_price = self.price_medium
              case ("large"):
                      self.actual_price = self.price_large
        def print(self):
              print("Brew Type: " + self.brew_type + "\nSize: " +  self.size + "\nPrice: " + "$"+str(self.actual_price))
"""
coffee_type1 = input("Enter a coffee type/brew to create a coffee object (One example may be \"Espresso\", \"Mocha\", or \"Cappuccino\"): ")
coffee_type2 = input("Enter another coffee type/brew to create a coffee object: ")
coffee_type3 = input("Enter one last coffee type/brew to create a coffee object: ")


class coffee_type1(coffee_item(brew_type=coffee_type1)):
     pass

class coffee_type2(coffee_item(brew_type=coffee_type2)):
      pass

class coffee_type3(coffee_item(brew_type=coffee_type3)):
     pass
"""
     
class Espresso(coffee_item):
     pass
class Frap(coffee_item):
     pass
class Mocha(coffee_item):
     pass
     
def place_order(coffee_item1, coffee_item2, coffee_item3):
      total_cost = coffee_item1.actual_price + coffee_item2.actual_price + coffee_item3.actual_price
      print("Here is your order:\n")
      print("1. Coffee: "+ coffee_item1.brew_type + ", Size: " + coffee_item1.size + ", Price: " + "$"+ str(coffee_item1.actual_price))
      print("2. Coffee: "+ coffee_item2.brew_type + ", Size: " + coffee_item2.size + ", Price: " + "$"+str(coffee_item2.actual_price))
      print("3. Coffee: "+ coffee_item3.brew_type + ", Size: " + coffee_item3.size + ", Price: " + "$"+str(coffee_item3.actual_price))
      print("Total: $" + str(total_cost) +"\n")
      print("Your order is ready!")

item_1 = Espresso(price_small=4.00, brew_type="Espresso", size="medium")
item_2 = Frap(price_small=1.00, brew_type="Frap", size="small")
item_3 = Mocha(price_small=1.50, brew_type="Mocha", size="large")
place_order(item_1, item_2, item_3)