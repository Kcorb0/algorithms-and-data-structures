# Measure the execution time
import time

def sum_of_n(n):
    start = time.time()

    nsum = 0
    for i in range(1, n + 1):
        nsum += i

    end = time.time()

    return nsum, '{0:.20f}'.format(start-end)

def sum_of_n3(n):
    start = time.time()
    nsum = ((n*(n+1))/2)
    end = time.time()

    return nsum, '{0:.16f}'.format(start-end)



# Find minimum number, O(n) linear algorithm

def findmin(alist):
    num = alist[0]

    for i in alist:
        if i <= num:
            num = i

    return num

n = 100000010

for i in range(100000000, n):
    print(sum_of_n(i))