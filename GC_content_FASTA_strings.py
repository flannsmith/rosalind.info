import numpy as np
import pandas as pd
import Bio
from Bio.Seq import Seq
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.Alphabet import generic_dna
from Bio.SeqUtils import GC


# with open('rosalind_gc.txt', 'r') as fasta_file:
#     fasta_file = list(fasta_file)

rec1 = SeqRecord(Seq("TAAGGCCTTTCATACAGGGGAGGTAGCAGGGTTCTGTTCCCATGGGAATTTCCTGCGCAC\
                     TACTGTAGGGTTGTCATGCGTGTAGCGAAGATTGAGCCGCTGCCTCTGATGCGACAGGTA\
                     GGAAATAGACAAAGTTCGTATCAGCCGGGGATTTGTACACCCGTTGGCTACCTAAAAACG\
                     TCCTCGAAAGCCGTTTCCCGGATGCCGTGACCAGAAGTAGTACGCTTCTGCGTGGTTGAT\
                     CTGGATGTATGATACGGCTACGTTTGCCATAGGAATCTGCTAACGCTCCGCACCATGTAT\
                     GCAGTGTCCGAGCGCCCTCCTTATATAAAATCACTTCTACAAGTTCCTGGGCGGGCGGTT\
                     GTCATTCACAGGCCAGACGTATGCATGTTCCGGACTTCATGCGGTGACCCCTTCCTTTTT\
                     TTGAACCTCGACTACCGTCCGGCGTCACATGGGTACGAGGCCGCTAGTCTTGCTGATATC\
                     TCCGCTAGCCTAAAAGTTGGTGATTGGGTTTCCAGCGTTTGGCCTTAACTATACTGAGAC\
                     CTACGAAGATCCACCCATGTCCAGTCCCCCACATGGTGGTTTGGGAAGCTATGAATCAAG\
                     GTGAACCGTTCAAGGATCCGGCGAACACTTACATTCGTCCGTTTGCATATGGTTTCTTTG\
                     GAGTCTGTCTTTCGCAACATATTGTGCCCCAACGAAGCTTATCCGTTGTACCGATCCGCG\
                     TTTTCCACGATATACGATCGTATCGGAACTCAGGTTTCATCTGAGTGACTGGTCACGTCG\
                     AACATGCGTCGGGTCGAGGCAAC", generic_dna), id="> Rosalind_7648",
                    description="")


rec3 = SeqRecord(Seq("ACAAACCCCGCGAAACCTGAGGCATGCGACGTGTCAACAACCTGGTCGTAAGCTCGGGTC\
                     GAGTCGAGCCGCTTTTGGGGCGCACTAAAGGAAGCCCATGGAATATATCACGTTGCTAGA\
                     GTGGCAGAAGGGTTCAAAGTGGGTCACATCGCCCACGAACGTTCGGTCGCGTAGCCTGTC\
                     TGTGACAGTACAGCAAGTCTTAAAAACCGGACATGGTAGTGACTAGCGATGAATCACTAC\
                     TCCGTCACCAATTTACTGTGCGCAGTAACTTCCTGGAGGTACGGGTAGCCCAAACTAGGA\
                     ATCGTATTGGCTGTACTAGGACCGCACCTGTTGGGCTCTGATTGCGCCCCTGTGACATGT\
                     GGACGTTGGATCGAGCGAGCACAGCACACTCCGTTTAAGTGGTTCCCGTGTGAGCGGCTT\
                     TTAGTCGGAGGATGGGATCGCTTGAATAAGTCATACTCAGCACGCATTCACCTTGACGCG\
                     GTGCCTCATATGGGTTTTCCCAGTGTTGCAGCACAGACACCCTATTAAACCCCTATTAGC\
                     TGCCCCAAACGTCGAAGTCCAGTCATCGAATAATATCGGATTGCCCCTACACATGGAACA\
                     GTTGAAGGACGTAATCTATATGAAGCCAATTCCGTTACTTGCTGAGTGACCGTAAACAAA\
                     ATGAGCGCTTTCACAGCTAGCAGATCCGCCATCAGGTATCCGTTGGGATATCCCTCGTAA\
                     CTCCCCAGCGGGGGCACCTCTGTCCAGGCGACATGTGATCCATGTTTTGCGTACCGTCAG\
                     TGCGCGTGGTTGCAGAGGGAGCTCATCTCGTACAAGTGGTACCCGACCAAGCTATATGGA\
                     ACCTTTCGCCGCATCGAAG\
                     ", generic_dna),
                 id="",
                 description="")

