Students = {'Ali':18,'Rahim':12,'Karim':22,'Joya':25}
print('All Item : ')
print(Students)
print('Print by key Rahim : ')
print(Students['Rahim'])


Boys = {'Ali':18,'Rahim':12,'Karim':22}
Girls = {'Joya':25}

studentX = Boys.copy()
StudentY = Girls.copy()

print('All Boys : ')

print(dir(studentX))


#We use the method Students.update to 
print('add Sarah to our existing dictionary')
Students.update({"Sarah":9})
print(Students)

print('If exist update dictionary')
Students.update({'Karim':12})
print(Students)

print('Delete by key : ')
del Students['Ali']
print(Students)


print('Print Items : ')
print("Students Name : %s" % Students.items())
print('Convert dic to list : ')
print("Students name : %s " % list(Students.items()))


# print('Print only keys : ')
# for key in Students.keys():
#     print(key)


print('Print only values : ')
for val in Students.values():
    print(val)
    


# Print keys and values 
print("Print Only Key and Values : ")
for key in Students.keys():
    print(key + "-" + str(Students[key]))
