# Head first Python
# Page 199

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
    def addTime(self, timeValue):
        self.times.append(timeValue)
    def addTimes(self, listTimes):
        self.times.extend(listTimes)
def getCoachData(fileName):
    try:
        with open(fileName) as file:  
            personData = file.readline().strip().split(',')
        person = Athlete(personData.pop(0), personData.pop(0), personData)
        return(person.name + "\'s top three times are: " + str(person.top3()))

    except IOError as err:
        print('IO Error!' + str(err))
        return(None)

vera = Athlete('Vera Vi')
vera.addTime('1.31')
print(vera.top3())
vera.addTimes(['2.22', '2-22', '3.1'])
print(vera.top3())

#print(getCoachData('james2.txt'))
#print(getCoachData('julie2.txt'))
#print(getCoachData('mikey2.txt'))
#print(getCoachData('sarah2.txt'))


