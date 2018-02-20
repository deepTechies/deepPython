# Head first Python
# Page 133

import pickle

with open('myData.pickle', 'wb') as myStoreData:
    pickle.dump([1, 2, "write"], myStoreData)
with open('myData.pickle', 'rb') as myRestoreData:
    myList = pickle.load(myRestoreData)
print(myList)

