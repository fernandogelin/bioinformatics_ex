import Levenshtein
import itertools

infile = open('/Users/fernandogelin/Desktop/infile.txt')
sequence = infile.read()
motif_size = int(raw_input("Enter motif size: "))
max_mismatch = int(raw_input("Enter max mismatch: "))


def find_motif(sequence, motif_size):
    motif_list = [sequence[i:i + motif_size] for i in range(0, len(sequence) - motif_size + 1)]
    return motif_list
    
    
motif_list = find_motif(sequence, motif_size)

def rc(seq):
  basecomplement = {'A':'T', 'C':'G', 'T':'A', 'G':'C'}  # lookup table of complements
  seq = list(seq) # convert sequence string to list
  seq.reverse() # reverse the list
  return ''.join([basecomplement[base] for base in seq])  # create new list of complementary bases and then join it (join makes a string from a list)
  
def apm(sequence, pattern, max_mismatch):
    motif_size = len(pattern)
    list_motif_mism = []
    for i in range(0, len(sequence) - motif_size + 1):
        if Levenshtein.hamming(pattern,sequence[i:i + motif_size]) <= max_mismatch:
            list_motif_mism.append(sequence[i:i + motif_size])
    return list_motif_mism


def find_motif_mistmatches(sequence, motif_list, max_mismatch):
    counts = {}
    for i in range(0, len(motif_list)):
        counts[motif_list[i]] = len(apm(sequence, motif_list[i], max_mismatch))
    dic = {}
    for key, value in sorted(counts.iteritems()):
        dic.setdefault(value, []).append(key)
    return dic

def permutations(characters,length):
    return [''.join(i) for i in itertools.product(characters,repeat=length)]

seq = sequence + rc(sequence)

possibility_list = permutations('ATCG', motif_size)
result = find_motif_mistmatches(seq, possibility_list, max_mismatch)
motifs = result[max(result)]
frequency = max(result)


print " ".join(motifs)




