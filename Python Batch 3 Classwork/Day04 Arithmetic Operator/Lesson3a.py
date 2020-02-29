s = "The quick\b \"brown\" fox \njump over\t\t\tthe lazy dog"













s = "The quick brown fox jump over the lazy dog"

print(s)

m = "The quick \\brown\\ fox \"jump\" over the lazy dog"
print(m)

# Escape    	Description							Example						Output
# \\ 					Prints Backslash 				print "\\" 						\
# \` 					Prints single-quote 			print "\'" 						'
# \" 					Pirnts double quote 			print "\"" 						"
# \a 					ASCII bell makes ringing 	print "\a" 						N/A
# \b 					ASCII backspace ( BS )  	print "ab" + "\b" + "c" 	ac
# \f 					ASCII formfeed ( FF ) 		print "hello\fworld" 		hello
# \n 					ASCII linefeed ( LF ) 		print "hello\nworld" 		hello 
																										world
# \r 					ASCII carriage return 
# \t 					ASCII horizontal tab 			Prints TAB 	print "\t* hello	hello

