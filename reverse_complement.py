# In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'. Given a nucleotide p, we denote its complementary nucleotide as p. The reverse complement of a string Pattern = p1…pn is the string Pattern = pn … p1 formed by taking the complement of each nucleotide in Pattern, then reversing the resulting string.

# For example, the reverse complement of Pattern = "GTCA" is Pattern = "TGAC".

# Reverse Complement Problem

# Reverse complement a nucleotide pattern.

# Given: A DNA string Pattern.

# Return: Pattern, the reverse complement of Pattern.

seq = raw_input("Enter sequence:")
def reverse_complement (seq):
  basecomplement = {'A':'T', 'C':'G', 'T':'A', 'G':'C'}  # lookup table of complements
  seq = list(seq) # convert sequence string to list
  seq.reverse() # reverse the list
  return ''.join([basecomplement[base] for base in seq])  # create new list of complementary bases and then join it (join makes a string from a list)
  
rev_comp = reverse_complement (seq)
  
print "The reverse complement sequence is: " + rev_comp