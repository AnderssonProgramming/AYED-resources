
"""Considere una pila S y una cola Q, ambas vacías en un principio.Ilustre el paso a paso"""
from collections import deque

#a)

    #Ambas cadenas vacías
S = []
Q = deque([])

print("SECUENCIA S STACK")

    #S.push(2)
S.append(2)

    #S.push(8)
S.append(8)

    #S.push(11)
S.append(11)

    #S.pop()
print(S.pop())

    #S.push(-3)
S.append(-3)

    #S.push(7)
S.append(7)

    #S.pop()
print(S.pop())

    #S.pop()
print(S.pop())

print(S)

#b)

print("SECUENCIA Q QUEUE")

    #Q.enqueue(4)
Q.append(4)

    #Q.enqueue(17)
Q.append(17)

    #Q.enqueue(20)
Q.append(20)

    #Q.enqueue(6)
Q.append(6)

    #Q.enqueue()
print(Q.popleft())

    #Q.enqueue()
print(Q.popleft())

    #Q.enqueue(-5)
Q.append(-5)

    #Q.enqueue()
print(Q.popleft())

print(Q)
