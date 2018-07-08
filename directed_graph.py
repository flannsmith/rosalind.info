import numpy as np
import pandas as pd
import Bio
from Bio.Seq import Seq
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.Alphabet import generic_dna
from Bio.SeqUtils import GC
import itertools

def is_k_overlap(s1, s2, k):
    return s1[-k:] == s2[:k]


def k_edges(data, k):
    edges = []
    for u, v in itertools.combinations(data, 2):
        u_dna, v_dna = data[u], data[v]

        if is_k_overlap(u_dna, v_dna, k):
            edges.append((u, v))

        if is_k_overlap(v_dna, u_dna, k):
            edges.append((v, u))

    return edges

graph_dict={}

from Bio import SeqIO
for seq_record in SeqIO.parse("rosalind_grph.txt", "fasta"):
    graph_dict[seq_record.id]=seq_record.seq
    # print(seq_record.id)
    #print(repr(seq_record.seq))
    # print(len(seq_record))

#print(graph_dict)

for edge in k_edges(graph_dict, 3):
    print (edge[0], edge[1])

#print(k_edges(graph_dict,3))
