# Head first Python
# Page 97

import os
print(os.chdir('~/Desktop/data'))
	
	data =  open('sketch.txt') 
	for line in data:
			(role, lineSpoken) = line.split(':', 1)
			print(role, end='')
			print(' said: ', end='')
			print(lineSpoken, end='')
	data.close()
else:
	print('The data file is missing!')

