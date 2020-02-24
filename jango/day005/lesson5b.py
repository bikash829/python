# if test expression:
#     Body of if 

# elif test expression:
#     Body of elif
    
# else:
#     Body of else

while True:
    print('Press 0 for Exit...')
    mn = input('Enter month number : ')

    if mn == '1':
        print("January")

    elif mn =='2':
        print('February')

    elif mn =='3':
        print('March')

    elif mn =='4':
        print('April')

    elif mn =='5':
        print('May')

    elif mn =='6':
        print('June')

    elif mn =='7':
        print('July')

    elif mn =='8':
        print('August')

    elif mn =='9':
        print('Spetember')

    elif mn == '10':
        print('October')

    elif mn == '11':
        print('November')

    elif mn == '12':
        print('December')

    elif mn == '0':
        break
    else:
        print("Envalid input..please try again..")

