import pandas as pd
# Dynamic programming Python implementation of LIS problem

# lis returns length of the longest increasing subsequence
# in arr of size n

list1=[]

def lis(arr):
    n = len(arr)

    # Declare the list (array) for LIS and initialize LIS
    # values for all indexes
    lis = [1]*n

    # Compute optimized LIS values in bottom up manner
    global list1
    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j] and lis[i] < lis[j] + 1:
                list1.append(arr[i])
                lis[i] = lis[j]+1
                

    # Initialize maximum to 0 to get the maximum of all
    # LIS
    maximum = 0

    # Pick maximum of all LIS values
    for i in range(n):
        maximum = max(maximum, lis[i])

    return maximum,list1
# end of lis function


#arr = [10, 22, 9, 33, 21, 50, 41, 60]

arr=[5, 1, 4, 2, 3]
print ("Length of lis is", lis(arr))
# This code is contributed by Nikhil Kumar Singh


#myset = set(list1)
print(list1)

