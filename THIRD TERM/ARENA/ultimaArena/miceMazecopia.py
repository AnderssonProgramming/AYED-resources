from sys import stdin
import heapq
def prims(source, nv, adj, tmax):
    q = [(0, source)]
    dist = [1000000] * (nv + 1)
    dist[source] = 0
    cont = 0

    while len (q) > 0:
        wu, u = heapq.heappop (q)
        for wv, v in adj[u]:
            if dist[wv] > dist[u] + v:
                heapq.heappush (q, (dist[u] + v, wv))
                dist[wv] = dist[u] + v
    for d in dist:
        if d <= tmax:
            cont += 1

    return cont

def main():
    cases = int(stdin.readline ())

    for _ in range(cases):
        stdin.readline()
        n = int(stdin.readline())
        salida = int(stdin.readline())
        tmax = int(stdin.readline())
        k = int(stdin.readline())

        graph = [list () for x in range (n + 1)]

        for i in range (k):
            a, b, c = [int (x) for x in stdin.readline().split()]
            graph[b].append ((a, c))

        resp = prims (salida, n, graph, tmax)
        #
        if _ == cases - 1:
            print (resp, end="\n");
        else:
            print (resp, end="\n\n");
main ()