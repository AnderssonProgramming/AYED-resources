import math
import heapq
from sys import stdin

WHITE = "white"
BLACK = "black"
GRAY = "gray"

class Graph:
    def _buildAdjMatrix(self):
        self.adjMat = [[math.inf for _ in range(len(self.vertexes))] for _ in range(len(self.vertexes))]
        for relation in self.relations:
            row, col, weight = self.encoder[relation[0]], self.encoder[relation[1]], relation[2]
            self.adjMat[row][col] = weight

    def _buildEncoding(self):
        self.encoder, self.decoder = {}, {}
        index = 0
        for v in self.vertexes:
            self.encoder[v] = index
            self.decoder[index] = v
            index += 1

    def _buildAdjList(self):
        self.adjList = {}
        for v in self.vertexes:
            self.adjList[v] = []
        for relation in self.relations:
            self.adjList[relation[0]].append((relation[1], relation[2]))

    def _buildRelation(self, e):
        if self.directed:
            self.relations = e
        else:
            self.relations = set()
            for el in e:
                self.relations.add(el)
                if len(el) == 2:
                    self.relations.add((el[1], el[0], el[2]))  # Fixing this line
                else:
                    self.relations.add((el[1], el[0], el[2]))
                    self.relations.add((el[0], el[1], el[2]))

    def _buildWeight(self):
        self._weight = {}  # (a,b) --> w
        for e in self.relations:
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

    def relax(self, source, destination):
        if self.v_props[destination]['distance'] > self.v_props[source]['distance'] + self._weight[(source, destination)]:
            self.v_props[destination]['distance'] = self.v_props[source]['distance'] + self._weight[(source, destination)]
            return True
        return False

    def dijkstra(self, s, T):
        self._buildVProps(s)
        Q = [(0, s)]  # Heap for priority queue, (distance, vertex)
        while Q:
            dist, u = heapq.heappop(Q)
            if dist > T:
                break  # If the distance exceeds the time limit, no need to explore further
            if u == self.exit_cell:
                self.mice_reached_exit += 1  # Increment counter if the mouse reaches the exit
            for v, weight in self.adjList[u]:
                if self.relax(u, v):
                    heapq.heappush(Q, (self.v_props[v]['distance'], v))

    def _buildVProps(self, source):
        self.v_props = {}
        for v in self.vertexes:
            self.v_props[v] = {
                'distance': math.inf,
            }
        self.v_props[source]['distance'] = 0
        self.mice_reached_exit = 0

    def getMiceReachedExit(self):
        return self.mice_reached_exit

def predictMiceExit():
    # Read the number of test cases
    cases = int(stdin.readline().strip())
    output = []

    # Process each test case
    for _ in range(cases):
        stdin.readline()  # Skip blank line
        # Read N, E, T
        line = stdin.readline().strip().split()
        N, E, T = map(int, line)
        # Read M
        M = int(stdin.readline().strip())

        # If there's only one cell and it's the exit, no mice can exit
        if N == 1 and E == 1:
            output.append(0)
            # Skip connections for this case
            for _ in range(M):
                stdin.readline()
            continue

        # Read connections
        connections = [tuple(map(int, stdin.readline().split())) for _ in range(M)]

        # Build graph
        vertexes = set(range(1, N + 1))
        relations = connections
        graph = Graph(vertexes, relations)

        # Run Dijkstra's algorithm
        graph.exit_cell = E  # Add exit cell attribute to the graph
        graph.dijkstra(E, T)

        output.append(graph.getMiceReachedExit())

        stdin.readline()  # Skip blank line

    return output

# Test the function with the sample input
print(predictMiceExit())
