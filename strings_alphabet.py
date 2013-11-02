def allstrings2(alphabet, length):
    """Find the list of all strings of 'alphabet' of length 'length'"""

    c = []
    for i in range(length):
        c = [[x]+y for x in alphabet for y in c or [[]]]

    return c
    
infile = open('/Users/fernandogelin/Desktop/infile.txt')
genome = infile.read()

length = int(raw_input("L:"))

print allstrings2(genome, length)