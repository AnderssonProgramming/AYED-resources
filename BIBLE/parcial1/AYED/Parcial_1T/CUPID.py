from sys import stdin

def search(princ, index_0, index_n, h):
    if index_0 > index_n:
        return 0
    mid = (index_0 + index_n)//2
    if princ[mid] <= h:
        return max(princ[mid], search(princ, mid + 1, index_n, h))
    elif princ[mid] >= h:
        return search(princ, index_0, mid - 1, h)
    elif len(princ) == 1 and princ[mid] < h:
        return princ[mid]
    elif len(princ) == 1 and princ[mid] >= h:
        return 0


def comparator(hei, princ):
    if search(princ, 0 , len(princ), hei - 1) != 0:
            return search(princ, 0 , len(princ), hei - 1)
    return "X"


def main():
    N = int(stdin.readline().strip())
    princesses = [int(index) for index in stdin.readline().strip().split()]
    Q = int(stdin.readline().strip())
    inquiries = [int(index) for index in stdin.readline().strip().split()]
    for hei in inquiries:
        print(comparator(hei, princesses))


main()
