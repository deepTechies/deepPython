# Head first Python
# Page 123

import os
import sys
import nester
import pickle

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
    with open('manOut.txt', 'wb') as manFile, open('otherOut.txt', 'wb') as otherFile:
        pickle.dump(man, manFile)
        pickle.dump(other, otherFile)
except IOError as err:
    print('File error' + str(err))
except pickle.PickleError as perr:
    print('Picke error:', +str(perr))

# unpickle

newMan = []

try:
    with open('manOut.txt', 'rb') as manFile:
        newMan = pickle.load(manFile)
except IOError as err:
    print('File error: ' + str(err))
except pickle.pickleError as perr:
    print('Pickling error: ' +str(perr))

nester.printLol(newMan)
