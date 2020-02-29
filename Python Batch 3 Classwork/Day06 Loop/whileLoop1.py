"""
init variable
while condition:
    Statements
       ...
"""

i=1
while i<=5 :
	print(i,end='\t')
	#i = i+1
	i += 1
	
############################

start = int( input('Enter Start Value : '))
stop  = int(input('Enter Stop Value : '))

i=start
while i<=stop :
	print(i,end='\t')
	i += 1

##########################

#Letting the User Choose When to Quit
message = ""
while message != 'quit':
    message = input('Enter a message :')
    print(message)
	
##########################
	
msg = ""
while True:
	msg = input('Enter a message :')
	if msg == 'x':
		break
	print(msg)	
	

##########################

msg = ""
active=True
while active:
	msg = input('Enter your message :')
	if msg == 'x':
		active=False
	else:
		print(msg)	

##########################

n = 0
while n < 10:
    n += 1
    if n % 2 == 0:
        continue
    
    print(n)
	
##########################

#simple fibonacci series
#the sum of two elements defines the next set

a=0
b=1
while b < 50:
	print(b, end=' ')
	a=b
	b=a+b


##########################

#simple fibonacci series
# the sum of two elements defines the next set

a, b = 0, 1
while b < 50:
	print(b, end=' ')
	a, b = b, a + b
				
				