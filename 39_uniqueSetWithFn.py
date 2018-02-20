# Head first Python
# Page 168
import sanitizer

import os
os.chdir('~/Desktop/data')
try:
    def getCoachData(fileName):
        with open(fileName) as file:  
            fileName = file.readline().strip().split(',')
        return(fileName)

    def printScores(name):
        print(sorted(set([sanitizer.sanitizeString(line) for line in name]))[0:3])

    james = getCoachData('james.txt')
    julie = getCoachData('julie.txt')
    mikey = getCoachData('mikey.txt')
    sarah = getCoachData('sarah.txt')

    printScores(james)
    printScores(julie)
    printScores(mikey)
    printScores(sarah)

except IOError as err:
    print('IO Error!' + str(err))




