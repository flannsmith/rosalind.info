
#Problem
#After identifying the exons and introns of an RNA string, we only need to delete the introns and concatenate the exons to form a new string ready for translation.

#Given: A DNA string s (of length at most 1 kbp) and a collection of substrings of s acting as introns. All strings are given in FASTA format.

#Return: A protein string resulting from transcribing and translating the exons of s. (Note: Only one solution will exist for the dataset provided.

from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Alphabet import generic_dna

sequences = []
handle = open('rosalind_splc.txt', 'r')
for record in SeqIO.parse(handle, 'fasta'):
    sequence = ''
    for nt in record.seq:
        sequence += nt
    sequences.append(sequence)
handle.close()

long_seq = sequences[0]
introns = sequences[1:]

for i in range(len(introns)):
    long_seq = long_seq.replace(introns[i], '')

long_seq = Seq(long_seq)
print(long_seq.translate(to_stop=True))
