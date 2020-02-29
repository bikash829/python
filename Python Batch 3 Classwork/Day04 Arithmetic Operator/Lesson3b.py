"""
Arithmetic Operations
======================
Date: 10/10/2019
----------------------
"""

try:
	x= float(input("Enter X : "))
	y= float(input("Enter Y : "))

	print(x+y)
	print(x-y)
	print(x*y)
	print(x/y)
	print(x%y)
	print(x**y)

except Exception as ex1:
	print('Error: ',ex1)
		
