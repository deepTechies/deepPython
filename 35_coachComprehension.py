# Head first Python
# Page 157
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

print(sorted([sanitizer.sanitizeString(line) for line in james]))
print(sorted([sanitizer.sanitizeString(line) for line in julie]))
print(sorted([sanitizer.sanitizeString(line) for line in mikey]))
print(sorted([sanitizer.sanitizeString(line) for line in sarah]))


