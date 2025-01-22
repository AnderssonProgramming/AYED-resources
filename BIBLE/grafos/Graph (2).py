from sys import stdin
import math
import queue

WHITE = 'white'
BLACK = 'black'
GRAY = 'gray'

class Graph:

    def __init__(self, V, E):
        self.V = set(V)
        self.E = set(E)
        #print('==================== ADJ LIST =============================')
        self.composeAdjList()
        #print('==================== ADJ Matrix =============================')
        self.composeAdjMatrix()

    def _initializeAll(self):
        self.ss_values = {}
        for v in self.V:
                self.ss_values[v] = {
                    'color': WHITE,
                    'distance': math.inf,
                    'phi': None
                }

    def _initializeSS(self, s):
        self.ss_values = {}
        for v in self.V:
            if v != s :
                self.ss_values[v] = {
                    'color' : WHITE,
                    'distance': math.inf,
                    'phi' : None
                }
            else:
                self.ss_values[v] = {
                        'color': GRAY,
                        'distance': 0,
                        'phi': None
                    }




    def showAdjList(self):
        for k in self.adjList.keys():
            print(k, self.adjList[k])

    def showAdjMatrix(self):
        for row in self.adjMatrix:
            print(row)

    def composeAdjList(self):
        self.adjList = {}
        self.adjList_w = {}

        for v in self.V:
            self.adjList[v] = set([])
            self.adjList_w[v] = set([])

        for e in self.E:
            self.adjList[e[0]].add(e[1])
            self.adjList_w[e[0]].add(e)

        #self.showAdjList()

    def composeAdjMatrix(self):
        self.adjMatrix = [[ 0 if (e,w) not in self.E else 1 for w in range(len(self.V))] for e in range(len(self.V))]
        #self.showAdjMatrix()

    def _getNeighborsAdjMatrix(self, v):
        row, neighbors = self.adjMatrix[v], []
        for column in range(len(row)):
            if row[column] == 1:
                neighbors.append(column)
        return neighbors



    def BFSAdjMatrix(self, s):
        self._initializeSS(s)
        Q = queue.Queue()
        Q.put(s)
        while Q.qsize() > 0:
            u = Q.get()
            for v in self._getNeighborsAdjMatrix(u):
                if self.ss_values[v]['color'] == WHITE:
                    self.ss_values[v]['color'] = GRAY
                    self.ss_values[v]['distance'] = self.ss_values[u]['distance'] + 1
                    self.ss_values[v]['phi'] = u
                    Q.put(v)
            self.ss_values[u]['color'] = BLACK

        return self.ss_values

    def DFSAdjList_Visit(self, u, time):
        self.ss_values[u]['distance'] = time
        self.ss_values[u]['color'] = GRAY

        for v in self.adjList[u]:
            if self.ss_values[v]['color'] == WHITE:
                self.ss_values[v]['phi'] = u
                time = self.DFSAdjList_Visit(v, time + 1)

        self.ss_values[u]['color'] = BLACK
        self.ss_values[u]['final'] = time
        return time

    def DFSAdjList(self):
        #Initialize Graph
        self._initializeAll()
        time = 0
        for u in self.V:
            if self.ss_values[u]['color'] == WHITE :
                self.DFSAdjList_Visit(u, time)
        return self.ss_values

    def BFSAdjList(self, s):
        self._initializeSS(s)
        Q = queue.Queue()
        Q.put(s)
        while Q.qsize() > 0:
            u = Q.get()
            for v in self.adjList[u]:
                if self.ss_values[v]['color'] == WHITE:
                    self.ss_values[v]['color'] = GRAY
                    self.ss_values[v]['distance'] = self.ss_values[u]['distance'] + 1
                    self.ss_values[v]['phi'] = u
                    Q.put(v)
            self.ss_values[u]['color'] = BLACK

        return self.ss_values

    def relax(self, e):
        u,v,w = e
        if self.ss_values[v]['distance'] > self.ss_values[u]['distance'] + w:
            self.ss_values[v]['distance'] = self.ss_values[u]['distance'] + w
            self.ss_values[v]['phi'] = u

    def extract_min(self, visited):
        min_distance, u = math.inf, None
        for v in self.V:
            if v not in visited and min_distance > self.ss_values[v]['distance']:
                min_distance, u = self.ss_values[v]['distance'], v
        return u

    def bellman_ford(self, s):
        self._initializeSS(s)
        # Relajar V-1 veces los arcos
        for n in range(len(self.V)-1):
            for e in self.E:
                self.relax(e)
        # Confirmar ciclos o tendencias a -inf
        for e in self.E:
            u, v, w = e
            if self.ss_values[v]['distance'] > self.ss_values[u]['distance'] + w:
                return None
        return self.ss_values

    def dijkstra_SSP(self, s):
        self._initializeSS(s)
        visited = set()
        to_process = [ v for v in self.V ]
        while len(to_process) > 0:
            u = self.extract_min(visited)
            visited.add(u)
            to_process.remove(u)
            for e in self.adjList_w[u]:
                self.relax(e)
        return self.ss_values

    def printResult(self, result):
        for key in result.keys():
            print(key, result[key], self.printPath(key, result))

    def printPath(self, ele, result):
        path, node = str(ele), ele
        while node is not None:
            node = result[node]['phi']
            if node is not None:
                path = str(node) + ' -> ' + path
        return path

def main():
    g1 = Graph([ 0,1,2,3,4,5],
               [(0, 1), (0, 2), (1,2), (2,3), (3,1), (4,3), (4,5)]
               )
    bfs = g1.BFSAdjList(0)
    print('==================== BFS Analysis =============================')
    g1.printResult(bfs)

    bfs_mtx = g1.BFSAdjMatrix(0)
    print('==================== BFS Analysis =============================')
    g1.printResult(bfs_mtx)

    dfs = g1.DFSAdjList()
    print('==================== DFS Analysis =============================')
    g1.printResult(dfs)
    print('==================== SSP Analysis - BellmanFord =============================')
    g1 = Graph([0, 1, 2, 3, 4],
               [(0, 1, 1), (0, 2, 10), (1, 3, 2), (2, 3, -10), (3, 4, 3)]
               )
    bellman_ford = g1.bellman_ford(0)
    g1.printResult(bellman_ford)

    print('==================== SSP Analysis - Dijkstra =============================')
    g1 = Graph([0, 1, 2, 3, 4],
               [(0, 1, 1), (0, 2, 10), (1, 3, 2), (2, 3, -10), (3, 4, 3)]
               )
    dijkstra = g1.dijkstra_SSP(0)
    g1.printResult(dijkstra)


main()