import random
import math

WHITE = "white"
BLACK = "black"
GRAY = "gray"


class Graph:
    def _buildAdjMatrix(self):
        self.adjMat = [[0 for _ in range(len(self.vertexes))] for _ in range(len(self.vertexes))]
        for relation in self.relations:
            row, col = self.encoder[relation[0]], self.encoder[relation[1]]
            self.adjMat[row][col] = 1

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
        time += 1
        self.v_props[vertex]['distance'] = time
        self.v_props[vertex]['color'] = GRAY
        for neighbor in self._getNeighborsMatAdj(vertex):
            if self.v_props[neighbor]['color'] == WHITE:
                self.v_props[neighbor]['parent'] = vertex
                time = self.dfs_visit(neighbor, time)
        self.v_props[vertex]['color'] = BLACK
        time += 1
        self.v_props[vertex]['final'] = time
        return time


class HashTableLinkedList:
    def __init__(self, size):
        self.elements = [[] for _ in range(size)]

    def getElements(self):
        return self.elements

    def printElements(self):
        for index in range(len(self.elements)):
            print(index, ': ', self.elements[index])

    def hash(self, key):
        return hash(key) % len(self.elements)

    def assign(self, index, element):
        self.elements[index].append(element)

    def insert(self, key, value):
        index = self.hash(key)
        self.assign(index, (key, value))

    def search(self, key):
        index = self.hash(key)
        for e in self.elements[index]:
            if e[0] == key:
                return e[1]
        return None

    def update(self, key, value):
        index = self.hash(key)
        for e in self.elements[index]:
            if e[0] == key:
                e[1] = value

    def delete(self, key):
        index = self.hash(key)
        element = self.search(key)
        if element:
            self.elements[index].remove(element)


class HashTableBinarySearch:
    def __init__(self, size):
        self.elements = [[] for _ in range(size)]

    def getElements(self):
        return self.elements

    def printElements(self):
        for index in range(len(self.elements)):
            print(index, ': ', self.elements[index])

    def hash(self, key):
        return hash(key) % len(self.elements)

    def assign(self, index, element):
        self.elements[index].append(element)
        self.elements[index].sort(key=lambda x: x[0])

    def insert(self, key, value):
        index = self.hash(key)
        if not self.elements[index]:
            self.elements[index].append((key, value))
        else:
            left, right = 0, len(self.elements[index]) - 1
            while left <= right:
                mid = (left + right) // 2
                if self.elements[index][mid][0] == key:
                    self.elements[index][mid] = (key, value)
                    return
                elif self.elements[index][mid][0] < key:
                    left = mid + 1
                else:
                    right = mid - 1
            self.elements[index].insert(left, (key, value))

    def search(self, key):
        index = self.hash(key)
        left, right = 0, len(self.elements[index]) - 1
        while left <= right:
            mid = (left + right) // 2
            if self.elements[index][mid][0] == key:
                return self.elements[index][mid][1]
            elif self.elements[index][mid][0] < key:
                left = mid + 1
            else:
                right = mid - 1
        return None

    def update(self, key, value):
        index = self.hash(key)
        for i, e in enumerate(self.elements[index]):
            if e[0] == key:
                self.elements[index][i] = (key, value)
                return

    def delete(self, key):
        index = self.hash(key)
        for e in self.elements[index]:
            if e[0] == key:
                self.elements[index].remove(e)
                return


class HashTableDepth:
    def __init__(self, size, depth):
        self.elements = [[] for _ in range(size)]
        self.depth = depth

    def getElements(self):
        return self.elements

    def printElements(self):
        for index in range(len(self.elements)):
            print(index, ': ', self.elements[index])

    def hash(self, key):
        return hash(key) % len(self.elements)

    def assign(self, index, element):
        self.elements[index].append(element)

    def insert(self, key, value):
        index = self.hash(key)
        self.assign(index, (key, value))

    def search(self, key):
        index = self.hash(key)
        for e in self.elements[index]:
            if e[0] == key:
                return e[1]
        return None

    def update(self, key, value):
        index = self.hash(key)
        for e in self.elements[index]:
            if e[0] == key:
                e[1] = value

    def delete(self, key):
        index = self.hash(key)
        element = self.search(key)
        if element:
            self.elements[index].remove(element)


