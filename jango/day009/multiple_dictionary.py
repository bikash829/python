stu_1 = {
    'id':1,
    'name':'Bikash Chowdhury',
    'batch':'L5-77'
}
stu_2 = {
    'id':2,
    'name':'Mayesha Chowdhury',
    'batch':'L5-77'
}
stu_3 = {
    'id':3,
    'name':'Kazi Chowdhury',
    'batch':'L5-77'
}
stu_4 = {
    'id':4,
    'name':'Nahid Chowdhury',
    'batch':'L5-77'
}
stu_5 = {
    'id':5,
    'name':'Amit Chowdhury',
    'batch':'L5-77'
}
stu_6 = {
    'id':6,
    'name':'Rayhan Chowdhury',
    'batch':'L5-77'
}

print("%-5s %-20s %-10s"%('id','name','batch'))
print("%-5s %-20s %-10s"%(stu_1['id'],stu_1['name'],stu_1['batch']))

# .format function 
print("\n"+"Format Function".center(40,'-')+"\n")
print("{0:6} {1:20} {2:10}".format('id','name','batch'))
print("{0:<6} {1:20} {2:10}".format(stu_1['id'],stu_1['name'],stu_1['batch']))

# Multiple dictionary combine
studentList = [stu_1,stu_2,stu_2,stu_4,stu_5,stu_6]


#Nested dictionary
studentList2 = {
    'something':{
    'id':5,
    'name':'Amit Chowdhury',
    'batch':'L5-77'
},
    'something2':{
    'id':6,
    'name':'Rayhan Chowdhury',
    'batch':'L5-77'
}
}

studentList3 = {'st_info':stu_1,'st_info2':stu_2,'st_info3':stu_3}

print("Multiple dictionary".center(40,'='))
print("{0:6} {1:20} {2:10}".format('id','name','batch'))
print(40*"-")
for data in studentList:
    print("{0:<6} {1:20} {2:10}".format(data['id'],data['name'],data['batch']))