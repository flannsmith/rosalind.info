import itertools 
n = 3 
s = 'A B C D E F G'
lst = list(map(str,s.split())) 
x = list(itertools.product(lst, repeat=n))
#print(x)
#print(len(x))
print(*[''.join(i) for i in x],sep='\n')


