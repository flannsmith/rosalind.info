import pandas as pd
# Problem
# Assume you have the protein sequence attached below. It's composed of 800 amino acids.

# Can you find the length of the shortest subsequence that needs to be replaced in order to have all the amino acids equally represented? That means same numbers of "A", "C", "D" and so on.


from Bio.SeqUtils import seq3

#print(seq3(imput, custom_map=None))


#1 step count the amount of each type of amino acid

codons = {
    'UUU': 'F',     'CUU': 'L',     'AUU': 'I',     'GUU': 'V',
    'UUC': 'F',     'CUC': 'L',     'AUC': 'I',     'GUC': 'V',
    'UUA': 'L',     'CUA': 'L',     'AUA': 'I',     'GUA': 'V',
    'UUG': 'L',     'CUG': 'L',     'AUG': 'M',     'GUG': 'V',
    'UCU': 'S',     'CCU': 'P',     'ACU': 'T',     'GCU': 'A',
    'UCC': 'S',     'CCC': 'P',     'ACC': 'T',     'GCC': 'A',
    'UCA': 'S',     'CCA': 'P',     'ACA': 'T',     'GCA': 'A',
    'UCG': 'S',     'CCG': 'P',     'ACG': 'T',     'GCG': 'A',
    'UAU': 'Y',     'CAU': 'H',     'AAU': 'N',     'GAU': 'D',
    'UAC': 'Y',     'CAC': 'H',     'AAC': 'N',     'GAC': 'D',
    'UAA': 'Stop',  'CAA': 'Q',     'AAA': 'K',     'GAA': 'E',
    'UAG': 'Stop',  'CAG': 'Q',     'AAG': 'K',     'GAG': 'E',
    'UGU': 'C',     'CGU': 'R',     'AGU': 'S',     'GGU': 'G',
    'UGC': 'C',     'CGC': 'R',     'AGC': 'S',     'GGC': 'G',
    'UGA': 'Stop',  'CGA': 'R',     'AGA': 'R',     'GGA': 'G',
    'UGG': 'W',     'CGG': 'R',     'AGG': 'R',     'GGG': 'G'
}






protein_seq = ['ASQLDRFRVFLGWDNGMMLVYQGNKTYEPWLNCDMASPTLSLVSKKAPKILKAADINTTLQPCLAFFIELLLKGIDNERIPNSGSGGREMGLLAPTYSSEATLVTRENNMMEGVHGFENMQDVEVIKLKLPEGYSDVCHFMFMLAGILYIVYDLQMHMSSERETGKFPNPLSDEEFDNPKVVVTNSFVLLEFTVTGAGARPSEQGQEPHNLGATKGSLAISSKTPEIHKDTNPASAQFEGKHTESDAKGVSNEDVFITKERDGREVEPTIKLSKKSVLNPMNVVYNPMLQISEGALRKHSMNDEITILNNTLINKERSVDLGAVSFVNDLLIDKLGCVSGKLAVQLNQSAPPEILHGKDPLTLFLGNTIALMLSKMQRIRVWEEYIFLNLHLALAWEPLLGNLKTHDSQKKWALCGFLIISRIRNLFESEGPVHGLRFSAMPCNTDTRQIKALERFPYAPEKPQWHGDELESPCRLVVASKLLASHDGVSIGKTIGSWPLPAQRYNAYVAWAANDSSILSARPGFAVKEDRLGHSLAQESGTIVVRNPQYGVRFINYNKDEHREFKREATFYPKTVVTHLGAIEGTLMFEIGDAAFTMLHLEEATDAEVRELYYMDMLDKKSSLGRACERIRRVLAPGDHKANGLESAIVSGQNGYEGRIRGLQTFQSNPLKKGRTHMAFCTTLHPFGGLKLVSSQLLKKELAVGTYGHQRTVLHSAEYSCPTSIPNLEGLMYNLISAQGEVNSDAKCHYAALAYICLQVRSVSMNQTEASDLRNFLETPILANDALASEQLLGSKKAKS']

print(len(protein_seq))

#print(codon_frequence(imput1))

#count the occurence/frequency of each amino acid 
#find the longest number of elements that when deleted make the string even 

#8 is smallest number of AA occurrence

import collections

d = collections.defaultdict(int)
for read in protein_seq:
    for c in read:
        d[c] += 1

print(d)


valuesd = d.values()
import statistics
mean_ = statistics.mean(valuesd)

#print(mean_)

#40 is mean occurrence of each aa in string

#make an empty list which will contain all elements appearing more than mean no. of times
#iterate over list for each AA and if occurs more than 40 times pop element into list

AAs = {'F':0,'L':0,'S':0,'Y':0,'C':0,'W':0,'P':0,'H':0,'Q':0,'I':0,'M':0,'T':0,'N':0,'K':0,'R':0,'V':0,'A':0,'D':0,'E':0,'G':0}

popped_list = []



count = 8

for read in protein_seq:
    for element in read:
        if element in AAs and AAs[element]<=7:
            AAs[element]+=1
        else:
            popped_list.append(element)
            

print(len(popped_list))





for line in popped_list:
    a = popped_list.replace('"', '')
    
print(a)
