#Fn=Fn-1 + Fn-2
# a recurrence relation defines the terms of a sequence with respect to the values of previous terms

def rabbitPairs(numMonths, numOffspring):
    if numMonths == 1:
        return 1
    elif numMonths == 2:
        return numOffspring
    
    oneGen = rabbitPairs(numMonths-1, numOffspring)
    twoGen = rabbitPairs(numMonths-2, numOffspring)

    if numMonths <=4:
        return (oneGen + twoGen)
    else:
        return(oneGen + (twoGen*numOffspring))

print(rabbitPairs(32,4))