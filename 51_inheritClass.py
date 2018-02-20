class namedList(list):
    def __init__(self, a_name):
            list.__init__([])
            self.name = a_name

johnny = namedList("Johan Paul Jones")
print(type(johnny))
print(dir(johnny))

johnny.append("Bass Player")
johnny.extend(['Composer', 'Arranger', 'Musician'])
print(johnny)

for attribute in johnny:
    print(johnny.name + 'is a' + attribute +'.')



