class Calculator:
    def add(self,a,b):
        c = a + b
        return c #"Addition is : " + str(a + b)

    def sub(self,a,b):
        c = a - b
        return c #"Addition is : " + str(a + b)

    def mul(self,a,b):
        c = a * b
        return c #"Addition is : " + str(a + b)

    def div(self,a,b):
        c = a / b
        return c #"Addition is : " + str(a + b)

something = Calculator()

print("Addition is : {0}".format(something.add(1,2)))
print("Multification is : {0}".format(something.mul(1,2)))
print("Substration is : {0}".format(something.sub(1,2)))
print("Divition is : {0}".format(something.div(1,2)))