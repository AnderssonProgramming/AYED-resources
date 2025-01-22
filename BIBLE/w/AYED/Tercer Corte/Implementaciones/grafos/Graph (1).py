from sys import stdin
import math
import queue
#Colors
WHITE = 'white'
BLACK = 'black'
GRAY = 'gray'

class GraphL:
    def __init__(self,vertexes, arcs):
        self.V = {}
        for v in vertexes:
            self.V[v] = self.initializeVertex()
        self.E = {}
        #Hay un espacio por cada vertice
        for v in self.V:
            self.E[v] = []

        for arc in arcs:
            self.E[arc[0]].append(arc[1])

    def initializeVertex(self):
        return {
            'color': WHITE,
            'distance': math.inf,
            'final_time': math.inf,
            'phi': None
        }

    def BFS(self, s):
        for vertex in self.V.keys():
            self.V[vertex] = self.initializeVertex()
            if vertex == s:
                self.V[vertex]['color'] = GRAY
                self.V[vertex]['distance'] = 0
        Q = queue.Queue()
        Q.put(s)
        while Q.qsize() > 0:
            vertex = Q.get()
            vertexObj = self.V[vertex]
            for neighbor in self.getNeighbors(vertex):
                neighborObj = self.V[neighbor]
                if neighborObj['color'] == WHITE:
                    self.V[neighbor]['color'] = GRAY
                    self.V[neighbor]['distance'] = vertexObj['distance'] + 1
                    self.V[neighbor]['phi'] = vertex
                    Q.put(neighbor)
            self.V[vertex]['color'] = BLACK
        return self.V

    def DFS_VISIT(self, u, time):
        time = time + 1
        self.V[u]['distance'] = time
        self.V[u]['color'] = GRAY
        for v in self.getNeighbors(u):
            if self.V[v]['color'] == WHITE:
                self.V[v]['phi'] = u
                time = self.DFS_VISIT(v, time)
        self.V[u]['color'] = BLACK
        time = time + 1
        self.V[u]['final_time'] = time
        return time

    def DFS(self):
        for v in self.V.keys():
            self.V[v]['color'] = WHITE
            self.V[v]['phi'] = None
        time = 0
        for v in self.V.keys():
            if self.V[v]['color'] == WHITE:
                self.DFS_VISIT(v, time)
        return self.V

    def printCurrentState(self, result):
        for vertex in result.keys():
            print(vertex, result[vertex])


    def getVertexes(self):
        return self.V

    def getArcs(self):
        return self.E

    def getNeighbors(self, v):
        return self.E[v]

    def printArcs(self):
        for v in self.E.keys():
            print(v, self.E[v])

    def isStartingPoint(self, v):
        return self.V[v]['phi'] == None


class Graph:
    def __init__(self,vertexes, arcs):
        self.V = set(vertexes)
        self.E = [[ 0 for i in range(len(self.V))] for j in range(len(self.V))]
        for arc in arcs:
            self.E[arc[0]][arc[1]] = 1

    def getVertexes(self):
        return self.V

    def getArcs(self):
        return self.E

    def getNeighbors(self, v):
        neighbors = []
        candidates = self.E[v]
        for vertex in range(len(candidates)):
            if candidates[vertex] == 1:
                neighbors.append(vertex)
        return neighbors

    def printArcs(self):
        for line in self.E:
            print(''.join(map(str,line)))



def main():
    n,m = list(map(int, stdin.readline().strip().split()))
    arcs = []
    vertexes = [ i for i in range(n)]
    for i in range(m):
        pair = list(map(int, stdin.readline().strip().split()))
        arcs.append(pair)
    print(vertexes, arcs)
    g1 = Graph(vertexes, arcs)
    print("============================ Adj Matrix =======================")
    g1.printArcs()
    print("============================ Getting neighbors 0 =======================")
    print(g1.getNeighbors(0))
    g2 = GraphL(vertexes, arcs)
    print("============================ Adj List =======================")
    g2.printArcs()
    print("============================ Getting neighbors 0 =======================")
    print(g2.getNeighbors(0))
    print("============================ BFS 0 ====================================")
    g2.printCurrentState(g2.BFS(0))
    print("============================ BFS 2 ====================================")
    g2.printCurrentState(g2.BFS(2))
    print("============================ DFS ====================================")
    currentState = g2.DFS()
    g2.printCurrentState(currentState)
    startingPoints = []
    for v in currentState.keys():
        if g2.isStartingPoint(v):
            startingPoints.append(v)
    for startingPoint in startingPoints:
        print('=================== BFS', startingPoint, '=======================')
        g2.printCurrentState(g2.BFS(startingPoint))


main()
'''
13 17
0 1
0 7
1 2
1 3
2 5
3 4
5 4
5 6
6 2
7 8
7 11
8 9
9 10
11 10
11 12
12 9
12 10
'''