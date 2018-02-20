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

try:
    manOut = open('~/Desktop/data/manOut.txt', 'w')
    otherOut = open('~/Desktop/data/otherOut.txt', 'w')
    print(man, file = manOut)
    print(other, file = otherOut)
    manOut.close()
    otherOut.close()
except IOError:
    print('File error')
