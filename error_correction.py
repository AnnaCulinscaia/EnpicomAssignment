from Bio import SeqIO
from Bio.Seq import Seq

complement = {"A": "T", "T": "A", "C": "G", "G": "C"}


# Calculating Hamming Distance Function
def hamming(s1, s2):
    return sum(s1 != s2 for s1, s2 in zip(s1, s2))


if __name__ == "__main__":

    reads = []
    with open("rosalind_corr.txt", 'r') as handle:
        for record in SeqIO.parse(handle, 'fasta'):
            reads.append(str(record.seq))

    correct_reads = []
    incorrect_reads = []

    # Generate a list of reads + reverse reads
    reads_complimented = ["".join(complement.get(base, base) for base in reversed(read)) for read in reads] + reads
    # Determine correct and incorrect reads
    correct_reads = set([read for read in reads_complimented if reads_complimented.count(read) > 1])
    incorrect_reads = set(reads) - correct_reads

    # Printing the incorrect reads with corrected ones
    with open("answer.txt", 'a') as f:
        for read in incorrect_reads:
            print("%s->%s\n" % (read, [corrected for corrected in correct_reads if hamming(corrected, read) == 1][0]),
                  file=f)