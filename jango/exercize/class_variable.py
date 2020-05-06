# class Something:
#     pi = 3.14
#     def __init__(self,circle,radius):
#         self.circle = circle
#         self.radius = radius

#     def dcircle(self):
#         return self.circle*Something.pi
#     def dradious(self):
#         return self.radius*Something.pi

# something = Something(11,22)

# print(something.dcircle())
# print(something.dradious())


class Laptop:
    discount_laptop =10
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.price = price
        self.laptop_name = f"{brand} {model}"

    def discount(self):
        self.dis = self.price - (self.price/100)*self.discount_laptop
        return self.dis




laptop = Laptop('Lenevo','Ideapad-110',29000)
# Laptop.discount_laptop =20
laptop2 = Laptop('Lenevo','Ideapad-54',290400)
laptop3 = Laptop('Lenevo','Ideapad-345',220300)

# discount for perticular object
laptop4 = Laptop('Lenevo','Ideapad-343',100000)
laptop4.discount_laptop = 30


print(f"Laptop1 brand = {laptop.brand} \nLaptop name = {laptop.laptop_name} \nLaptop Model  = {laptop.model} \nLaptop Price = {laptop.price}")
print(f"Discount price = {laptop.discount()} \n" + 40*"=")
print(f"Laptop brand = {laptop2.brand} \nLaptop name = {laptop2.laptop_name} \nLaptop Model  = {laptop2.model} \nLaptop Price = {laptop2.price}")
print(f"Discount price = {laptop2.discount()}")
print(40*"+")
print(f"Laptop brand = {laptop4.brand} \nLaptop name = {laptop4.laptop_name} \nLaptop Model  = {laptop4.model} \nLaptop Price = {laptop4.price}")
print(f"Discount price = {laptop4.discount()}")
print(laptop.__dict__)