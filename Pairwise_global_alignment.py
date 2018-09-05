# The best we can do is to compare alignments quantitatively by using a scoring approach. Many such alignment scores assign 0 to a match, a negative number to a mismatch, and an even larger negative number to a gap. Summing all these scores over an alignment gives the alignment's score
# in keeping with the assumption of parsimony, the optimal alignment will have the highest score, implying the fewest possible changes between the strings.

# EBI hosts many different online user interfaces for bioinformatics tools, including Needle and Stretcher. Needle and Stretcher are tools from the EMBOSS package that are for aligning genetic strings.

#https: // www.ebi.ac.uk/Tools/psa/emboss_needle/nucleotide.html


from Bio import Entrez
from Bio import SeqIO

from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqFeature import SeqFeature
from Bio.SeqRecord import SeqRecord


#Convert genBank ID to nucleotide sequence

Entrez.email = 'flannsmith@gmail.com'

with open('/Users/lindasmith/Downloads/rosalind_need.txt') as input_data:
    GenBankIds = input_data.read().strip().split()
    # print(GenBankIds)


Entrez.email = "Your.Name.Here@example.org"
handle = Entrez.efetch(db="nucleotide", id=GenBankIds, rettype="gb",retmode="text")
print(handle.read())

# record = Entrez.read(handle)

#record = Entrez.read(Entrez.einfo())



# records = list(SeqIO.parse(handle, "gb"))
# print(records.Seq)


# records = list(SeqIO.parse(handle, "genbank"))

# print(records)
