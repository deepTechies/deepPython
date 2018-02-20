# Head first Python
# Page 97


try:	
	data =  open('sketch.txt') 
	for line in data:
			(role, lineSpoken) = line.split(':', 1)
			print(role, end='')
			print(' said: ', end='')
			print(lineSpoken, end='')
	data.close()
except:
	print('The data file is missing!')

