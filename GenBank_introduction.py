#Given: A genus name, followed by two dates in YYYY/M/D format.

#Return: The number of Nucleotide GenBank entries for the given genus that were published between the dates specified.


from Bio import Entrez #data retrieval system offered by NCBI

with open('/Users/lindasmith/Downloads/rosalind_gbk.txt') as input_data:
	genus, start_date, end_date = [line.strip() for line in input_data.readlines()]

print(genus, start_date, end_date)

Entrez.email = 'flannsmith@gmail.com'
handle = Entrez.esearch(db='nucleotide', term=genus +'[ORGN]', mindate=start_date, maxdate=end_date, datetype='pdat')


record = Entrez.read(handle)
print(record)
print (record['Count'])

