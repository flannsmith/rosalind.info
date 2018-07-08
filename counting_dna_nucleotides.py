#dna_seq = ['TTCTTACGGTCTTACTGAAGACTATTCTTCGACACCAACAATGATCGCTCGCCCTCCAGGGCGTTGATCCCTTAGACGTTCTGTGTAACTCTTAGCCGTGCTGCCTCCAAACCTGACACTTTCTGTCGAGCATTCTGTACGCCTGCACGGCAGTTTTATGGCGCGCGTATCGACAATACAAATTCGTGTAAGCGGAAACCACACTGTGACTTGCTCACGTACCTTAAGGCGAAAAAGTGCCTTGCCGATTATCAACTCACGAAGCTCCGACCCAGCATTACTTGCACTTACTAGGTCCAGTTTGTGTGGACGTGAGGCCTGTGGCGTTTCCGAACAAACCCTACAAACGTGATGTGGCTTAACACGCACAAGTAATCGGGTCTGAGCTCAGCGACAAGCACAACACACTCCAATCCGGAGGTAACCTCGTGCAGCTAAAGCAGGGTTACCGGGTGATGCCGTACACTAATAAACGGTATATTCTGCACTACCGATTGTGTTTGGCGCATATCCTTAGAAGAATGACGGACCTAGACGTCTCTCGCTTAAGCCAAGGCTAGTGTAGCCCTCGAAGAATTGTACCTAGTTGGTAACGCTCATCTCTGTATGGTCTGTACACACTTTATTCTTGAATTGCAAGTACCCCAACGACGAAAGTGTTGCTATAGCTGGGAGCGGCCCGAGTGTAGGCACTGCGTGGTTTACGGGTCCTCTGAGCTCCTTTGCGCGCCAGGACGCCGGGATACATCTTTGCCCGAATGGATAATTATCTACAACATCCGATAGGTGATCTCCTACTCATGGATAAGTCAGAGTGAGTGGAGCAGGAATAGTGGGAACCCTAAGCCTCACACCTCTTAGATACCCTGTCCAAAATACGGTACAGATCATTGCTGTACCATCATAACAAGTTTACCTCACATCGAGGTGCTGAGAAACTCCA']



dna_seq = open('rosalind_dna.txt', 'r')


def count_nucleotides(dna_seq):
    a=0
    t=0
    c=0
    g=0
    for i in dna_seq:
        for base in i:
            if base == 'A':
                a+=1
            elif base == 'T':
                t+=1
            elif base == 'C':
                c+=1
            else:
                if base == 'G':
                    g+=1
        return(a, c, g, t)


print(count_nucleotides(dna_seq))

