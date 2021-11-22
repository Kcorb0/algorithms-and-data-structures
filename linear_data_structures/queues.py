# Hot potato sim
# input list of names and constant for counting round the circle
# Output survivor
from pythonds.basic import Queue

def hotpotato(names, num):

    q = Queue()
    for name in names:
        q.enqueue(name)

    count = 0
    while q.size() > 1:
        
        if count == num:
            q.dequeue()
            count = 0
        else:
            q.enqueue(q.dequeue())
            count += 1

    return q.dequeue()


names = ["Hades", "Neptune", "Josh", "Zeus", "Hermes", "Aphrodite"]
print(hotpotato(names, 7))