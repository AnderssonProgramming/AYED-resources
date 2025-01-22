import queue
from Heaps import *

WHITE, BLACK, GRAY = 'white', 'black', 'gray'


class Graph:

    def __init__(self, V, E):
        self.V = set(V)
        self.E = set(E)
        self.adjList = self.composeAdjList()
        self.adjMatrix = self.composeAdjMatrix()

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
            if v != s:
                self.ss_values[v] = {
                    'color': WHITE,
                    'distance': math.inf,
                    'phi': None
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
        for v in self.V:
            self.adjList[v] = set([])
        for e in self.E:
            self.adjList[e[0]].add(e[1])
        return self.adjList

    def composeAdjMatrix(self):
        self.adjMatrix = [[0 if (e, w) not in self.E else 1 for w in range(len(self.V))] for e in range(len(self.V))]
        return self.adjMatrix

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
        # Initialize Graph
        self._initializeAll()
        time = 0
        for u in self.V:
            if self.ss_values[u]['color'] == WHITE:
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
        u, v, w = e
        if self.ss_values[v]['distance'] > self.ss_values[u]['distance'] + w:
            self.ss_values[v]['distance'] = self.ss_values[u]['distance'] + w
            self.ss_values[v]['phi'] = u

    def printResult(self, result):
        for key in result.keys():
            print(str(key) + ":", self.printPath(key, result), "Distancia", result[key]['distance'])

    def printPath(self, ele, result):
        path, node = str(ele), ele
        while node is not None:
            node = result[node]['phi']
            if node is not None:
                path = str(node) + ' -> ' + path
        return path

    def printAdjList(self):
        for key in self.adjList.keys():
            print(key, self.adjList[key])

    def getNeighbors(self, v):
        list = []
        for i in self.E:
            if i[0] == v:
                list.append((i[1], i[2]))
        return list

    def dijkstra_priority_queue(self, s):
        self._initializeSS(s)
        pq = PriorityQueue(self.getNeighbors(s), 1, "Min")
        u = s
        while not pq.isempty():
            for arc in self.getNeighbors(u):
                pq.push(arc)
                self.relax((u, arc[0], arc[1]))
            u = pq.pop()[0]

        return self.ss_values