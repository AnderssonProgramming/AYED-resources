from sys import stdin

class DisjointSets:

    def __init__(self):
        self.sets = []

    def getSets(self):
        return self.sets

    def findSet(self, x):
        for si in self.sets:
            if x in si:
                return si
        return None

    def makeSet(self, x):
        if self.findSet (x) is None:
            self.sets.append (set ([x]))
            return self.sets[len (self.sets) - 1]
        return self.findSet (x)

    def union(self, x, y):
        s1 = self.findSet (x)
        s2 = self.findSet (y)

        if s1 is None:
            s1 = self.makeSet (x)
        if s2 is None:
            s2 = self.makeSet (y)
        if s1 != s2:
            s3 = s1.union (s2)
            self.sets.remove (s1)
            self.sets.remove (s2)
            self.sets.append (s3)

    def connectedComponents(self, Arcs):
        for e in Arcs:
            self.union (e[0], e[1])
            #print ('After processing arc', e, self.sets)
        result = []
        for si in self.sets:
            if len (si) > 1:
                result.append (si)
        return result

def main():

    n = int(stdin.readline().strip())
    arcs = []

    for i in range(n):
        a, b = map(int,stdin.readline().strip().split())
        arcs.append((a,b))

    dj = DisjointSets()
    result = dj.connectedComponents(arcs)

    combination = list(map(len,result))

    print(min(combination),max(combination))

main()