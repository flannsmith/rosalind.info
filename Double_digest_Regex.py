# Click here to download a file dna.txt which contains a made up DNA sequence. Predict the fragment lengths that we will get if we digest the sequence with two made up restriction enzymes – AbcI, whose recognition site is ANT/AAT, and AbcII, whose recognition site is GCRW/TG. The forward slashes(/) in the recognition sites represent the place where the enzyme cuts the DNA.

import re

#how to work out the fragment sizes from the cut positions?

dna = open("dna.txt").read().strip('\n')
all_cuts = [0]
print("AbcI cuts at:")
for match in re.finditer(r'A[ATCG]TAAT', dna):
    # +3 because enzyme cuts 3 base pairs upstream of the start
    all_cuts.append(match.start() + 3)

all_cuts.append(len(dna))

    
print(all_cuts)

for i in range(1,len(all_cuts)):
    this_cut_position = all_cuts[i]
    previous_cut_position = all_cuts[i-1]
    fragment_size = this_cut_position-previous_cut_position
    print("One fragment size is " + str(fragment_size))


import re
dna = open("dna.txt").read().rstrip("\n")
print(str(len(dna)))
all_cuts = [0]
# add cut positions for AbcI
for match in re.finditer(r"A[ATGC]TAAT", dna):
    all_cuts.append(match.start() + 3)
# add cut positions for AbcII
for match in re.finditer(r"GC[AG][AT]TG", dna):
    all_cuts.append(match.start() + 4)
# add the final position
all_cuts.append(len(dna))
sorted_cuts = sorted(all_cuts)
print(sorted_cuts)
for i in range(1, len(sorted_cuts)):
    this_cut_position = sorted_cuts[i]
    previous_cut_position = sorted_cuts[i-1]
    fragment_size = this_cut_position - previous_cut_position
    print("one fragment size is " + str(fragment_size))

