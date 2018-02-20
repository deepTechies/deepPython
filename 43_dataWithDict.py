# Head first Python
# Page 185

import sanitizer
import os
os.chdir('~/Desktop/data')
try:
    def getCoachData(fileName):
        with open(fileName) as file:  
            fileName = file.readline().strip().split(',')
        personData = {}
        personData['name'] = fileName.pop(0)
        personData['dob'] = fileName.pop(0)
        personData['times'] = fileName
        getTimes = str(sorted(set([sanitizer.sanitizeString(line) for line in personData['times']]))[0:3])
        return(personData['name'] + '\'s top times are '+ getTimes)

    print(getCoachData('james2.txt'))
    print(getCoachData('julie2.txt'))
    print(getCoachData('mikey2.txt'))
    print(getCoachData('sarah2.txt'))

except IOError as err:
    print('IO Error!' + str(err))



