k = 21 # DD
m = 17 # Dr
n = 18 # rr


total = k + m + n
total2 = total - 1

prob = k/total + m/total * ( (k/total2) + (0.75*((m-1)/total2)) + (0.5*(n/total2)) ) + n/total * ( (k/total2) + (0.5*(m/total2)) )

print(prob)

print("\n---\n")


