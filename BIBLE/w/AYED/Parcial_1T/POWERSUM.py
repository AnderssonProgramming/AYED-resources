from sys import stdin


def pow_sum(x, n, index):
    pow_num = (index ** n)
    if x == pow_num:
        return 1
    if x < pow_num:
        return 0
    return pow_sum(x - pow_num, n, index + 1) + pow_sum(x, n, index + 1)


def memo_power(x, n, index, mem):
    try:
        return mem[x, n]
    except KeyError:
        mem[x, n] = pow_sum(x, n, index)
        return mem[x, n]


def main():
    line = stdin.readline().strip()
    n = stdin.readline().strip()
    mem = {}
    while line:
        line = int(line)
        n = int(n)
        print(memo_power(line, n, 1, mem))
        line = stdin.readline().strip()
        n = stdin.readline().strip()

main()
