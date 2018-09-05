from Bio import ExPASy #access Biopython's ExPASy database
from Bio import SwissProt #obtain data from an entry using the SwissProt module

handle = ExPASy.get_sprot_raw('A6N0M9')  # gets protein by its ID
record = SwissProt.read(handle)  # use SwissProt.parse for multiple proteins

#print(dir(record))
# print(record.cross_references)


with open('/Users/lindasmith/Downloads/rosalind_dbpr.txt') as input_data:
	UniProt_ID = input_data.read().strip()

handle = ExPASy.get_sprot_raw(UniProt_ID)
record = SwissProt.read(handle)

bio_proc = []
for item in record.cross_references:
    if item[0] == 'GO' and item[2][0] == 'P':
        bio_proc.append(item[2].lstrip('P:'))

print ('\n'.join(bio_proc))
with open('intro_to_protein_db.txt', 'w') as output_data:
	output_data.write('\n'.join(bio_proc))

