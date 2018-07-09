
# import itertools
# n = 4
# s = ['H', 'U', 'P', 'M']
# perm = itertools.product(s, repeat=n)
# for i, j in enumerate(list(perm)):
#     permutation = ''
#     for item in j:
#         permutation += str(item)
#     with open('rosalind_lexf.txt', 'a') as text_file:
#         print(permutation.strip(), file=text_file)


import itertools
n = 5
s = ['H', 'U', 'P', 'M']
perm = itertools.product(s, repeat=n)
answer = []
for i, j in enumerate(list(perm)):
    permutation = ''
    for item in j:
        permutation += str(item)
    answer.append(permutation)

sorted_answer = sorted(answer)
with open('rosalind_lexf.txt', 'a') as text_file:
    print(*sorted_answer, sep=' ', file=text_file)



