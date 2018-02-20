# Head first Python
# From the page 42, 127

import sys
def printLol(theList, indent=False, level=0, fh=sys.stdout):
    for i in theList:
        if isinstance(i, list):
            printLol(i, indent, level+1, fh)
        else:
            if indent:
                for tabStop in range(level):
                    print("\t", end = '', file=fh)
            print(i, file=fh)
