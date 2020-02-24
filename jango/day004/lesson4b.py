try:
    x = float(input("Enter X : "))
    # x = int(input("Enter X : "))
    y = float(input("Enter Y : "))
    # y = int(input("Enter Y : "))


    print(x+y)
    print(x-y)
    print(x*y)
    print(x/y)
    print(x%y)
    print(x**y)

except Exception as ex1:
    # print("Type a valid number!!!!!")
    print('Error:',ex1)