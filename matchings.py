# A-U and G-C pairs can be represented as two bipartite subgraphs,
# Then maximum number of perfect matchings would be the number of matchings in the first subgraph multiplied by that of the second subgraph
# Factorial method is used as this problem is combinatorial, as first node (for instance, G) can pait with n complementary nodes (for instance, C), the second node can only pair with (n-1) nodes, etc.

#The solution depends of which base has more counts, if there are n Gs and m Cs, and n>m, there will be m matchings with (n-m) subset . The are n!/(n-m)!  of G-C pairs in this case. Same applies to A-U pairs


from Bio import SeqIO
from math import factorial

def comb(n,m):
    return factorial(n) // factorial(n-m)
sequence = []

with open("rosalind_mmch (6).txt", 'r') as handle:
    for record in SeqIO.parse(handle, 'fasta'):
        sequence.append(str(record.seq))

s = sequence[0]

A,U,C,G = s.count('A'), s.count('U'), s.count('C'), s.count('G')
minAU,maxAU = sorted([A,U])
minGC,maxGC = sorted([C,G])

AU_pairs = comb(maxAU, minAU)
GC_pairs = comb(maxGC, minGC)

print(int(AU_pairs*GC_pairs))

