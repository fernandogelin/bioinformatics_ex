def gen_match(w, d):
    gen = []
    gen_temp_1 = {'':0}
    gen_temp_2 = {}
    letterrange = ['A', 'C', 'G', 'T']
    for i in range(0, len(w)):
        l = w[i]
        for j in range(0, 4):
            l2 = letterrange[j]
            for word in gen_temp_1:
                if (l == l2):
                    gen_temp_2[word + l2] = gen_temp_1[word]
                elif (gen_temp_1[word] < d):
                    gen_temp_2[word + l2] = gen_temp_1[word]+1
        gen_temp_1 = gen_temp_2
        gen_temp_2 = {}
    return gen_temp_1.keys()


def rc(seq):
  basecomplement = {'A':'T', 'C':'G', 'T':'A', 'G':'C'}  # lookup table of complements
  seq = list(seq) # convert sequence string to list
  seq.reverse() # reverse the list
  return ''.join([basecomplement[base] for base in seq])  # create new list of complementary bases and then join it (join makes a string from a list)
 

# Too lazy to read file, so I copy and pasted
seq = raw_input("Enter sequence:")
text = seq + rc(seq) 
d = 3
k = 10
dic = {}
dic_2 = {}
s = ''


# I do a quick frequcncy analysis
for i in range(0, len(text) - k):
    word = text[i:i+k]
    if word not in dic:
        dic[word] = 0
    dic[word] += 1

# For each k-mer existing in dic, find all the "similar k-mers"
# Then put the count in dic_2
for word in dic:
    keylist = gen_match(word, d)
    for key in keylist:
        if (key not in dic_2):
            dic_2[key] = 0
        dic_2[key] += dic[word]

# Find most frequent similar k-mers
sorted_dic = sorted(dic_2, key=dic_2.get, reverse=True)
maxcount = dic_2[sorted_dic[0]]

for key in sorted_dic:
    if (dic_2[key] == maxcount):
        s += key + ' '

print(s)