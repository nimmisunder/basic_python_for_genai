class Fruit:
    def __init__(self,price,quantity):
        self.prices = price
        self.quantitys = quantity
    
    def cost(self):
        return self.prices*self.quantitys
    
fruit1=Fruit(100,5)
print(fruit1.cost())

name="nimmi"
rev=""
for i in name:
    rev=i+rev
    
print(rev)

        