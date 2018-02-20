# Head first Python
# Page 177

import sanitizer
import os
os.chdir('~/Desktop/data')

try:
    def getCoachData(fileName):
        with open(fileName) as file:  
            fileName = file.readline().strip().split(',')
        return(fileName)

    def getTimes(name):
        return(str(sorted(set([sanitizer.sanitizeString(line) for line in name]))[0:3]))

    def getNameTimes(newFileName):
        name = getCoachData(newFileName)
        (personName, personDOB) = name.pop(0), name.pop(0)
        return(personName + 's top times are '+ getTimes(name))

    print(getNameTimes('james2.txt'))
    print(getNameTimes('julie2.txt'))
    print(getNameTimes('mikey2.txt'))
    print(getNameTimes('sarah2.txt'))

except IOError as err:
    print('IO Error!' + str(err))



