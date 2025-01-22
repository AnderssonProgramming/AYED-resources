from sys import stdin
def binary(n):
    return [] if n < 1 else binary(n // 2) + [n % 2]

def sumBits(count):
    Bsum = sum(binary(count))
    return Bsum

def main():
    X = int(stdin.readline().strip())
    count = 0
    summ = 0
    while summ < X:
        count += 1
        summ += sumBits(count)
    print(count)

main()