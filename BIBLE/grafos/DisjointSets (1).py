
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
    print(dj.getData())
    for e in E:
        dj.union_find(e[0], e[1])
        print('Processing', e, 'with result', dj.getData())

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

def main():
    vertexes = [ x for x in range(5)]
    arcs = [
        (0,1,4), (0,2,4), (0,3,6), (0,4,6),
        (1,2,2), (1,0,4), (2,3,8), (2,1,2),
        (2,0,4), (3,0,6), (3,2,8), (3,4,9),
        (4,0,6), (4,3,9)
    ]
    #print(connected_components(vertexes, arcs))
    print(MST_Kruskal({
        'V': vertexes,
        'E': arcs
    }))


main()