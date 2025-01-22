from random import randint
SEED = 100
SIZE = 10

def sortElement(index, s):
    element, inter = s[index], index
    for k in range(index, -1, -1):
        if element > s[k]:
            s[inter], s[k] = s[k], s[inter]
            element, inter = s[k], k

def insertionSort(s):
    for index in range(1,len(s)):
        sortElement(index, s)
    return s

def main():
    for i in range(SIZE):
        s = [randint(0,SEED) for j in range(SIZE)]
        print(s)
        print(insertionSort(s))
        print('---------')
main()