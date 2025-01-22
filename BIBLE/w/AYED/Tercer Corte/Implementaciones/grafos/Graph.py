from sys import stdin
import math
import queue
#Colors
WHITE = 'white'
BLACK = 'black'
GRAY = 'gray'

class GraphL:
    def __init__(self,vertexes, arcs):
        self.V = set(vertexes)
        self.E = {}
        #Hay un espacio por cada vertice
        for v in self.V:
            self.E[v] = []

        for arc in arcs:
            self.E[arc[0]].append(arc[1])

    def initializeVertex(self, v):
        return {
            'color': WHITE,
            'distance': math.inf,
            'phi': None
        }


    def BFS(self, s):
        vertexDicc = {}
        for vertex in self.V:
            vertexDicc[vertex] = self.initializeVertex(vertex)
            if vertex == s:
                vertexDicc[vertex]['color'] = GRAY
                vertexDicc[vertex]['distance'] = 0
        Q = queue.Queue()
        Q.put(s)
        while Q.qsize() > 0:
            vertex = Q.get()
            vertexObj = vertexDicc[vertex]
            for neighbor in self.getNeighbors(vertex):
                neighborObj = vertexDicc[neighbor]
                if neighborObj['color'] == WHITE:
                    vertexDicc[neighbor]['color'] = GRAY
                    vertexDicc[neighbor]['distance'] = vertexObj['distance'] + 1
                    vertexDicc[neighbor]['phi'] = vertex
                    Q.put(neighbor)
            vertexDicc[vertex]['color'] = BLACK
        return vertexDicc

    def printBFSResult(self, result):
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
    g2.printBFSResult(g2.BFS(0))
    print("============================ BFS 2 ====================================")
    g2.printBFSResult(g2.BFS(2))

main()
'''
5 5
0 1
1 2
2 3
3 4
4 0
'''