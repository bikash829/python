#IntroduCing  Lists

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

#Accessing Elements in a List
print(motorcycles[1])

#Updating Elements in a List
motorcycles[0] = 'hero'
print(motorcycles)


motorcycles.append('Mahim')
print(motorcycles)

fruits =[]
print(fruits)

fruits.append('Orange')
fruits.append('Mango')
fruits.append('Banana')
print(fruits)

fruits.insert(1,'Apple')
print(fruits)

print('After Sort :')
fruits.sort()
print(fruits)

print('After Reverse Sort :')
fruits.sort(reverse=True)
print(fruits)

print('After Reverse :')
fruits.reverse()
print(fruits)

print('After Remove :')
fruits.remove('Apple')
print(fruits)

print('After Delete :')
del fruits[0]
print(fruits)

cars = ['bmw', 'audi', 'toyota', 'audi','subaru','audi','cortina']
print('Count Numberer of Occurences :')
print(cars.count('audi'))

print(cars.index('audi'))

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the Original list:")
print(cars)

print("\nTotal Number of car : ",end="")
print(len(cars))

print(cars[0:2])
print(cars[:2])
print(cars[2:4])
print(cars[-1])


print(30*'=')
print(help(fruits.index))

print('\n')	
for x in cars:
	print(x,end="\t")
	
	