"""PILAS"""

def stackEmpty(S):
    if S.top == 0:
        return True
    return False

def push(S,x):
    S.top = S.top + 1
    S[S.top] = x

def pop(S):
    if stackEmpty(S):
        raise Exception("underflow")
    S.top = S.top - 1
    return S[S.top + 1]

stack = [3,7,9,10,11]
stack.append(19)
print(stack.pop())

