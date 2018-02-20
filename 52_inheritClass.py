# Head first Python
# Page 207

import sanitizer
import os
os.chdir('~/Desktop/data')
class AthleteList(list):
    def __init__(self, a_name, a_dob=None, a_times=[]):
            list.__init__([])
            self.name = a_name
            self.dob = a_dob
            self.extend(a_times)
    def top3(self):
        return(sorted(set([sanitizer.sanitizeString(line) for line in self]))[0:3])

def getCoachData(fileName):
    try:
        with open(fileName) as file:  
            personData = file.readline().strip().split(',')
        person = Athlete(personData.pop(0), personData.pop(0), personData)
        return(person.name + "\'s top three times are: " + str(person.top3()))

    except IOError as err:
        print('IO Error!' + str(err))
        return(None)

vera = AthleteList('Vera Vi')
vera.append('1.31')
print(vera.top3())
vera.extend(['2.22', '2-22', '3.1'])
print(vera.top3())

