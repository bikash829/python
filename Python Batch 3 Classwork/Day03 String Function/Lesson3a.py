s = "   hAve a niCe DAy "

print(s)

print(s.upper()) #
print(s.lower()) #
print(s.capitalize())
print(s.count('A'))
print(s.count('a'))
print(s.upper().count('A'))
print(s.endswith('r')) #
print(s.lower().endswith('y'))
print(s.lower().startswith('h'))
print(s.find('a'))
print(s.find('k'))
print(s.index('v'))
#print(s.index('k'))
print(s.replace('V','U'))
print(s.title())
print(s.swapcase()) #toggle case

#print(help(s.find))
#print(dir(s))
#print(help(s.casefold))
print(s.strip())

print(len(s))
print(len(s.strip()))
print(len(s.rstrip()))
print(len(s.lstrip()))

data = s.split()
print(data)
print(s.join(data))

print("5".isdigit())
print("5".isalpha())
print("25.7".isdecimal())
print(s.center(30))
print(s.center(30,'_'))

print('Nazmul'.casefold() == 'nazmul')
print("225".zfill(5))




