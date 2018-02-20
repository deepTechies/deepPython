# Head first Python
# Page 161
import sanitizer

import os
os.chdir('~/Desktop/data')

with open('james.txt') as jamesFile:
    james = jamesFile.readline().strip().split(',')
with open('julie.txt') as julieFile:
    julie = julieFile.readline().strip().split(',')
with open('mikey.txt') as mikeyFile:
    mikey = mikeyFile.readline().strip().split(',')
with open('sarah.txt') as sarahFile:
    sarah=sarahFile.readline().strip().split(',')

james = sorted([sanitizer.sanitizeString(line) for line in james])
print(sorted(set(james))[0:3])

julie = sorted([sanitizer.sanitizeString(line) for line in julie])
print(sorted(set(julie))[0:3])

mikey = sorted([sanitizer.sanitizeString(line) for line in mikey])
print(sorted(set(mikey))[0:3])

sarah = sorted([sanitizer.sanitizeString(line) for line in sarah])
print(sorted(set(sarah))[0:3])

