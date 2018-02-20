# Head first Python
# Page 142

import os
os.chdir('~/Desktop/data')

data = open('james.txt')
james= data.readline().strip().split(',')
print(james)

data = open('julie.txt')
julie= data.readline().strip().split(',')
print(julie)

data = open('mikey.txt')
mickey= data.readline().strip().split(',')
print(mickey)

data = open('sarah.txt')
sarah= data.readline().strip().split(',')
print(sarah)

