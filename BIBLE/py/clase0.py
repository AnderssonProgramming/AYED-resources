from sys import stdin


def readline():
    return stdin.readline().strip()


def relationalOperator(a, b):
    return '=' if a == b else ('<' if a < b else '>')


def main():
    """cases = int(readline())
    for case in range(cases):
        a,b = map(int, readline().split())
        print(relationalOperator(a,b))"""
    A = [1, 2, 3, 5, 6, 7]
    print(4 in A)


main()
