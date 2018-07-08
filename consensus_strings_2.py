from Bio import SeqIO

A, C, G, T = [], [], [], []
consensus = ""

with open('rosalind_cons.txt') as f:
    mylist = list(f)

for i in range(0, len(mylist)):
    countA, countC, countG, countT = 0, 0, 0, 0
    for record in SeqIO.parse("rosalind_cons.txt", "fasta"):
        if record.seq[i] == "A":
            countA = countA+1
        if record.seq[i] == "C":
            countC = countC+1
        if record.seq[i] == "G":
            countG = countG+1
        if record.seq[i] == "T":
            countT = countT+1

    A.append(countA)
    C.append(countC)
    G.append(countG)
    T.append(countT)

    if countA >= max(countC, countG, countT):
        consensus = consensus+"A"
    elif countC >= max(countA, countG, countT):
        consensus = consensus+"C"
    elif countG >= max(countA, countC, countT):
        consensus = consensus+"G"
    elif countT >= max(countA, countC, countG):
        consensus = consensus+"T"

print(consensus)

print("A: "+" ".join([str(i) for i in A]))
print("C: "+" ".join([str(i) for i in C]))
print("G: "+" ".join([str(i) for i in G]))
print("T: "+" ".join([str(i) for i in T]))


