# Head first Python
# Page 151
import sanitizer

import os
os.chdir('~/Desktop/data')

# Define function
#def sanitize(timeString):
#    if '-' in timeString:
#        splitter = '-'
#    elif ':' in timeString:
#        splitter = ':'
#    else:
#        return(timeString)
#    (mins, secs) = timeString.split(splitter)
#    return(mins + '.' + secs)

# The main code

with open('james.txt') as jamesFile:
    james = jamesFile.readline().strip().split(',')
with open('julie.txt') as julieFile:
    julie = julieFile.readline().strip().split(',')
with open('mikey.txt') as mikeyFile:
    mikey = mikeyFile.readline().strip().split(',')
with open('sarah.txt') as sarahFile:
    sarah=sarahFile.readline().strip().split(',')

newJames = []
newJulie = []
newMikey = []
newSarah = []
for line in james:
    newJames.append(sanitizer.sanitizeString(line))
for line in julie:
    newJulie.append(sanitizer.sanitizeString(line))
for line in mikey:
    newMikey.append(sanitizer.sanitizeString(line))
for line in sarah:
    newSarah.append(sanitizer.sanitizeString(line))
print(sorted(newJames))
print(sorted(newJulie))
print(sorted(newMikey))
print(sorted(newSarah))

