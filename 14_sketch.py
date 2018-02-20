# Head first Python
# Page 91

import os
print(os.chdir('~/Desktop/data'))
data =  open('sketch.txt') 

for line in data:
	try:
		(role, lineSpoken) = line.split(':', 1)
		print(role, end='')
		print(' said: ', end='')
		print(lineSpoken, end='')
	except:
		pass
data.close()

