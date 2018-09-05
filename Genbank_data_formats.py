# Given: A collection of n(n≤10) GenBank entry IDs.

# Return: The shortest of the strings associated with the IDs in FASTA format.

from Bio import Entrez
from Bio import SeqIO

with open('/Users/lindasmith/Downloads/rosalind_frmt.txt') as input_data:
    #read function reads data from txt file, strip returns a copy of string removing all trailing whitespace
    #split splits IDs into a list of strings by using the default whitespace 
    IDs=input_data.read().strip().split()
    print(IDs)

Entrez.email = "your_name@your_mail_server.com"
handle = Entrez.efetch(db="nucleotide", id=IDs, rettype="fasta")
# we get the list of SeqIO objects in FASTA format 
records = list(SeqIO.parse(handle, "fasta"))


[min_index] = [i for i in range(len(records)) if len(records[i]) == min([len(record.seq) for record in records])]
print([min_index])

handle2 = Entrez.efetch(db='nucleotide', id=IDs, rettype='fasta')
minFASTA = handle2.read().strip().split('\n\n')[min_index]

print (minFASTA)


# print (records[0].id)  # first record id
# #gi | 227437129 | gb | FJ817486.1| 
# print (len(records[-1].seq))  # length of the last record

