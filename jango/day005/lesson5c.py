while True:
    print("Main Manue")
    print("1.Addition")
    print('2.Substraction')
    print('3.Multification')
    print('4.Division')
    print("5.Exit\n\n")

    mn = input("Enter your selection : ")
    if mn == '1':
        print('Addition\n\n')

    elif mn == '2':
        print('Substration\n\n')

    elif mn == '3':
        print('Multification\n\n')
    
    elif mn == '4':
        print("Division\n\n")

    elif mn == '5':
        break
    else:
        print("Invalid input plese enter a valid number...\n\n")