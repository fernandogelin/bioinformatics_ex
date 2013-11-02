# Minimum Skew Problem: Find a position in a genome minimizing the skew.
#      Input: A DNA string Genome.
#      Output: All integer(s) i minimizing Skew(Prefixi (Text)) among all values of i (from 0 to |Genome|).

# CODE CHALLENGE: Solve the Minimum Skew Problem.

# Sample Input:
#     TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT

# Sample Output:
#     11 24


infile = open('/Users/fernandogelin/Desktop/infile.txt') # read sequence from file
sequence = infile.read()

# sequence = raw_input("Sequence:") # user input

skew_values = {'A': 0, 'C': -1, 'T': 0, 'G': 1}  # lookup skew values for each base
skew = [0]

for i in sequence:
    skew.append(skew_values[i] + skew[-1])

min_skew_list = []
for i in range(0, len(skew)):
    if skew[i] == min(skew):
        min_skew_list.append(i)


print " ".join([str(x) for x in min_skew_list])




    