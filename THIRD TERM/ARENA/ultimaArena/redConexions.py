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
    cases = int(stdin.readline().strip())
    blank = stdin.readline().strip()
    for i in range(cases):
        computers = int(stdin.readline().strip())
        aff = 0
        neg = 0
        dj = DisjointSets([str(x+1) for x in range(computers)])
        ins = stdin.readline().strip().split()
        while ins:
            if ins[0] == "c":
                dj.union(ins[1],ins[2])
            elif ins[0] == "q":
                connection = dj.findSet(str(ins[1]))
                if str(ins[2]) in connection:
                    aff += 1
                else:
                    neg += 1

            ins = stdin.readline().strip().split()
        print(str(aff)+","+str(neg))
        print(blank)


main()