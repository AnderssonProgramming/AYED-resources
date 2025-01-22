from sys import stdin
def countBits(n):
    # Function to count the number of set bits in a number
    return bin(n).count('1')

def sumBits(n):
    # Function to calculate the sum of bits from 1 to n
    return sum(countBits(i) for i in range(1, n+1))

def findN(X):
    # Binary search for smallest N such that sumBits(N) >= X
    left, right = 0, X
    while left < right:
        mid = (left + right) // 2
        if sumBits(mid) < X:
            left = mid + 1
        else:
            right = mid
    return left

def main():
    line = stdin.readline().strip()
    while line:
        X = int(line)
        N = findN(X)
        print("N =", N)
        line = stdin.readline().strip()
main()
