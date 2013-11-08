peptide = raw_input('Enter peptide sequence: ')

def rotate(strg,n):
    return strg[n:] + strg[:n]
    
def list_pep(peptide):
    list_pep = []
    for i in range(0, len(peptide)):
        new_pep = rotate(peptide, i)
        list_pep.append(new_pep)
    return list_pep
    
peptide_list = list_pep(peptide)

def theoretical_spectrum(peptide_list):
    ts = [0]
    for peptide in peptide_list:
        table_mass = {'G': 57, 'A': 71, 'S': 87, 'P': 97, 'V': 99, 'T': 101, 'C': 103, 'I': 113, 'L': 113, 'N': 114, 'D': 115, 'K': 128, 'Q': 128, 'E': 129, 'M': 131, 'H': 137, 'F': 147, 'R': 156, 'Y': 163, 'W': 186}
        subpeptide = [peptide[i:i+1] for i in range(0, len(peptide))]
        for i in range(0, len(peptide) - len(subpeptide) + 1):
            mass = 0
            for j in range(0, len(subpeptide)):
                mass += table_mass[subpeptide[j]]
                ts.append(mass)
                sort = sorted(ts)
        
    return sort[0:len(ts)-len(peptide_list)+1]
                    
            
print " ".join([str(x) for x in theoretical_spectrum(peptide_list)])