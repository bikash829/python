class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model 
        self.year = year
        

    def get_description_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

cars = Car("new make",'new model','new year')

print(cars.get_description_name())