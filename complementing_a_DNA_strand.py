#A and T are complements of C and G
#reverse complement of GTCA ==> ACTG ==> AGAC

#DNA = ['AAAACCCGGT']
DNA_complement = ['ACCGGGTTTT']

DNA = open('rosalind_revc.txt', 'r')


def complement_DNA_strand(DNA):
    DNA_strand_comp=''
    for i in DNA:
        DNA_reversed = ''.join(reversed(i))
   
    for letter in DNA_reversed:
        for i in letter:
            if i == 'A':
                DNA_strand_comp+=('T')
            elif i == 'T':
                DNA_strand_comp+=('A')
            elif i == 'C':
                DNA_strand_comp+=('G')
            elif i == 'G':
                DNA_strand_comp+=('C')
    return(DNA_strand_comp)


print(complement_DNA_strand(DNA))

