WHITE = "white"
BLACK = "black"
from sys import stdin

class Graph:
    def __init__(self, n):
        self.n = n
        self.adj_list = [[] for _ in range(n)]
        self.colors = [None] * n

    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def dfs(self, u, color):
        self.colors[u] = color
        for v in self.adj_list[u]:
            if self.colors[v] is None:
                if not self.dfs(v, BLACK if color == WHITE else WHITE):
                    return False
            elif self.colors[v] == color:
                return False
        return True

def main():
    while True:
        n = int(stdin.readline().strip())
        if n == 0:
            break

        m = int(stdin.readline().strip())
        g = Graph(n)

        for _ in range(m):
            u, v = map(int, stdin.readline().split())
            g.add_edge(u, v)

        if g.dfs(0, WHITE):  # Comenzamos con color blanco
            print("BICOLORABLE.")
        else:
            print("NOT BICOLORABLE.")

main()
