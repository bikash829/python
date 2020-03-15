class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def sit(self):
        print(self.name.title() + " is now sitting.")
    def roll_over(self):
        """Simulate rolling over in response to a comand."""
        print(self.name.title()+" rolled over!")
myObject = Dog("Djhhhhhh",5)

myObject.sit()
myObject.roll_over()
print(myObject.roll_over.__doc__) 