rec4 = SeqRecord(Seq("ATAACGACCAGTTCTATGTGGGACTTGCCAAATTTTACAGATGGGTTGGAATGTAGTTTG\
                     TATATACTGGAGAATGTTGAGTAACCATTGGTGAGTCTGGATTGTGGATGTAGTCTGTAT\
                     TGGCAGCCGTGCTAAAGGTCGGGAACGTACACGGTGAGATTCACCCACGCTGCTAATTGG\
                     AAAACGATCCTGGCACGTATTATCATGGACTTTTAGTCTTCATTATATCAGTACTTGAAG\
                     TGGAACCCATGGAGTAGAATGACGTCGGAACAACAGAAATTCACATTGTCCTTCAGACGA\
                     TGTAATATTTAGATGTCTCGACTGAACCCCTGTACGATCAGATGCTTTCTAACCAACAAT\
                     GCCAGTGAAAACACGTGTACCCTGACACTTCAGGTGCACGGCACCAAAATCGTGGAACGA\
                     ACCAGCACTTACGTCGATAATCCGAAGAGCACGCGCGGGTAAAGGTTACATTATTTACAT\
                     CGACCCGGCACTATAGTGAACTTAATGGAGAAATGTTTCTCTAAGTCTCTCGGGTTATAT\
                     GGCGATTTCTGATTGTGGCGCACAATATATTGCGGCACCCAACGTCAACATGTGACCAAC\
                     CAGGTCTGATGGATCCAACAGTTCCAGCAAGAACGGTATCAACTTTTAATTCTTCAGAGT\
                     TAGTCATCTTTCGGAACGCGATACCCGTTGAGGATCAAAACAAAGACTTACCTTTGTGAA\
                     TGTTGTGACTTCTGATTCCTCCCCCCTGCCCAAAATGATATCGCTAATCATAGAGGGCTT\
                     GCTTGGGACAAAATTCCCACCGGGATCAACCGGGTGACGCCCACGAGTACCCGTGGACCT\
                     ACCGGTTTCCATATGATAAATTAAGAAGGAGGAAAAGTAAGCGCCTT\
                     ", generic_dna),
                 id="> Rosalind_7983
                 ",
                 description="")

rec5 = SeqRecord(Seq("ACAGTGGACTGATAAGGAAGTGAAAGTTCGGTGACTGGGCCATCCCCTGGGGTAGTGCAA\
                     TGCCTTACGGGCCTGCAAACGCGCCATGTATAATTATGCCCTGTCGTCGGGACACGTAGT\
                     GCTCCTCGAAGTCGCTTCCTCTCCCGTTCCCCCCCGTATTTGCAATGATTCCCGTACTAT\
                     CTTTTGTGCTGTACTAAACTCCCCCTTACAATCACGGATACTTCGGAGGTGGTAGTAGAC\
                     AAGTTGGGGGAGCAATGGCAGAAATATGGGGCGTTCATAGAGACGTCCAACACGATGGGC\
                     GGAGGCATTTACTGCAGCTATTGCAGTCAGACCGAACGCGTCTACGAAGCCGGTAAGACT\
                     TATCTCTTGCGCGTTGGCTCTCGGCTAGCGCAATCTAAGCTCAGACAGATAGAGTCCGAG\
                     CTTGCACTAGCGGGTAAAGGTCGTCGTATGGAAAACTTCCAGCTTCCACGGTCTTATGAC\
                     GAAGTTGCGGTATCGGTCTCAGCTGGGGTCTTCATCCGTGTTAACATACCCACGCCCGGT\
                     ACCCGTACCAGCTCCGCGTTTAATAAGCAGTCAAGTCTTGTTTCTGGAATGATCATTAGC\
                     GAGGAAGATTTGAAGTCAAAGTGTGTCGGTAACTCCAGTCCATATGTGATGAGACGAGCC\
                     GGATCTGAGGGCTTGAGCGGATGCATCTACGGAGCGTCGCCGTATTGGAACCGGCGACTA\
                     GATTAACAGGGGGACAGAAGCTCACGGAAGGGCCGGTCAAGGGAATATGAATGATTACGT\
                     TCTATCGTCCGACTGGCTATTCCGCATAACTGAAATCGCCCCCCTTGTTTGTTCATCCTG\
                     AAACCGGAAGGGTGGGAACCAGGGCTTACTTCCAATGCCATGCCGCTCGGTGATTCGCTT\
                     GCTAGACTGTTTTT\
                     ", generic_dna),
                 id=">Rosalind_9034",
                 description="")


sequences = [rec1, rec2, rec3, rec4, rec5]
highestGC = 0
currentGC = 0
highGCid = -1
currentid = 0

for s in sequences:
    currentGC = (GC(s.seq))
    if currentGC > highestGC:
        highestGC = currentGC
        highGCid = currentid
    currentid = currentid + 1

print(sequences[highGCid].id)
print(highestGC)

print("\n---\n")





