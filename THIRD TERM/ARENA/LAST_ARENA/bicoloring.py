from sys import stdin

def is_bicolorable(graph):
    colors = [None]* len(graph)
    def dfs(node, color):
        if colors[node] is not None:
            return colors[node] == color
        colors[node] = color
        for neighbor in graph[node]:
            if not dfs(neighbor, 1 - color):
                return False
        return True

    for node in range(len(graph)):
        if colors[node] is None:
            if not dfs(node, 0):
                return False
    return True

while True:
    n = int(stdin.readline().strip())
    if n == 0:
        break
    graph = [[] for _ in range(n)]
    l = int(stdin.readline().strip())
    for _ in range(l):
        u, v = map(int, stdin.readline().split())
        graph[u-1].append(v-1)
        graph[v-1].append(u-1)
    print("BICOLORABLE." if is_bicolorable(graph) else "NOT BICOLORABLE.")
