'''(string, int, int, int) -> tuple of strings with len(k)'''

 # Given: A string 'd', and integers k, L, and t.
 # Return: All distinct k-mers forming (L, t)-clumps in Genome.

infile = open('/Users/fernandogelin/Desktop/infile.txt')
d = infile.read()
k = 9
L = 500
t = 3

window = '' 
w = 0
m = {}
for j in range(len(d)-L+1):           
    window = d[w:w+L]                                        # creats a window of size L
    w = w + 1                                                # and loops over d
    c = {}                                                   # sets c to an empty dictionary
    for i in range(len(window)-k+1):                         # loops over window 
        key = window[i:i+k]                                  # sets the keys to the length of the kmers
        c[key] = c.get(key,0)+1                              # adds the key to {c} at value one
        if c[key] == t:                                      # if the key = t                 
            m[key] = t                                       # adds the key pair to m             
print " ".join(item[0] for item in m.items() if item[1] == t)
                                                             # loops over each item, key:value pair, in m
                                                             # and makes 'item' a 2 item tuple. ie;('c3', 3)
                                                             # then joins the key, item[0], to the return
                                                             # if the value, item[1], is = t. then separates 
                                                             # by a space, " ".
                                                             
