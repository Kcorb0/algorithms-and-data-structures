# Converting decimal numbers to binary numbers
# Divide by 2 algorithm
# Start with an int greater than 0
# Continually divide the number by 2 keeping track of the remainder
# For every remainder if the value is even (0) then an odd value will have a remainder of 1
# The first remainder will be the last digit of the sequence
# Pop the numbers out sequencially for the answer

from pythonds.basic import Stack

def convert_to_binary(num):

    bin_stack = Stack()
    binary = ""

    while num > 0:
        rem = num % 2
        bin_stack.push(rem)
        num = num // 2

    while not bin_stack.isEmpty():
        digit = bin_stack.pop()
        binary = binary + str(digit)

    return binary

print(convert_to_binary(42))
print(convert_to_binary(4251))
print(convert_to_binary(6516163))

def baseConverter(decNumber,base):
    digits = "0123456789ABCDEF"

    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % base
        remstack.push(rem)
        decNumber = decNumber // base

    newString = ""
    while not remstack.isEmpty():
        newString = newString + digits[remstack.pop()]

    return newString

print(baseConverter(25,8))
print(baseConverter(26,26))