import re

accessions = ['xkn59438', 'yhdck2', 'eihd39d9', 'chdsye847', 'hedle3455', 'xjhd53e', '45da', 'de37dp']


#find entry that contains number 5

for i in accessions:
    if re.search(r"5", i):
        print("\t" + i)


#find entry that contains d or e

for i in accessions:
    if re.search(r"(d|e)", i):
        print("\t" + i)

#contain the letters d followed by e in that order

for i in accessions:
    if re.search(r"(d.*e)", i):
        print("\t" + i)


#contain the letters d and e in that order with a single letter between them
for i in accessions:
    if re.search(r"(d.e)", i):
        print("\t" + i)


#contain both the letters d and e in any order
for i in accessions:
    #if re.search(r"(d.*e|e.*d)", i):
    if re.search(r"d.*e", i) or re.search(r"e.*d", i):
        print("\t" + i)


#start with x or y
for i in accessions:
    if re.search(r"(^x|^y)", i):
        print("\t" + i)

#start with x or y and end with e    
#  we need to use .* in the middle to match any number of any character
for i in accessions:
    if re.search(r"(^x|^y).*e$", i):
        print("\t" + i)


#contain three or more digits in a row
for i in accessions:
    if re.search(r"\d{3,}", i):
        print("\t" + i)

#end with d followed by either a, r or p
for i in accessions:
    if re.search(r"d[arp]$", i):
        print("\t" + i)


