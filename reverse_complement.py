seq = raw_input("Enter sequence:")
def reverse_complement (seq):
  basecomplement = {'A':'T', 'C':'G', 'T':'A', 'G':'C'}  # lookup table of complements
  seq = list(seq) # convert sequence string to list
  seq.reverse() # reverse the list
  return ''.join([basecomplement[base] for base in seq])  # create new list of complementary bases and then join it (join makes a string from a list)
  
rev_comp = reverse_complement (seq)
  
print "The reverse complement sequence is: " + rev_comp