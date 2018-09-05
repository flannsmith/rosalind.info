import re

dna = "ATCGCGAATTCAC"
if re.search(r'GC(A|T|G|C)AC', dna):
    print("restriction site found!")

# if re.search(r'GC)
dna = "ATCGCGAATTCGC"
if re.search(r"GC[ATGC]GC", dna):
    print("restriction site found!")

#So the pattern GC[ATGC]GC will match GCAGC, GCTGC, GCGGC and GCCGC.

regex = re.compile('[^a-zA-Z]')
#First parameter is the replacement, second parameter is your input string
regex.sub('', 'ab3d*E')
#Out: 'abdE'

regex = re.compile('[,\.!?]')  # etc.
