# Recall from that different occurrences of a substring can overlap with each other. For example, ATA occurs three times in CGATATATCCATAG.

# Pattern Matching Problem

# Find all occurrences of a pattern in a string.

# Given: Two strings, Pattern and Text.

# Return: All starting positions where Pattern appears as a substring of Text.


def find_all_substring_indices(source, sub):
  start = 0
  indices = set()
  while start < len(source) and source.find(sub, start) > -1:
    indices.add(source.find(sub, start))
    start += 1
  return indices


infile = open('/Users/fernandogelin/Desktop/infile.txt')
source = infile.read()
sub = raw_input("Enter a pattern: ")


my_set = find_all_substring_indices(source, sub)
my_list = sorted(list(my_set))

print " ".join([str(x) for x in my_list])

