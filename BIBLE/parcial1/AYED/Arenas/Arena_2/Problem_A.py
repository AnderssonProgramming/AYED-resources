from sys import stdin
import time

def algorithm(n, cycles):
    if n == 1:
        cycles += 1
        return cycles
    if n % 2 == 1:
        n = (3*n)+1
        cycles += 1
        return algorithm(n, cycles)
    elif n % 2 == 0:
        cycles += 1
        n = n//2
        return algorithm(n, cycles)

def memo_aglo(index, cycles, mem):
    try:
        return mem[index] + cycles
    except KeyError:
        mem[index] = algorithm(index, cycles)
        return mem[index]


def main():
    line = stdin.readline().strip()
    mem = {}
    while line:
        i, j = map(int, line.split())
        h, k = i, j
        i, j = min(i, j), max(i, j)
        c_max = 0
        for index in range(i, j+1):
            cycles = memo_aglo(index, 0, mem)
            if cycles > c_max:
                c_max = cycles
        print(h, k, c_max)
        line = stdin.readline().strip()


if __name__ == '__main__':
    main()
