import time
import sys

if len(sys.argv) < 2:
    print("USAGE: %s <Enter any word>" % sys.argv[0])
    sys.exit(-1)

print('You Entered The Word : %s' % sys.argv[1])
strInp = sys.argv[1].upper();

phoneticDict = { 'A': 'Alfa', 'B': 'Bravo', 'C': 'Charlie', 'D': 'Delta', 'E': 'Echo', 'F': 'Foxtrot', 'G': 'Golf', 'H': 'Hotel', 'I': 'India', 'J': 'Juliett', 'K': 'Kilo', 'L': 'Lima', 'M': 'Mike', 'N': 'November', 'O': 'Oscar', 'P': 'Papa', 'Q': 'Quebec', 'R': 'Romeo', 'S': 'Sierra', 'T': 'Tango', 'U': 'Uniform', 'V': 'Victor', 'W': 'Whiskey', 'X': 'X-ray', 'Y': 'Yankee', 'Z': 'Zulu'}

for x in strInp:
    if(x.isalpha()):
        print phoneticDict[x] + ' - ',
    else:
        print x + ' - ',
