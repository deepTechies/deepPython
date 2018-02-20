# Head first Python
# From the page 29 and 39

""" This is the “nester.py" module, and it provides one function called
print_lol() which prints lists that may or may not include nested lists."""

movies = ["The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91,
         ["Graham Chapman",
         ["Michael Palin", "John Cleese", "Terry Gilliam", "Eric Idle", "Terry Jones"]]]


""" This function takes a positional argument called “the_list", which is any
Python list (of, possibly, nested lists). Each data item in the provided list
is (recursively) printed to the screen on its own line."""

def printLol(theList):
	for i in theList:
		if isinstance(i, list):
			printLol(i)	
		else:
			print(i)
	
printLol(movies)

