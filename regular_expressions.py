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

#finding (.+) (.+) 
#We can now refer to the captured bits of the pattern by supplying an argument to the group() method. group(1) will return the bit of the string matched by the section of the pattern in the first set of parentheses, group(2) will return the bit matched by the second,

scientific_name = "Homo sapiens"

m = re.search("(.+) (.+)", scientific_name)

if m:
    genus = m.group(1)
    species = m.group(2)
    print("genus is " + genus + ", species is " + species)


#searching for ambiguous base

dna = "CGATNCGGAACGATC"
m = re.search(r"[^ATGC]", dna)

if m:
    print("ambiguous base found!")
    print("at position " + str(m.start()))




#multiple matches

dna = "CGCTCNTAGATGCGCRATGACTGCAYTGC"

matches = re.finditer(r"[^ATGC]", dna)
for m in matches:
    base = m.group()
    pos = m.start()
    print(base + " found at position " + str(pos))


#We could extract the bits of the string that match the pattern using re.finditer() and group():

dna = "CTGCATTATATCGTACGAAATTATACGCGCG"

matches = re.finditer(r"[AT]{6,}", dna)

result = []
for m in matches:
    result.append(m.group())

print(result)


#SPLITTING A STRING USING A REGULAR EXPRESSION

dna = "ACTNGCATRGCTACGTYACGATSCGAWTCG"
runs = re.split(r"[^ATGC]", dna)
print(runs)
