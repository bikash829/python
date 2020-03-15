class Parrot:
    #class attribute 
    species = "Bird"

    # instance attributes 
    def __init__(self,name,age):
        self.name = name
        self.age = age

# instantiate the Parrot class 
blu = Parrot("Blu",10)
woo = Parrot("Woo",15)


# access the class attribute 

print("Ble is a {}".format(blu.__class__.species))