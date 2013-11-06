import Levenshtein


infile = open('/Users/fernandogelin/Desktop/infile.txt')
sequence = infile.read()
#sequence = raw_input("Enter the sequence: ")
pattern = raw_input("Enter pattern to match: ")
motif_size = len(pattern)
max_mismatch = int(raw_input("Enter max mismatch: "))

# creates a list with all motifs of motif_size entered by the user
def find_motif(sequence, motif_size):
    motif_list = [sequence[i:i + motif_size] for i in range(0, len(sequence) - motif_size + 1)]
    return motif_list
    
    
motif_list = find_motif(sequence, motif_size)    

def apm(motif_list, pattern, max_mismatch):
    list_indices = []
    for i in range(0, len(motif_list)):
        if Levenshtein.hamming(pattern,motif_list[i]) <= max_mismatch:
            list_indices.append(i)
    return list_indices
 
print " ".join([str(x) for x in apm(motif_list, pattern, max_mismatch)])