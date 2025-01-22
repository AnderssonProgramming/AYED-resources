import collections
from sys import stdin


def bicoloring():
    nodes = int(stdin.readline().strip())
    while nodes != 0:
        edges = int(stdin.readline().strip())
        m_ady = [[0 for i in range(nodes)] for j in range(nodes)]
        color = [-1 for i in range(nodes)]
        for i in range(edges):
            node1, node2 = list(map(int, stdin.readline().strip().split()))
            m_ady[node1][node2] = 1
            m_ady[node2][node1] = 1
        d_queue = collections.deque([0])
        color[0] = 0
        flag = True
        while d_queue:
            index_left = d_queue.popleft()
            for i in range(nodes):
                if not m_ady[index_left][i]:
                    continue
                if color[i] == -1:
                    color[i] = color[index_left] + 1
                    d_queue.append(i)
                elif color[index_left] == color[i]:
                    flag = False
        if flag:
            print("BICOLORABLE.")
        else:
            print("NOT BICOLORABLE.")
        nodes = int(stdin.readline().strip())


bicoloring()
