
#Figure 2. Palindromic recognition site
#A DNA string is a reverse palindrome if it is equal to its reverse complement. For instance, GCATGC is a reverse palindrome because its reverse complement is GCATGC. See Figure 2.

#Given: A DNA string of length at most 1 kbp in FASTA format.

#Return: The position and length of every reverse palindrome in the string having length between 4 and 12. You may return these pairs in any order.

from Bio import SeqIO

record = SeqIO.read('rosalind_revp.txt', 'fasta')
frw_seq = str(record.seq)
rev_seq = str(record.seq.complement())

for i in range(len(frw_seq)):
    for j in range(i, len(frw_seq)):
        m = frw_seq[i:j + 1]
        rev_m = rev_seq[i:j + 1]
        if len(m) >= 4 and len(m) <= 12:
            if m == rev_m[::-1]:
                print(i + 1, len(m))
