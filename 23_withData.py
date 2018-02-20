# Head first Python
# Page 120
import os
print(os.chdir('~/Desktop/data'))

try:
    with open('missing.text', 'w') as data:
        print('its...', file=data)
except IOError as err:
    print('File error' + str(err))
