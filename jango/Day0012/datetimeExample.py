import datetime

datetime_object = datetime.datetime.now()
print(datetime_object)




d2 = datetime.date.today()
print(d2)



print(dir(datetime.datetime))


# example 3 : Date object to represent a date 
d3 = datetime.date(2019,4,13)
print(d3)


from datetime import date
a = date(2019,4,13)
print(a)

# Example 4 : Get current date
from datetime import date
d3 = date.now()