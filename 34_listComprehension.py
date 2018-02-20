# Head first Python
# Page 156
import sanitizer

mins = [1, 2, 3]
secs = [i*60 for i in mins]
print(secs)

meters = [1, 10, 2]
feet = [i*3.281 for i in meters]
print(feet)

lower = ["I", "don't", "like", "spam"]
upper = [i.upper() for i in lower]
print(lower)

dirty = ['2-22', '2:22', '2.22']
clean = [sanitizer.sanitizeString(i) for i in dirty]
print(clean)

clean = [float(i) for i in clean]
print(clean)

clean = [float(sanitizer.sanitizeString(i)) for i in dirty]
print(clean)
