WHITE = "white"
BLACK = "black"
GRAY = "gray"
import math
import heapq


class Graph:
    def _buildAdjMatrix(self):
        self.adjMat = [[0 for v in range(len(self.vertexes))] for v in range(len(self.vertexes))]
        for relation in self.relations:
            row, col = self.encoder[relation[0]], self.encoder[relation[1]]
            self.adjMat[row][col] = 1

    def _buildEncoding(self):
        self.encoder, self.decoder = {}, {}
        index = 0
        for v in self.vertexes:
            self.encoder[v] = index
            self.decoder[index] = v
            index = index + 1

    def _buildAdjList(self):
        self.adjList = {}
        for v in self.vertexes:
            self.adjList[v] = []
        for relation in self.relations:
            self.adjList[relation[0]].append(relation[1])

    def _buildRelation(self, e):
        if self.directed:
            self.relations = e
        else:
            self.relations = set()
            for el in e:
                self.relations.add(el)
                if len(el) == 2:
                    self.relations.add((el[1], el[0]))
                else:
                    self.relations.add((el[1], el[0], e[2]))

    def _buildWeight(self):
        self._weight = {}  # (a,b) --> w
        for e in self.relations:
            if len(e) == 2:
                self._weight[e] = 1
            else:
                self._weight[(e[0], e[1])] = e[2]

    def __init__(self, v, e, directed=True, view=True):
        self.directed = directed
        self.view = view
        self.vertexes = v
        self._buildRelation(e)
        self._buildAdjList()
        self._buildEncoding()
        self._buildAdjMatrix()
        self._buildWeight()

    def getAdjMatrix(self):
        return self.adjMat

    def getAdjList(self):
        return self.adjList

    def relax(self, e):
        source, destination, weight = e[0], e[1], e[2]
        if self.v_props[destination]['distance'] > self.v_props[source]['distance'] + weight:
            self.v_props[destination]['distance'] = self.v_props[source]['distance'] + weight
            self.v_props[destination]['parent'] = source
            return True
        return False

    def dijkstra(self, s):
        self._buildVProps(s)
        Q = [(self.v_props[v]['distance'], v) for v in self.vertexes]
        heapq.heapify(Q)
        while len(Q) > 0:
            _, minimo_local = heapq.heappop(Q)
            for neighbor in self.getNeighbors(minimo_local):
                self.relax((minimo_local, neighbor, self._weight[(minimo_local, neighbor)]))
                # Reorganizar la cola de prioridad
                Q = [(self.v_props[v]['distance'], v) for _, v in Q]
                heapq.heapify(Q)
        return self.v_props

    def _buildVProps(self, source=None):
        self.v_props = {}
        for v in self.vertexes:
            self.v_props[v] = {
                'color': WHITE,
                'distance': math.inf,
                'parent': None
            }
        if source is not None:
            self.v_props[source] = {
                'color': GRAY,
                'distance': 0,
                'parent': None
            }

    def getNeighbors(self, vertex):
        if self.view:
            return self.adjList[vertex]
        return

    def bfs(self, source):
        self._buildVProps(source)
        queue = [source]
        while len(queue) > 0:
            u = queue.pop(0)
            for neighbor in self.getNeighbors(u):
                if self.v_props[neighbor]['color'] == WHITE:
                    self.v_props[neighbor]['color'] = GRAY
                    self.v_props[neighbor]['distance'] = self.v_props[u]['distance'] + 1
                    self.v_props[neighbor]['parent'] = u
                    queue.append(neighbor)
            self.v_props[u]['color'] = BLACK
        return self.v_props

    def dfs(self):
        self._buildVProps()
        time = 0
        for v in self.vertexes:
            if self.v_props[v]['color'] == WHITE:
                time = self.dfs_visit(v, time)
        return self.v_props

    def dfs_visit(self, vertex, time):
        time = time + 1
        self.v_props[vertex]['distance'] = time
        self.v_props[vertex]['color'] = GRAY
        for neighbor in self.getNeighbors(vertex):
            if self.v_props[neighbor]['color'] == WHITE:
                self.v_props[neighbor]['parent'] = vertex
                time = self.dfs_visit(neighbor, time)
        self.v_props[vertex]['color'] = BLACK
        time = time + 1
        self.v_props[vertex]['final'] = time
        return time


def printVProps(v_props):
    print("===================== Results =======================")
    for v in v_props.keys():
        v_props[v]['path'] = '-->'.join(map(str, getPath(v, v_props)))
        print(str(v), '-->', v_props[v])


def printAdjMatrix(graph):
    print("===================== ADJ Matrix =======================")
    adjMat = graph.getAdjMatrix()
    for row in adjMat:
        print(' '.join(list(map(str, row))))


def getPath(vertex, v_props):
    path = [vertex]
    current = vertex
    while (v_props[current]['parent'] is not None):
        path.insert(0, v_props[current]['parent'])
        current = v_props[current]['parent']
    return path


def printAdjList(graph):
    print("===================== ADJ List =======================")
    adjList = graph.getAdjList()
    for v in adjList.keys():
        print(str(v), list(map(str, adjList[v])))


def main():
    vertexes = set([x for x in range(9)])
    relations = set([(0, 1), (0, 2), (2, 3), (1, 3),
                     (3, 4), (3, 5), (4, 5), (5, 4),
                     (6, 7), (7, 8), (6, 8)
                     ])
    graph = Graph(vertexes, relations, True)
    printAdjList(graph)
    printAdjMatrix(graph)
    print("====================== BFS S=0 ===================")
    printVProps(graph.bfs(0))
    print("====================== BFS S=3 ===================")
    printVProps(graph.bfs(3))
    print("====================== DFS ===================")
    result = graph.dfs()
    printVProps(result)
    print("====================== Connected components spread ===================")
    for v in result.keys():
        if result[v]['parent'] is None:
            printVProps(graph.bfs(v))
    vertexes = set(["s", "t", "y", "x", "z"])
    relations = set([("s", "y", 5), ("s", "t", 10),
                     ("t", "y", 2), ("t", "x", 1),
                     ("y", "t", 3), ("y", "x", 9),
                     ("y", "z", 2), ("x", "z", 4),
                     ("z", "x", 6), ("z", "s", 7)
                     ])
    graphw = Graph(vertexes, relations)

    print("====================== Dijkstra ===================")
    printVProps(graphw.dijkstra("s"))


main()
