
infile = open('/Users/fernandogelin/Desktop/infile.txt')
genome = infile.read()
interval_L = int(raw_input("Enter the interval (L):"))
motif_size_k = int(raw_input("Enter the motif size (k):"))
number_reps_t = int(raw_input("Enter number of reps (t):"))


# creates a list with all sub_sequences of length = L
def sub_sequence(sequence, sub_seq_length):
    sub_sequence = [sequence[i:i + sub_seq_length] for i in range(0, len(sequence) - sub_seq_length + 1)]
    return sub_sequence

# creates a dictionary with most frequent motifs in each sub_sequence
def stats_motifs(list_motifs):
    stats = {}
    for item in list_motifs:
        stats[item] = stats.get(item, 0) + 1
    return stats

# joins the motifs that occur at the same frequency and returns the most frequent motifs
def count_motifs(motif_dict):
    dict = {}
    for key, value in sorted(motif_dict.iteritems()):
        dict.setdefault(value, []).append(key)
    return dict
    
clump = sub_sequence(genome, interval_L)
matches = set()

# for loop to create a dictionary of motifs of length = k for each sub_sequence of length L
for item in clump:
    motifs = list(sub_sequence(item, motif_size_k))
    freq_motif = count_motifs(stats_motifs(motifs))
    result = freq_motif.get(number_reps_t)
    if result:
        for x in result:
            matches.add(x)

my_list = list(matches)
print " ".join([str(x) for x in my_list])
print len(my_list)
