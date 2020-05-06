class Laptop:
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.price = price
        self.laptop_name = f"{brand} {model}"

    def discount(self,dis):
        self.dis = (self.price/100)*dis
        return self.dis




laptop = Laptop('Lenevo','Ideapad-110',29000)
laptop2 = Laptop('Lenevo','Ideapad-54',290400)
laptop3 = Laptop('Lenevo','Ideapad-345',220300)
laptop4 = Laptop('Lenevo','Ideapad-343',100000)

print(f"Laptop brand = {laptop.brand} \nLaptop name = {laptop.laptop_name} \nLaptop Model  = {laptop.model} \nLaptop Price = {laptop.price}")
print(f"Price discount = {laptop.discount(40)}")
print(f"Laptop brand = {laptop2.brand} \nLaptop name = {laptop2.laptop_name} \nLaptop Model  = {laptop2.model} \nLaptop Price = {laptop2.price}")
print(f"Price discount = {laptop2.discount(40)}")