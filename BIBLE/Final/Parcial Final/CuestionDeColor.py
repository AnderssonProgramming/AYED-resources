
from sys import stdin


def bicoloring(graph, colors, pos, c, n):
    if colors[pos] != -1 and colors[pos] != c:
        return False
    colors[pos] = c
    resp = True
    for i in range(n):
        if graph[pos][i]:
            if colors[i] == -1:
                resp &= bicoloring(graph, colors, i, 1-c, n)

            if colors[i] != -1 and colors[i] != 1 - c:
                return False

        if not resp:
            return False
    return True



def main():
    n = int(stdin.readline().strip())
    while n != 0:
        l = int(stdin.readline().strip())
        aris = [list(map(int, stdin.readline().strip().split())) for i in range(l)]
        graph = [[0 for j in range(n)] for i in range(n)]
        for arc in aris:
            graph[arc[0]][arc[1]] = 1
            graph[arc[1]][arc[0]] = 1
        colors = [-1] * n
        print('NOT BICOLORABLE.') if not bicoloring(graph, colors, 0, 1, n) else print('BICOLORABLE.')
        n = int(stdin.readline().strip())

main()

"""
3
3
0 1
1 2
2 0
3
2
0 1
1 2
9
8
0 1
0 2
0 3
0 4
0 5
0 6
0 7
0 8
0
"""