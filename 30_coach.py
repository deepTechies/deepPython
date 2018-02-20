# Head first Python
# Page 142

import os
os.chdir('~/Desktop/data')

with open('james.txt') as jamesFile:
    james = jamesFile.readline().strip().split(',')
    print(james)
with open('julie.txt') as julieFile:
    julie = julieFile.readline().strip().split(',')
    print(julie)
with open('mikey.txt') as mikeyFile:
    mikey = mikeyFile.readline().strip().split(',')
    print(mikey)
with open('sarah.txt') as sarahFile:
    sarah=sarahFile.readline().strip().split(',')
    print(sarah)


