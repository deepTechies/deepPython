# Head first Python
# Page 121
import os
print(os.chdir('~/Desktop/data'))

try:
    with open('manOut.txt', 'w') as manFile:
        print('man', file=manFile)    
    with open('otherOut.txt', 'w') as otherFile:
        print('other', file=otherFile)
except IOError as err:
    print('File error' + str(err))

