import math

# O(n)
def count(n):
    for num in range(n):
        print(n)
    
# O(n^2)
def square(n):
    for row in range(n):
        for col in range(n):
            print(row, col)

# O(n^3)
def cube(n):
    for y in range(n):
        for x in range(n):
            for z in range(n):
                print(y, x, z)

# O(log n) - Recursive
def log_rec(n):
    print(n)
    if n == 0:
        return "Done"
    n = math.floor(n / 2)
    return log_rec(n)

# O(log n) - Iterative
def log_iter(n):
    new_num = n
    while True:
        if new_num != 0:
            new_num = math.floor(new_num / 2)
        else:
            return new_num
        print(new_num)


print(log_iter(100000000000000))