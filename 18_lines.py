# Head first Python
# Page 108
man = []
other = []
try:
    data = open('~/Desktop/data/sketch.txt')
    for line in data:
        try:
            (role, lineSpoken) = line.split(':', 1)
            lineSpoken = lineSpoken.strip()
            if role == 'Man':
                man.append(lineSpoken)
            elif role == 'Other Man':
                other.append(lineSpoken)
        except ValueError:
            pass
    data.close()
except IOError:
    print('The data file is missing!')
print(man)
print(other)

