# Head first Python
# Page 76

import os
print(os.getcwd())
print(os.chdir('~/Desktop/data'))
print(os.getcwd())

data =  open('sketch.txt') 
print(data.readline(), end='')
print(data.readline(), end='')

data.seek(0)

for line in data:
	if not line.find(':') == -1:
		print(line, end='')
#	help(line.split)	
		(role, lineSpoken) = line.split(':', 1)
		print(role, end='')
		print(lineSpoken, end='')
data.close()

