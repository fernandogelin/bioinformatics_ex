# skew diagram
# EXERCISE BREAK: Give all values of Skew(Prefixi (GAGCCACCGCGATA)) for i ranging from 0 to 14.

# Sample Input:
#     CATGGGCATCGGCCATACGCC

# Sample Output:
#     0 -1 -1 -1 0 1 2 1 1 1 0 1 2 1 0 0 0 0 -1 0 -1 -2


sequence = raw_input("Sequence:")

skew_values = {'A': 0, 'C': -1, 'T': 0, 'G': 1}  # lookup skew values for each base
skew = [0]
for base in sequence:
    skew.append(skew_values[base] + skew[-1])
        

print " ".join([str(x) for x in skew])

