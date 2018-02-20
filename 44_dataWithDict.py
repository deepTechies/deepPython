# Head first Python
# Page 186

import sanitizer
import os
os.chdir('~/Desktop/data')
try:
    def getCoachData(fileName):
        with open(fileName) as file:  
            personData = file.readline().strip().split(',')
        return({'name':personData.pop(0), 'dob': personData.pop(0), 'times': str(sorted(set([sanitizer.sanitizeString(line) for line in personData]))[0:3])})        

    james = getCoachData('james2.txt')
    print(james['name'] + '\'s top times are '+ james['times'])

except IOError as err:
    print('IO Error!' + str(err))



