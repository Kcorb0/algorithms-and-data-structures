from pythonds.basic import Stack

stk = Stack()
stk.push('Axe')
stk.push('Spade')
stk.push('Gun')
stk.pop()

#print(stk.peek())
#print(stk.items)
#print(stk.size())


# Reverse a given string
def rev_string(str):

    str_stack = Stack()
    str_reversed = []

    for i in str:
        str_stack.push(i)

    while not str_stack.isEmpty():
        str_reversed.append(str_stack.pop())

    return "".join(str_reversed)

#print(rev_string('drawer'))

# Check for matching perentheses
def parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol == "(":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()

        index = index + 1

    if balanced and s.isEmpty():
        return True
    else:
        return False

#print(parChecker('((()))'))
#print(parChecker('(()'))
#print(parChecker(')))((('))
#print(parChecker('(()()()())'))

def parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top,symbol):
                       balanced = False
        index = index + 1
    if balanced and s.isEmpty():
        return True
    else:
        return False

def matches(open,close):
    opens = "([{"
    closers = ")]}"
    return opens.index(open) == closers.index(close)

#print(parChecker('{({([][])}())}'))
#print(parChecker('[{()]'))


