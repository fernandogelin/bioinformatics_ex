# We say that position i in k-mers p1 … pk and q1 … qk is a mismatch if pi ≠ qi. For example, CGAAT and CGGAC have two mismatches.

# Approximate Pattern Matching Problem

# Find all approximate occurrences of a pattern in a string.

# Given: Two strings Pattern and Text along with an integer d.

# Return: All positions where Pattern appears in Text with at most d mismatches.

# Sample Dataset

# ATTCTGGA
# CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAATGCCTAGCGGCTTGTGGTTTCTCCTACGCTCC
# 3
# Sample Output

# 6 7 26 27 78


def find_all_substring_indices(source, sub):
  start = 0
  indices = set()
  while start < len(source) and source.find(sub, start) > -1:
    indices.add(source.find(sub, start))
    start += 1
  return indices


infile = open('/Users/fernandogelin/Desktop/infile.txt')
source = infile.read()
sub = raw_input("Enter a pattern:")
mismmatch = raw_input("Mismatches:")


my_set = find_all_substring_indices(source, sub)
my_list = sorted(list(my_set))

print " ".join([str(x) for x in my_list])

