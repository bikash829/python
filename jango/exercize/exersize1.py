
# class Bird: 
#     def __init__(self,name,canSwim,canFly):
#         self.name= name
#         self.canSwim = canSwim
#         self.canFly = canFly
# bird = Bird("Crow","Can't swim",'can fly')
# print(f"It's a {bird.name.lower()}. It {bird.canSwim.lower()} but it {bird.canFly.lower()}.")


class Birds: 
    def fly(self):
        print("Birds can fly..")

    def swim(self):
        print("Birds can't sweim.")

class Animal:
    def fly(self):
        print("Animal can't fly")
    def swim(self):
        print("Animal can swim")

def Ploy(peramiter):
    peramiter.fly()
    peramiter.swim()


bird = Birds()
animal = Animal()

Ploy(bird)
Ploy(animal)
