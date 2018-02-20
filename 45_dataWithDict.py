# Head first Python
# Page 187

import sanitizer
import os
os.chdir('~/Desktop/data')
try:
    def getCoachData(fileName):
        with open(fileName) as file:  
            personData = file.readline().strip().split(',')
        return({'name':personData.pop(0), 'dob': personData.pop(0), 'times': str(sorted(set([sanitizer.sanitizeString(line) for line in personData]))[0:3])})        

    def getAll(fileName):
        person = getCoachData(fileName)
        return(person['name'] + '\'s top times are '+ person['times'])

    print(getAll('james2.txt'))

except IOError as err:
    print('IO Error!' + str(err))



