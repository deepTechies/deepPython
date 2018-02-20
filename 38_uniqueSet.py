# Head first Python
# Page 168
import sanitizer

import os
os.chdir('~/Desktop/data')

try:
    with open('james.txt') as jamesFile:
        james = jamesFile.readline().strip().split(',')
    with open('julie.txt') as julieFile:
        julie = julieFile.readline().strip().split(',')
    with open('mikey.txt') as mikeyFile:
        mikey = mikeyFile.readline().strip().split(',')
    with open('sarah.txt') as sarahFile:
        sarah=sarahFile.readline().strip().split(',')
except IOError as err:
    print('IO Error!' + str(err))

print(sorted(set([sanitizer.sanitizeString(line) for line in james]))[0:3])
print(sorted(set([sanitizer.sanitizeString(line) for line in julie])) [0:3])
print(sorted(set([sanitizer.sanitizeString(line) for line in mikey]))[0:3])
print(sorted(set([sanitizer.sanitizeString(line) for line in sarah])) [0:3])


