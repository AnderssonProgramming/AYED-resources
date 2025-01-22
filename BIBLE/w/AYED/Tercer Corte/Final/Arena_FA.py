from sys import stdin
import math


class DisjointSets:
    def __init__(self, A):
        self.sets = []
        for x in set(A):
            self.makeSet(x)

    def connectedComponents(self, E):
        # Union ranked
        for ei in E:
            self.union(ei[0], ei[1])

        connected_components = []
        for st in self.sets:
            if len(st) > 1:
                connected_components.append(st)

        return connected_components

    def findOrCreate(self, x):
        sx = self.findSet(x)
        if sx is None:
            sx = self.makeSet(x)
        return sx

    def union(self, x, y):
        s1,s2 = self.findOrCreate(x), self.findOrCreate(y)
        if s1 != s2:
            s3 = s1.union(s2)
            self.sets.remove(s1)
            self.sets.remove(s2)
            self.sets.append(s3)

    def findSet(self, x):
        ret = None
        for s_i in self.sets:
            if x in s_i:
                ret = s_i
        return ret

    def makeSet(self, x):
        if self.findSet(x) is None:
            self.sets.append(set([x]))
            return self.sets[len(self.sets)-1]
        return None

    def getSets(self):
        return self.sets


def main():
    n = int(stdin.readline().strip())
    edges = []
    dis_s = DisjointSets([])
    for index in range(n):
        edge = list(map(int, stdin.readline().split()))
        edges += [edge]
        for nod in edge:
            dis_s.makeSet(nod)
    sets = dis_s.connectedComponents(edges)
    max_edges = -1
    min_edges = math.inf
    for set in sets:
        if len(set) > max_edges:
            max_edges = len(set)
        if len(set) < min_edges:
            min_edges = len(set)
    print(min_edges, max_edges)


main()
