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
    with open('manOut.txt', 'w') as manFile, open('otherOut.txt', 'w') as otherFile:
        nester.printLol(man, fh=manFile)
        nester.printLol(other, fh=otherFile)
except IOError as err:
    print('File error' + str(err))

