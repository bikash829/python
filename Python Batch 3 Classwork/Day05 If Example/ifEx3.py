while True:
	print('Main Menu')
	print('1. Addition')
	print('2. Subtraction')
	print('3. Multiplication')
	print('4. Division')
	print('5. Exit')
	mn = input('Enter your selection :')

	if mn=='1':
		print('Addition')
	elif mn=='2':
		print('Subtraction')
	elif mn=='3':
		print('Multiplication')
	elif mn=='4':
		print('Division')
	elif mn=='5':
		break
	else:
		print('Invalid Selection')