# Head first Python
# Page 150

def sanitizeString(timeString):
	if '-' in timeString:
		splitter = '-'
	elif ':' in timeString:
		splitter = ':'
	else:
		return(timeString)
	(mins, secs) = timeString.split(splitter)
	return(mins + '.' + secs)
