
#Problem
#Either strand of a DNA double helix can serve as the coding strand for RNA transcription. Hence, a given DNA string implies six total reading frames, or ways in which the same region of DNA can be translated into amino acids: three reading frames result from reading the string itself, whereas three more result from reading its reverse complement.

#An open reading frame(ORF) is one which starts from the start codon and ends by stop codon, without any other stop codons in between. Thus, a candidate protein string is derived by translating an open reading frame into amino acids until a stop codon is reached.

#Given: A DNA string s of length at most 1 kbp in FASTA format.

#Return: Every distinct candidate protein string that can be translated from ORFs of s. Strings can be returned in any order.


import re
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Alphabet import generic_dna

record = SeqIO.read('rosalind_orf.txt', 'fasta')
pattern = re.compile(r'(?=(ATG(?:...)*?)(?=TAG|TGA|TAA))')
frw_seq = record.seq
rev_seq = frw_seq.reverse_complement()
sequences = []

for m in re.findall(pattern, str(frw_seq)):
    dna_seq = Seq(m, generic_dna)
    prot_seq = dna_seq.translate()
    if prot_seq not in sequences:
        sequences.append(prot_seq)
for n in re.findall(pattern, str(rev_seq)):
    rev_dna_seq = Seq(n, generic_dna)
    rev_prot_seq = rev_dna_seq.translate()
    if rev_prot_seq not in sequences:
        sequences.append(rev_prot_seq)

for i, s in enumerate(sequences):
    print(s)
