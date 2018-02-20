# Head first Python
# Page 181

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

#    def gietNameTimes(newFileName):
#        name = getCoachData(newFileName)
#        (personName, personTime) = name.pop(0), name.pop(0)
#        return(personName + 's top times are '+ getTimes(name))

#    print(getNameTimes('james2.txt'))
#    print(getNameTimes('julie2.txt'))
#    print(getNameTimes('mikey2.txt'))
#    print(getNameTimes('sarah2.txt'))

    sarah = getCoachData('sarah2.txt')
    sarahData = {}
    sarahData['name'] = sarah.pop(0)
    sarahData['dob'] = sarah.pop(0)
    sarahData['times'] = sarah
    sarahData['name', 'dob', 'times'] = sarah.pop(0), sarah.pop(0), sarah
    print(sarahData['name'] + 's top times are '+ str(sorted(set([sanitizer.sanitizeString(line) for line in sarahData['times']]))[0:3]))

except IOError as err:
    print('IO Error!' + str(err))



