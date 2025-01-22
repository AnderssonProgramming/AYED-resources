import queue
import math
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
            self.data.append({x})
            return self.data[-1]
        return None

    def union_find(self, x, y):
        s1, s2 = self.find_set(x), self.find_set(y)

        if s1 is None :
            s1 = self.make_set(x)
        if s2 is None :
            s2 = self.make_set(y)

        if s1 != s2:
              s_union = s1.union(s2)
              self.data.remove(s1)
              self.data.remove(s2)
              self.data.append(s_union)

    def getData(self):
        return self.data


def adjlist(G):
    adjlist = {}
    for v in G["V"]:
        adjlist[v] = set([])
    for e in G["E"]:
        st = adjlist[e[0]]
        if e[1] not in st:
            st.add(e[1])
    return adjlist



def extract_min(cola):
    return (cola.get()[1])


def w(u,v,G):
    for arks in G["E"]:
        if arks[0] == u and arks[1] == v:
            return arks[2]


def search(v,cola):
    lista = list(cola.queue)
    for tuplex in lista:
        if tuplex[1] == v:
            return True
    return False


def actualizar(cola,v,peso):#arreglar
    lista = list(cola.queue)
    new_cola = queue.PriorityQueue()
    for i in range(len(lista)):
        if lista[i][1] == v:
            lista[i] = (peso,v)
            new_cola.put(lista[i])
        else:
            new_cola.put(lista[i])
    return new_cola


def MST_prim(G,r):
    cola = queue.PriorityQueue()
    adjlist_1 = adjlist(G)
    for node in G["V"]:
        if node == r:
            G["V"][node] = {
                "key": 0,
                "phi": None
            }
            cola.put((0, node))
        else:
            G["V"][node] = {
                "key": math.inf,
                "phi": None
            }
            cola.put((math.inf, node))
    while cola.qsize() > 0:
        u = extract_min(cola)#O(n) -> O(log(n))
        for v in adjlist_1[u]:
            peso = w(u,v,G)
            if search(v,cola) and G["V"][v]["key"] > peso:
                G["V"][v]["phi"] = u
                G["V"][v]["key"] = peso
                cola = actualizar(cola,v,peso)
    mst = set([])
    for i in range(1,len(G["V"])):
        mst.add((G["V"][i]["phi"], i, G["V"][i]["key"]))
    return mst



def MST_Kruskal(G):
    mst = set([])
    dj = DisjointSets(G['V'])
    edges = [ edge for edge in G['E']]
    edges.sort(key = lambda e: (e[2], e[0], e[1]))
    for edge in edges:
        if dj.find_set(edge[0]) != dj.find_set(edge[1]):
            mst.add(edge)
            dj.union_find(edge[0], edge[1])
    return mst

def determine_connected_components(V, E):
    cd, components = DisjointSets(V), []
    print('Initial state of disjoint-set', cd.getData())
    for e in E:
        cd.union_find(e[0], e[1])
        print('Procesing ', e, ' into disjoint-set:', cd.getData())
    print('Final state of disjoint-set', cd.getData())

    for com in cd.getData():
        if len(com) > 1:
            components.append(com)
    return components

def main():

    V = [ x for x in range(5)]
    E = [(0,1,9), (0,2,75), (1,0,9), (1,2,95),
         (1,3,19), (1,4,42), (2,0,75), (2,1,95),
         (2,3,51), (3,2,51),(3,1,19), (3,4,31),
         (4,1,42), (4,3,31)]
    #print('Connected components from G(V,E) are:', determine_connected_components(V, E))
    G = {
        'V': V,
        'E': E
    }
    print('MST-Krustal from G(V,E) are:', MST_Kruskal(G))
    r = G["V"][0]
    print('MST-Prim from G(V,E) are:', MST_prim(G,r))
    V = [x for x in range(6)]
    E = [(0,1,10),(0,3,5),(1,2,3),(3,4,100),(4,5,5)]
    G = {
        "V":V,
        "E":E
    }
    print('MST-Krustal from G(V,E) are:', MST_Kruskal(G))
    r = G["V"][0]
    print('MST-Prim from G(V,E) are:', MST_prim(G, r))
main()

