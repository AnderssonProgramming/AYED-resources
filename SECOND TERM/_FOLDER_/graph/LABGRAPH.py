from sys import stdin
import random

WHITE = "white"
BLACK = "black"
GRAY = "gray"
import math

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

    def __init__(self, v, e, directed=True, view=True):
        self.directed = directed
        self.view = view
        self.vertexes = v
        self._buildRelation(e)
        self._buildAdjList()
        self._buildEncoding()
        self._buildAdjMatrix()

    def getAdjMatrix(self):
        return self.adjMat

    def getAdjList(self):
        return self.adjList

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

    def _getNeighborsMatAdj(self, vertex):
        neighbors = []
        row = self.encoder[vertex]
        for col in range(len(self.adjMat[row])):
            if self.directed:
                if self.adjMat[row][col] == 1:
                    neighbors.append(self.decoder[col])
            else:
                if self.adjMat[row][col] == 1 or self.adjMat[col][row] == 1:
                    neighbors.append(self.decoder[col])
        return neighbors

    def bfs(self):
        self._buildVProps()
        for source in self.vertexes:
            if self.v_props[source]['color'] == WHITE:
                self.v_props[source]['color'] = GRAY
                self.v_props[source]['distance'] = 0
                self.v_props[source]['parent'] = None
                queue = [source]
                while queue:
                    u = queue.pop(0)
                    for neighbor in self._getNeighborsMatAdj(u):
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
        for neighbor in self._getNeighborsMatAdj(vertex):
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
    print()  # Salto de línea después de imprimir los resultados

def printAdjMatrix(graph):
    print("===================== ADJ Matrix =======================")
    adjMat = graph.getAdjMatrix()
    for row in adjMat:
        print(' '.join(list(map(str, row))))
    print()  # Salto de línea después de imprimir la matriz de adyacencia

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
    print()  # Salto de línea después de imprimir la lista de adyacencia

def checkIfConnectedComponent(result_bfs):
    amount_black = 0
    for e in result_bfs.keys():
        if result_bfs[e]['color'] == BLACK:
            amount_black += 1
    return amount_black > 1

def main():
    # Leer múltiples entradas desde el terminal
    for line in stdin:
        n = int(line.strip())
        print("Para n =", n)
        bus_stops = set([x for x in range(n)])
        # Crear rutas aleatorias dentro del rango de n
        routes = set()
        for i in range(n):
            for j in range(i + 1, n):
                if random.choice([True, False]):
                    routes.add((i, j))
        graph = Graph(bus_stops, routes, False)

        # Mostrar la lista de adyacencias y la matriz de adyacencias
        printAdjList(graph)
        printAdjMatrix(graph)

        # Ejecutar BFS y DFS
        print("====================== BFS ===================")
        printVProps(graph.bfs())
        print("====================== DFS ===================")
        printVProps(graph.dfs())

        # Encontrar componentes conectados
        print("====================== Connected components spread ===================")
        result_bfs = graph.bfs()
        if checkIfConnectedComponent(result_bfs):
            print("====================== Connected component found ===========================")
            printVProps(result_bfs)

        print()  # Salto de línea después de imprimir todo para este valor de n

main()
