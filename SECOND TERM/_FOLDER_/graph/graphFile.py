WHITE = "white"
BLACK = "black"
GRAY = "gray"
import math


class Graph:
    def _buildAdjMatrix(self):
        self.adjMat = [[0 for v in range(len(self.vertexes))] for v in range(len(self.vertexes))]  #V2
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
                # Para evitar la bidireccionalidad, solo agregamos la relación en una dirección
                self.relations.add(el)
                #self.relations.add ((el[1], el[0]))
    def __init__(self, v, e, directed=True, view=True):
        self.directed = directed
        self.view = view  # Si True estoy usando listas de adyacencias / False, debo usar la matriz de adyacencias
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

    def _getNeighborsAdjList(self, vertex):
        return self.adjList[vertex]

    def _getNeighborsMatAdj(self,vertex):
        neighbors = []
        row = self.encoder[vertex] # Obtiene el índice de la fila correspondiente al vértice en la matriz de adyacencia
        for col in range(len(self.adjMat[row])): # Itera a través de la fila correspondiente en la matriz de adyacencia
            if self.directed:
                # Si el grafo es dirigido, solo se consideran las conexiones desde el vértice dado hacia los vecinos.
                if self.adjMat[row][col] == 1:
                    neighbors.append(self.decoder[col])
            else:
                # Si el grafo no es dirigido, se consideran todas las conexiones del vértice dado, independientemente de la dirección.
                if self.adjMat[row][col] == 1 or self.adjMat[col][row] == 1:
                    neighbors.append(self.decoder[col])
        return neighbors

    def getNeighbors(self, vertex):
        if self.view:
            return self._getNeighborsAdjList(vertex)
            # Retornar los vecinos de forma correcta para la representación de la matriz de adyacencias
        return self._getNeighborsMatAdj(vertex)

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

def checkIfConnectedComponent(result_bfs):
    amount_black = 0
    for e in result_bfs.keys():
        if result_bfs[e]['color'] == BLACK:
            amount_black += 1
    return amount_black > 1


def main():
    vertexes = set([x for x in range(8)])
    relations = {(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (2, 5), (3, 4), (7, 6)}
    graph = Graph(vertexes, relations, False)
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
        if result[v]['parent'] is None:  #Determinar los puntos de arranque para BFS
            result_bfs = graph.bfs(v)
            if checkIfConnectedComponent(result_bfs):
                print("====================== Connected component found ", v, "==========================")
                printVProps(result_bfs)


main()
