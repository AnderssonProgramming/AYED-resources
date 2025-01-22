from collections import deque
def enqueue(Q,x):
    Q[Q.tail] = x

    if Q.tail == len (Q):
        Q.tail = 1

    Q.tail = Q.tail + 1

def dequeue(Q):
    x = Q[Q.head]
    if Q.head == len (Q):
        Q.head = 1

    Q.head = Q.head + 1
    return x

queue = deque(["Marcos","Dillon","Maria"])
queue.append("Terry")
queue.append("LeBron")
print(queue)
print(queue.popleft())
print(queue.popleft())


