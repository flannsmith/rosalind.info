RNA = ['A','U','C','G']
DNA = ['A','T','C','G']

#input = DNA string, t, with max length of 1000nt
#return transcribed RNA string of t
#only diff is uracil replaces thymine nt in RNA 

dna_seq = open('rosalind_rna.txt','r')

#dna_seq = ['GATGGAACTTGACTACGTAAATT']

def DNA_to_RNA(dna_seq):
    transcribed_RNA_1 = ''
    for i in dna_seq:
        for letter in i:
            if letter == 'T':
                transcribed_RNA_1+=('U')
            else:
                transcribed_RNA_1+=(letter)
    return(transcribed_RNA_1)

print(DNA_to_RNA(dna_seq))


