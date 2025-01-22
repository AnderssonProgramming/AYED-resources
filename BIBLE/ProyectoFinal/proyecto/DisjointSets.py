class DisjointSets:

    def __init__(self, data=None):
        self.data = []
        if data is not None:
            for e in data:
                self.make_set(e)

    def find_set(self, x):
        for e in self.data:
            if x in e:
                return e
        return None

    def make_set(self, x):
        st = self.find_set(x)
        if st is None:
            self.data.append(set([x]))
            return self.data[-1]
        return None

    def union_find(self, x, y):
        s1, s2 = self.find_set(x), self.find_set(y)

        if s1 is None:
            s1 = self.make_set(x)
        if s2 is None:
            s2 = self.make_set(y)

        if s1 != s2:
            s_union = s1.union(s2)
            self.data.remove(s1)
            self.data.remove(s2)
            self.data.append(s_union)
