#without peramiter functon 
def function():
    firstName = "Bikash"
    lastName = "Chowdhury"
    return "{0} {1}".format(firstName,lastName)


# function()
# print(40*'='+'\n'+function())
# print("{0}\n{1}".format(40*'=',function()))

#function with single paramiter
def functionP(value):
    return value

print("{0} \n {1}".format(40*'-',functionP("HI")))


#Multiple peramiter 
def myFunction(wav,name,msg):
    return "{0}, {1}. {2}".format(wav,name,msg)


x = input("Say Hi or Hello : ")
y = input("Mention someone : ")
z = input("Giv a message as you want : ")

print("{0} \n {1}".format(40*'-',myFunction(wav = x,name = y,msg = z)))