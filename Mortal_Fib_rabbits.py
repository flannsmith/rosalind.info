n = 99
m = 18

ages = [1] + [0]*(m-1)
for i in range(n-1):
    ages = [sum(ages[1:])] + ages[:-1]
print(sum(ages))


print("\n---\n")

