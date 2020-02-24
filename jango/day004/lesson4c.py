# input first name and last name which will show full name 


fname = str(input("Enter your first name : "))
lname = str(input("Enter your last name : "))

message = str(input("Write your message please : "))


print("Hello, {1} {0}. {2}".format(fname,lname,message))

