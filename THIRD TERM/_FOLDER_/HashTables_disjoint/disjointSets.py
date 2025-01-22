from sys import stdin


class DisjointSets:

    def __init__(self, A):
        self.sets = [set([x]) for x in A]

    def getSets(self):
        return self.sets

    def findSet(self, x):
        for si in self.sets:
            if x in si:
                return si
        return None

    def makeSet(self, x):
        if self.findSet(x) is None:
            self.sets.append(set([x]))
            return self.sets[len(self.sets)-1]
        return self.findSet(x)

    def union(self, x, y):
        s1 = self.findSet(x)
        s2 = self.findSet(y)

        if s1 is None:
            s1 = self.makeSet(x)
        if s2 is None:
            s2 = self.makeSet(y)
        if s1 != s2:
            s3 = s1.union(s2)
            self.sets.remove(s1)
            self.sets.remove(s2)
            self.sets.append(s3)

    def connectedComponents(self, Arcs):
        for e in Arcs:
            self.union(e[0], e[1])
            print('After processing arc', e, self.sets)
        result = []
        for si in self.sets:
            if len(si) > 1:
                result.append(si)
        return result

def main():
    dj = DisjointSets([ x for x in range(11)] )
    print('Initial State', dj.getSets())
    dj.makeSet(11)
    print('Adding new member', 11, dj.getSets())
    dj.makeSet(1)
    print('Adding Existing member', 1, dj.getSets())

    print('Find Set', 1, dj.findSet(1))
    print('Find Set', 10, dj.findSet(10))

    dj.union(1,10)
    print('Union',1,10, dj.getSets())
    dj.union(1, 6)
    dj.union(10, 4)
    print('Unions', dj.getSets())
    #Process Graph to determine connected components
    n = list(map(int, stdin.readline().strip().split()))
    V = [ x for x in range(n[0])]
    E = []
    for arc in range(n[1]):
        E.append(list(map(int, stdin.readline().strip().split())))
    print(V,E)
    dj2 = DisjointSets(V)
    result = dj2.connectedComponents(E)
    print('Connected Components from G(V, E): ', result)

main()