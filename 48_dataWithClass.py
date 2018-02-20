# Head first Python
# Page 195

import sanitizer
import os
os.chdir('~/Desktop/data')
class Athlete:
    def __init__(self, a_name, a_dob=None, a_times=[]):
            self.name = a_name
            self.dob = a_dob
            self.times = a_times
    def top3(self):
        return(sorted(set([sanitizer.sanitizeString(line) for line in self.times]))[0:3])

try:
    def getCoachData(fileName):
        with open(fileName) as file:  
            personData = file.readline().strip().split(',')
        return(Athlete(personData.pop(0), personData.pop(0), personData))

    person = getCoachData('james2.txt')
    print(person.name + "\'s top three times are: " + str(person.top3()))

except IOError as err:
    print('IO Error!' + str(err))


