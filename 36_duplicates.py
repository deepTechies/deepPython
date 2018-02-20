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
uniqueJames = []
for i in james:
    if i not in uniqueJames:
        uniqueJames.append(i)
print(uniqueJames[0:3])

julie = sorted([sanitizer.sanitizeString(line) for line in julie])
uniqueJulie = []
for i in julie:
    if i not in uniqueJulie:
        uniqueJulie.append(i)
print(uniqueJulie[0:3])

mikey = sorted([sanitizer.sanitizeString(line) for line in mikey])
uniqueMikey = []
for i in mikey:
    if i not in uniqueMikey:
        uniqueMikey.append(i)
print(uniqueMikey[0:3])

sarah = sorted([sanitizer.sanitizeString(line) for line in sarah])
uniqueSarah = []
for i in sarah:
    if i not in uniqueSarah:
        uniqueSarah.append(i)
print(uniqueSarah[0:3])


