from random import randint

SIZE = 10
SEED = 1e2 # 1 x 10 ^ 2 --> float



def isOrdered(s):
    is_ordered, index = True, 0
    while is_ordered and (index + 1) < len(s):
        is_ordered, index = (s[index] <= s[index+1]), index + 1
    return is_ordered

def main():
    print(isOrdered([2,3,4,1,2,3]))
    print(isOrdered([1,2,3,4,5,6]))
    print(isOrdered(['A', 'B', 'Z']))
    print(isOrdered(['Z', 'B', 'A']))


#main()


for i in range(int(1e2)):
    s = [randint(0, int(SEED)) for i in range(SIZE)]
    w = insertionSort(s)
    print(s, '----> ', w, '--->', isOrdered(w))
