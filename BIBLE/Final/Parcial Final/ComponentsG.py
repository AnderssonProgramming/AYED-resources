import math
from sys import stdin


class DisjointSets:
    def __init__(self, elements = []):
        self.data = []
        if len(elements) > 0:
            for e in elements:
                self.make_set(e)

    def find_set(self, e):
        for st in self.data:
            if e in st:
                return st
        return None

    def make_set(self, e):
        if self.find_set(e) is None:
            self.data.append(set([e]))
            return self.data[len(self.data) - 1]

    def union_find(self, x, y):
        c1 = self.find_set(x)
        c2 = self.find_set(y)
        if c1 is None:
            c1 = self.make_set(x)
        if c2 is None :
            c2 = self.make_set(y)

        if c1 != c2:
            c_union = c1.union(c2)
            self.data.remove(c1)
            self.data.remove(c2)
            self.data.append(c_union)

    def getData(self):
        return self.data

    def __len__(self):
        return len(self.data)

def connected_components(V, E):
    dj = DisjointSets(V)
    for e in E:
        dj.union_find(e[0], e[1])

    con_comp = []
    for st in dj.getData():
        if len(st) > 1:
            con_comp.append(st)

    return con_comp

def MST_Kruskal(G):
    mst = set([])
    dj = DisjointSets(G['V'])
    sorted_e = G['E'][:]
    sorted_e.sort(key = lambda tup: (tup[2], tup[0], tup[1]))
    while len(sorted_e) > 0 and len(dj) > 1:
        e = sorted_e.pop(0)
        u,v = e[0], e[1]
        if dj.find_set(u) != dj.find_set(v):
            mst.add(e)
            dj.union_find(u, v)
    return mst

def minAndMax(G):
    conectComps = connected_components(G['V'], G['E'])
    max = -math.inf
    min = math.inf
    for comp in conectComps:
        if len(comp) > max:
            max = len(comp)
        if len(comp) < min:
            min = len(comp)
    return min, max


def main():
    n = int(stdin.readline().strip())
    V = []
    E = []
    for i in range(n):
        j, k = map(int, stdin.readline().strip().split())
        E.append((j, k))
        if j not in V:
            V.append(j)
        if k not in V:
            V.append(k)
    G = {
        'V': V,
        'E': E
    }
    resp = minAndMax(G)
    print(resp[0], resp[1])

main()

"""
6
1 7
2 7
2 9
4 9
5 12
6 12
"""
"""
10
1 17
5 13
7 12
5 17
5 12
2 17
1 18
8 13
2 15
5 20
"""
