

from Bio import SeqIO
from math import factorial

def comb(n,m):
    return factorial(n) // factorial(n-m)
sequence = []

with open("rosalind_mmch.txt", 'r') as handle:
    for record in SeqIO.parse(handle, 'fasta'):
        sequence.append(str(record.seq))

s = sequence[0]

#Determining which base in purine and pirimidine pairs is in excess
A,U,C,G = s.count('A'), s.count('U'), s.count('C'), s.count('G')
minAU,maxAU = sorted([A,U])
minGC,maxGC = sorted([C,G])


AU_pairs = comb(maxAU, minAU)
GC_pairs = comb(maxGC, minGC)

print(int(AU_pairs*GC_pairs))

