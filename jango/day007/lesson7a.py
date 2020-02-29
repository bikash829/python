motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
#Accessing Elements in a List
print(motorcycles[1])

# Updating Elements in a List
motorcycles[1]= 'Zero'
print(motorcycles)


motorcycles.append('Lebu')
print(motorcycles)


# new collection 
fruits = []
print(fruits)
fruits.append('Orange')
fruits.append('Mango')
fruits.append('Banana')
print(fruits)


# new data add specific place
fruits.insert(1,'Apple')
print(fruits)

print("--------------------Array sorting------------------------")
#array sorting
fruits.sort()
print(fruits)

fruits.sort(reverse=True)
print(fruits)

fruits.reverse()
print(fruits)


# # Remove or delete method 
fruits.remove('Apple')

print(fruits)

# # Delete method 

del fruits[0]
print(fruits)


# new list 
cars = ['bmw','audi','toyota','audi','subaru','audi','cortina']
print('Count Numberer of Occurences')
print(cars.count('audi'))
print(cars.index('audi',2))

#temporary sorting
print("\nHere is the sorted list.")
print(sorted(cars))

print("\nTotal Number of car : ",end="")
print(len(cars))

print(cars[0:2])
print(cars[:2])
print(cars[2:4])
print(cars[-1])


print(dir(cars))


print(30*"==")
print(help(fruits.index))

print('\n')
for x in cars:
    print(x,end="\t")