# Head first Python
# Page 97


try:	
    data =  open('sketch.txt') 
    for line in data:
        try:			
            (role, lineSpoken) = line.split(':', 1)
            print(role, end='')
            print(' said: ', end='')
            print(lineSpoken, end='')
        except ValueError: 
            pass
    data.close()
except IOError:
    print('The data file is missing!')

