class Parrot:
    def fly(self):
        print("Parrot can fly")


    def swim(self):
        print("Parrot can't swim")


class Penguin:
    def fly(self):
        print("Penguin can't fly")

    def swim(self):
        print("Parrot can swim")

# Common interface
def flying_test(obj):
    obj.fly()


#instantiate objects
blu = Parrot()
peggy = Penguin()


#passing the object 
flying_test(blu)
flying_test(peggy)