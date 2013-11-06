# Rosalind problems:
# Frequent Words Problem:
# This is the first problem in a collection of "code challenges" to accompany Bioinformatics Algorithms: An Active-Learning Approach by Phillip Compeau & Pavel Pevzner. A full version of this text is hosted on Stepic.

# A k-mer is defined as a string of length k. We define Count(Text, Pattern) as the number of times that a k-mer Pattern appears as a substring of Text. For example,

# Count(ACAACTATGCATACTATCGGGAACTATCCT,ACTAT)=3

# We note that Count(CGATATATCCATAG, ATA) is equal to 3 (not 2) since we should account for overlapping occurrences of Pattern in Text.

# We say that Pattern is a most frequent k-mer in Text if it maximizes Count(Text, Pattern) among all k-mers. For example, "ACTAT" is a most frequent 5-mer in "ACAACTATGCATCACTATCGGGAACTATCCT", and "ATA" is a most frequent 3-mer of "CGATATATCCATAG".

# Find the most frequent k-mers in a string.

# Given: A string Text and an integer k.

# Return: All most frequent k-mers in Text.


# asks the user for the input data
sequence = raw_input("Enter the sequence:")
motif_size = int(raw_input("Enter the motif size:"))

# creates a list with all motifs of motif_size entered by the user
def find_motif(sequence, motif_size):
    motif_list = [sequence[i:i + motif_size] for i in range(0, len(sequence) - motif_size + 1)]
    return motif_list

motif_list = find_motif(sequence, motif_size)

# counts the number of occurance for each motif and creates a dictionary
def count_motif(motif_list):
    stats = {}
    for item in motif_list:
        stats[item] = stats.get(item, 0) + 1
    return stats

motif_dict = count_motif(motif_list)

# joins the motifs that occur at the same frequency and returns the most frequent motifs
def count_motifs(motif_dict):
    dic = {}
    for key, value in sorted(motif_dict.iteritems()):
        dic.setdefault(value, []).append(key)
    return dic

result = count_motifs(motif_dict)
motifs = str(result[max(result)])
frequency = str(max(result))


print "Most frequent motifs: " + motifs
print "Frequency: " + frequency + " times each"

