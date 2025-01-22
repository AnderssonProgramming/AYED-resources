import DisjointSets as ds


def MST_Kruskal(G):
    mst = set([])
    dj = ds.DisjointSets(G.V)
    edges = [edge for edge in G.E]
    edges.sort(key=lambda e: (e[2], e[0], e[1]))
    for edge in edges:
        if dj.find_set(edge[0]) != dj.find_set(edge[1]):
            mst.add(edge)
            dj.union_find(edge[0], edge[1])
    return mst
