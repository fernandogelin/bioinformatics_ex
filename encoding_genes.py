import itertools
infile = open('/Users/fernandogelin/Desktop/infile.txt')
seq = infile.read()


protein = raw_input('Enter the protein sequence: ')


def translation(seq):
    list_codons = [seq[i:i+3] for i in range(0, len(seq), 3)]
    aa_table = {'AAA': 'K', 'AAC': 'N', 'AAG': 'K', 'AAT': 'N', 'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACT': 'T', 'AGA': 'R', 'AGC': 'S', 'AGG': 'R', 'AGT': 'S', 'ATA': 'I', 'ATC': 'I', 'ATG': 'M', 'ATT': 'I', 'CAA': 'Q', 'CAC': 'H', 'CAG': 'Q', 'CAT': 'H', 'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCT': 'P', 'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGT': 'R', 'CTA': 'L', 'CTC': 'L', 'CTG': 'L', 'CTT': 'L', 'GAA': 'E', 'GAC': 'D', 'GAG': 'E', 'GAT': 'D', 'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A', 'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGT': 'G', 'GTA': 'V', 'GTC': 'V', 'GTG': 'V', 'GTT': 'V', 'TAA': '',  'TAC': 'Y', 'TAG': '',  'TAT': 'Y', 'TCA': 'S', 'TCC': 'S', 'TCG': 'S', 'TCT': 'S', 'TGA': '', 'TGC': 'C', 'TGG': 'W','TGT': 'C', 'TTA': 'L', 'TTC': 'F', 'TTG':'L','TTT': 'F'}
    return ''.join([aa_table[codon] for codon in list_codons])
    
def rc(seq):
  basecomplement = {'A':'T', 'C':'G', 'T':'A', 'G':'C'}  # lookup table of complements
  seq = list(seq) # convert sequence string to list
  seq.reverse() # reverse the list
  return ''.join([basecomplement[base] for base in seq])  # create new list of complementary bases and then join it (join makes a string from a list)
    
def find_encoding_genes(sequence, prodein):
    gene_list = []
    for i in range(0, len(sequence) - (len(protein)*3) + 1):
        if translation(sequence[i:i + len(protein)*3]) == protein:
            gene_list.append(sequence[i:i + (len(protein)*3)])
        elif translation(rc(sequence[i:i + len(protein)*3])) == protein:
            gene_list.append(sequence[i:i + (len(protein)*3)])   
    return gene_list

    
print " ".join(find_encoding_genes(seq, protein))