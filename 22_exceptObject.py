# Head first Python
# Page 118

try:
    data = open('missing.text')
    print(data.readline(), end='')
except IOError as err:
    print('File error' + str(err))
finally:
    if 'data' in locals():
        data.close()
