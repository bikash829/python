# if test expression:
#     statement(s)


# Python if.....elif...else Statement
# Syntax of if....elif.....else

# if test expression:
#     Body of if 

# elif test expression:
#     Body of elif
    
# else:
#     Body of else
    

# #display odd numbers betweeen 0 to 100
x = int(input("Please enter a numeric value : "))
if x % 2 != 0:
    print("The number is Odd",end= '\t')

else:
    print('The number is Even',end = '\t')