while True:
	print('Main Menu')
	print('1. Addition')
	print('2. Subtraction')
	print('3. Multiplication')
	print('4. Division')
	print('5. Exit')
	mn = input('Enter your selection :')

	x=10
	y=3
	
	if mn=='1':
		print('Addition {}'.format(x+y))
	elif mn=='2':
		print('Subtraction {}'.format(x-y))
	elif mn=='3':
		print('Multiplication {}'.format(x*y))
	elif mn=='4':
		print('Division {}'.format(x/y))
	elif mn=='5':
		break
	else:
		print('Invalid Selection')