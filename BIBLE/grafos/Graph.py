from sys import stdin
import queue
import math

WHITE = 'white'
BLACK = 'black'
GRAY = 'gray'


# Adj Matrix
class Graph:
    def __init__(self, vertexes, arcs):
        self.V = set([e for e in vertexes])
        self.E = set(arcs)
        self.SS_Values = {}
        self._composeAdjMatrix(arcs)
        self._composeAdjList(arcs)

    def getSSValues(self):
        return self.SS_Values

    def _initializeSS(self, s):
        for v in self.V:
            self.SS_Values[v] = {
                "color": WHITE,
                "distance": math.inf,
                "phi": None
            }
        self.SS_Values[s] = {
            "color": GRAY,
            "distance": 0,
            "phi": None
        }

    def getNeighbors_adjList(self, v):
        return self.adjList[v]
    def BFS_adjMatrix(self):
        matrix = self.getAdjMt()

    def BFS_adjList(self, s):
        # inicializar
        print(s)
        self._initializeSS(s)
        Q = queue.Queue()
        Q.put(s)
        while Q.qsize() > 0:
            u = Q.get()
            for v in self.getNeighbors_adjList(u):
                if self.SS_Values[v]['color'] == WHITE:
                    self.SS_Values[v]['color'] = GRAY
                    self.SS_Values[v]['distance'] = self.SS_Values[u]['distance'] + 1
                    self.SS_Values[v]['phi'] = u
                    Q.put(v)
            self.SS_Values[u]['color'] = BLACK

        return self.SS_Values

    def _composeAdjList(self, arcs):
        self.adjList = {}
        # AdjList
        for v in self.V:
            self.adjList[v] = set([])
        for e in arcs:
            st = self.adjList[e[0]]
            if e[1] not in st:
                st.add(e[1])

    def _composeAdjMatrix(self, arcs):
        self.adjMt = [[0 for e in range(len(self.V))] for w in range(len(self.V))]
        # AdjMatrix
        for e in arcs:
            self.adjMt[e[0]][e[1]] = 1

    def getAdjMt(self):
        return self.adjMt

    def getVertex(self):
        return self.V

    def getArcs(self):
        return self.E

    def printAdjMt(self):
        for row in self.adjMt:
            print(row)

    def printAdjList(self):
        for key in self.adjList.keys():
            print(key, self.adjList[key])


def composePath(v, answer):
    path = str(v)
    node = v
    while node is not None:
        node = answer[node]['phi']
        if node is not None:
            path = str(node) + '->' + path
    return path


def main():
    graph = Graph([e for e in range(7)], [(1, 2), (1, 4), (2, 5), (3, 5), (3, 6), (4, 2), (5, 4), (6, 6)])
    print("======================================== Adjacency Matrix ===================================")
    graph.printAdjMt()
    print("======================================== Adjacency List ===================================")
    graph.printAdjList()

    print("======================================== TEST BFS ===================================")
    V = [0, 1, 2, 3, 4, 5, 6, 7]
    E = [(0, 1), (0, 2), (1, 0), (2, 0), (2, 3),
         (3, 2), (3, 4), (3, 5), (4, 3), (4, 5),
         (4, 6), (5, 3), (5, 4), (5, 6), (5, 7),
         (6, 4), (6, 5), (6, 7), (7, 5), (7, 6)]

    graph = Graph(V, E)
    s = 0
    answer = graph.BFS_adjList(s)
    print('BFS from S=', s)
    for v in answer.keys():
        print(v, ':', answer[v], composePath(v, answer))

    print("======================================== TEST BFS Matrix ===================================")
    graph = Graph(V, E)
    graph.BFS_adjMatrix()
main()
