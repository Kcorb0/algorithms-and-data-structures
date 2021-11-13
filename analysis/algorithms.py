# Measure the execution time
import time

def sum_of_n(n):
    start = time.time()

    nsum = 0
    for i in range(1, n + 1):
        nsum += i

    end = time.time()

    return nsum, (end - start)

def sumOfN3(n):
    start = time.time()
    nsum = ((n*(n+1))/2)
    end = time.time()

    return nsum, start-end

#print(sum_of_n(10000000))
#print(sumOfN3(100000000000000000000000000000000000000000000))


# Find minimum number, O(n) linear algorithm

def findmin(alist):
    num = alist[0]

    for i in alist:
        if i <= num:
            num = i

    return num

print(findmin([15215, 2125, 1255, 125, 1526, 127, 6325]))
