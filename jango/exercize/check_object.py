class Test:
    count = 0
    def __init__(self,brand,model,price):
        Test.count += 1
        self.brand = brand.upper()
        self.model = model.title()
        self.price = price
        self.name = f"{self.brand.title()} {self.model}"
        
    def discount(self):
        pass

test = Test('samsung','galaxy-s2',20000)
test1 = Test('samsung','galaxy-s3',30000)
test2 = Test('samsung','galaxy-s4',40000)
test3 = Test('samsung','galaxy-s5',50000)


print(f"Mobile Brand = {test.brand} \nMobile Model = {test.model} \nMobile Name = {test.name} \nMobile Price = {test.price}")
print(40*"+")
print(f"Mobile Brand = {test1.brand} \nMobile Model = {test1.model} \nMobile Name = {test1.name} \nMobile Price = {test1.price}")
print(40*"+")
print(f"Mobile Brand = {test2.brand} \nMobile Model = {test2.model} \nMobile Name = {test2.name} \nMobile Price = {test2.price}")
print(40*"+")
print(f"Mobile Brand = {test3.brand} \nMobile Model = {test3.model} \nMobile Name = {test3.name} \nMobile Price = {test3.price}")
print(Test.count)