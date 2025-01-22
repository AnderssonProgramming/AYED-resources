from sys import stdin
import math
import queue
#Colors
WHITE = 'white'
BLACK = 'black'
GRAY = 'gray'

VI = 0
VF = 1
W = 2


# Priority Queue
class PriorityQueue:
    def __init__(self, A, property_check=0, typeHeap= "Max"):
        self.heap = Heap(A, property_check, typeHeap)
        self.typeHeap = typeHeap

    def push(self, element):
        if self.typeHeap == "Max":
            self.heap.insertMax(element)
        else:
            self.heap.insertMin(element)

    def pop(self):
        element = self.heap.getRoot()
        if self.typeHeap == "Max":
            self.heap.deleteMax(element)
        else:
            self.heap.deleteMin(element)
        return element

    def __len__(self):
        return len(self.heap)

    def isempty(self):
        if len(self.heap) == 0:
            return True
        else:
            return False


class Heap:
    def __init__(self, A, property_check = 0, typeHeap = "Max"):
        self.property_check = property_check
        self.elements = []
        self.typeHeap = typeHeap
        if typeHeap == "Max":
            for e in A:
                self.insertMax(e)
        else:
            for e in A:
                self.insertMin(e)

    def getElements(self):
        return self.elements

    def left(self, i):
        return 2*i + 1

    def right(self, i):
        return 2*(i + 1)

    def height(self):
        return math.floor(math.log(len(self.elements), 2)) + 1

    def parent(self, i):
        return (i-1)//2 if i % 2 != 0 else (i//2 - 1)

    def buildMaxHeapify(self):
        for i in range(len(self.elements)//2, -1, -1):
            self.maxHeapify(i)

    def buildMinHeapify(self):
        for i in range(len(self.elements)//2, -1, -1):
            self.minHeapify(i)

    def getRoot(self):
        return self.elements[0]

    def insertMax(self, e):
        self.elements.append(e)
        self.buildMaxHeapify()

    def insertMin(self, e):
        self.elements.append(e)
        self.buildMinHeapify()

    def deleteMax(self, key):
        self.elements.remove(key)
        self.buildMaxHeapify()

    def deleteMin(self, key):
        self.elements.remove(key)
        self.buildMinHeapify()

    def updateMax(self, old_key, new_key):
        self.deleteMax(old_key)
        self.insertMax(new_key)

    def updateMin(self, old_key, new_key):
        self.deleteMin(old_key)
        self.insertMin(new_key)

    # Funcion que matiene la politca de la raiz mayor que sus hijos
    def maxHeapify(self, root):
        left, right, largest = self.left(root), self.right(root), root
        if left < len(self.elements) and self.elements[root][self.property_check] < self.elements[left][self.property_check]:
            largest = left
        if right < len(self.elements) and self.elements[largest][self.property_check] < self.elements[right][self.property_check]:
            largest = right
        if largest != root:
            self.elements[largest], self.elements[root] = self.elements[root], self.elements[largest]
            self.maxHeapify(largest)

    # Funcion que matiene la politca de la raiz mayor que sus hijos
    def minHeapify(self, root):
        left, right, largest = self.left(root), self.right(root), root
        if left < len(self.elements) and self.elements[root][self.property_check] > self.elements[left][self.property_check]:
            largest = left
        if right < len(self.elements) and self.elements[largest][self.property_check] > self.elements[right][self.property_check]:
            largest = right
        if largest != root:
            self.elements[largest], self.elements[root] = self.elements[root], self.elements[largest]
            self.minHeapify(largest)

    def __len__(self):
        return len(self.elements)


    # min journey
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
            self.E[arc[VI]].append((arc[VF], arc[W]))

    def initializeVertex(self):
        return {
            'color': WHITE,
            'distance': math.inf,
            'final_time': math.inf,
            'phi': None
        }

    def initializeSingleSource(self, s):
        for v in self.V.keys():
            self.V[v] = self.initializeVertex()
        self.V[s]['distance'] = 0

    def relax(self, arc):
        if self.V[arc[VF]]['distance'] > self.V[arc[VI]]['distance'] + arc[W]:
            self.V[arc[VF]]['distance'] = self.V[arc[VI]]['distance'] + arc[W]
            self.V[arc[VF]]['phi'] = arc[VI]

    def extractMin(self, visited):
        min, u = math.inf, None
        for v in self.V.keys():
            if v not in visited and min > self.V[v]['distance']:
                min, u = self.V[v]['distance'], v
        return u

    def extractMin_priority_queue(self, visited, u):
            pq = PriorityQueue(self.getNeighbors(u), 1,"Min")
            print(pq.isempty())
            if not pq.isempty():
                return pq.pop()[0]

    def dijkstra_priority_queue(self, s):
        self.initializeSingleSource(s)
        pq = PriorityQueue(self.getNeighbors(s), 1, "Min")
        u = s
        while not pq.isempty():
            for arc in self.getNeighbors(u):
                pq.push(arc)
                self.relax((u, arc[VI], arc[VF]))
            u = pq.pop()[0]

        return self.V

    def dijkstra(self, s):
        self.initializeSingleSource(s)
        visited = set()
        processedVertex = [ v for v in self.V.keys() ]
        while len(processedVertex) > 0:
            u = self.extractMin(visited)
            processedVertex.remove(u)
            visited = visited.union(set([u]))
            for arc in self.getNeighbors(u):
                self.relax((u, arc[VI], arc[VF]))
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

    def getArcsAsTriplets(self):
        arcs = []
        for key in self.E.keys():
            for rel in self.E[key] :
                arcs.append((key, rel[VI], rel[VF]))
        return arcs

    def bellmanFord(self, s):
        self.initializeSingleSource(s)
        #Relax all arcs |V| - 1 times, assuming a dense graph
        for i in range(len(self.V.keys())-1):
            for arc in self.getArcsAsTriplets():
                self.relax(arc)
        #Verify negative value cycles
        for arc in self.getArcsAsTriplets():
            if self.V[arc[VF]]['distance'] > self.V[arc[VI]]['distance'] + arc[W]:
                return None
        return self.V

def main():
    n, m = list(map(int, stdin.readline().strip().split()))
    arcs = []
    vertexes = [ i for i in range(n)]
    for i in range(m):
        pair = list(map(int, stdin.readline().strip().split()))
        arcs.append(pair)
    print(vertexes, arcs)
    g2 = GraphL(vertexes, arcs)
    print("============================ Adj List =======================")
    g2.printArcs()
    print("============================ BellMan Ford =======================")
    g2.printCurrentState(g2.bellmanFord(0))
    print("============================ Dijkstra =======================")
    g2.printCurrentState(g2.dijkstra(0))
    print("============================ Dijkstra Queue =======================")
    g2.printCurrentState(g2.dijkstra_priority_queue(0))


#main()
'''
5 5
0 1 1
0 2 10
1 3 2
2 3 -10
3 4 3
'''
'''
7 10
0 1 3
0 3 2
1 2 2
1 6 3
2 6 2
3 2 3
3 5 3
3 4 2
4 5 2
5 6 2 
'''