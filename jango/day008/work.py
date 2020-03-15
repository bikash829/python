friendsName = ['Ami','Tmi','oo','ora','onekei']
# friendsName = ('Ami','Tmi','oo','ora','onekei')
print(len(friendsName))


# for x in friendsName:
#     print(x,end = " ")


#home work
students = [
    
    {'id':2,'name':'Kazi','salary':2000},
    {'id':1,'name':'Mayesha Fahmida Era','salary':50000},
    {'id':3,'name':'Bikash','salary':70000},
    {'id':4,'name':'Nahid','salary':6000}
]

print("Id\t name\t\t salary\n")
for listSet in students:
    print("{0}\t {1}\t\t {2}\n".format(listSet["id"],listSet["name"],listSet["salary"]))
print(50*"=")


print("%-3s %-20s %-10s"%("Id","Name","Salary\n" + 38*"-"))
for x in students:
    print("|%-3s %-20s %-10s|"%(x['id'],x['name'],x['salary']))