class DisjointSets:

    def __init__(self, A):
        self.sets = [set([x]) for x in A]

    def getSets(self):
        return self.sets

    def findSet(self, x):
        for si in self.sets:
            if x in si:
                return si
        return None

    def makeSet(self, x):
        if self.findSet(x) is None:
            self.sets.append(set([x]))
            return self.sets[len(self.sets) - 1]
        return self.findSet(x)

    def union(self, x, y):
        s1 = self.findSet(x)
        s2 = self.findSet(y)

        if s1 is None:
            s1 = self.makeSet(x)
        if s2 is None:
            s2 = self.makeSet(y)
        if s1 != s2:
            s3 = s1.union(s2)
            self.sets.remove(s1)
            self.sets.remove(s2)
            self.sets.append(s3)

    def connectedComponents(self, Arcs):
        for e in Arcs:
            self.union(e[0], e[1])
        result = []
        for si in self.sets:
            if len(si) > 1:
                result.append(si)
        return result


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
    while v_props[current]['parent'] is not None:
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


def main(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        n = int(lines[0].strip())
        print("Para n =", n)

        # Construir el grafo de paradas de buses
        bus_stops = set([x for x in range(n)])
        routes = []
        for line in lines[1:]:
            routes.append(tuple(map(int, line.strip().split())))
        graph = Graph(bus_stops, routes, False)

        # Mostrar la lista de adyacencias y la matriz de adyacencias del grafo
        print("================ Graph ================")
        printAdjList(graph)
        printAdjMatrix(graph)

        # Ejecutar BFS y DFS sobre el grafo
        print("================ BFS and DFS ================")
        print("================ BFS ===================")
        bfs_result = graph.bfs()
        printVProps(bfs_result)
        print("================ DFS ===================")
        dfs_result = graph.dfs()
        printVProps(dfs_result)

        # Encontrar componentes conectados en el grafo
        print("================ Connected Components ================")
        result_bfs = graph.bfs()
        if checkIfConnectedComponent(result_bfs):
            print("================ Connected component found ===========================")
            printVProps(result_bfs)

        # Crear y mostrar la Tabla Hash con Linked List
        print("================ Hash Table with Linked List ================")
        hashtable_ll = HashTableLinkedList(13)
        for i in range(n):
            hashtable_ll.insert(i, random.random())
        hashtable_ll.printElements()

        # Crear y mostrar la Tabla Hash con Búsqueda Binaria
        print("================ Hash Table with Binary Search ================")
        hashtable_bs = HashTableBinarySearch(13)
        for i in range(n):
            hashtable_bs.insert(i, random.random())
        hashtable_bs.printElements()

        # Crear y mostrar la Tabla Hash con Profundidad
        print("================ Hash Table with Depth ================")
        hashtable_depth = HashTableDepth(13, 3)
        for i in range(n):
            hashtable_depth.insert(i, random.random())
        hashtable_depth.printElements()

        # Crear y mostrar los Conjuntos Disjuntos
        print("================ Disjoint Sets ================")
        dj = DisjointSets([x for x in range(n)])
        print('Initial State', dj.getSets())
        dj.makeSet(11)
        print('Adding new member', 11, dj.getSets())
        dj.makeSet(1)
        print('Adding Existing member', 1, dj.getSets())

        print('Find Set', 1, dj.findSet(1))
        print('Find Set', 10, dj.findSet(10))

        dj.union(1, 10)
        print('Union', 1, 10, dj.getSets())
        dj.union(1, 6)
        dj.union(10, 4)
        print('Unions', dj.getSets())

        # Determinar componentes conectados con los Conjuntos Disjuntos
        print("================ Connected Components with Disjoint Sets ================")
        V = [x for x in range(n)]
        E = routes  # Usamos las relaciones entre paradas como arcos
        dj2 = DisjointSets(V)
        connected_components = dj2.connectedComponents(E)
        print('Connected Components from G(V, E): ', connected_components)


file_path = "lab2.txt"  # Path del archivo de entrada
main(file_path)
