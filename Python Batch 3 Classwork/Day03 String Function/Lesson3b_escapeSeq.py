s = "qui\bck \\brown\\ fox \njump \"over\" the lazy\tdog"

print(s)



# Escape Sequence	Description	Example	Output
# \\ 	Prints Backslash 	print "\\" 	\
# \` 	Prints single-quote 	print "\'" 	'
# \" 	Pirnts double quote 	print "\"" 	"
# \a 	ASCII bell makes ringing the bell alert sounds ( eg. xterm ) 	print "\a" 	N/A
# \b 	ASCII backspace ( BS ) removes previous character 	print "ab" + "\b" + "c" 	ac
# \f 	ASCII formfeed ( FF ) 	print "hello\fworld" 	hello
#          world
# \n 	ASCII linefeed ( LF ) 	print "hello\nworld" 	hello
# world
# \N{name} 	Prints a character from the Unicode database 	print u"\N{DAGGER}" 	†
# \r 	ASCII carriage return (CR). Moves all characters after ( CR ) the the beginning of the line while overriding same number of characters moved. 	
# \t 	ASCII horizontal tab (TAB). Prints TAB 	print "\t* hello" 	    * hello
# \t 	ASCII vertical tab (VT). 
