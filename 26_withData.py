# Head first Python
# Page 123

import os
import sys
import nester

# Creates man and other
man = []
other = []
try:
    data = open('~/Desktop/data/sketch.txt')
    for line in data:
        try:
            (role, lineSpoken) = line.split(':', 1)
            lineSpoken = lineSpoken.strip()
            if role == 'Man':
                man.append(lineSpoken)
            elif role == 'Other Man':
                other.append(lineSpoken)
        except ValueError:
            pass
    data.close()
except IOError:
    print('The data file is missing!')

# Prints man and other
os.chdir('~/Desktop/data')
try:
    with open('manOut.txt', 'w') as manFile:
        print(man, file=manFile)
    with open('otherOut.txt', 'w') as otherFile:
        print(other, file=otherFile)
except IOError as err:
    print('File error' + str(err))

# To know how it prints out
#with open('manOut.txt') as manFile:
#    print(manFile.readline())
    
# To print line by line
nester.printLol(man, True, 2)
