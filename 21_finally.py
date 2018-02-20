# Head first Python
# Page 118

try:
    data = open('missing.text')
    print(data.readline(), end='')
except IOError:
    print('File error')
finally:
    if 'data' in locals():
        data.close()
