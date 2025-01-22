import Graphs as gr
import SpanningTrees as st
from random import randint
from Heaps import *
from sys import stdin

WHITE, BLACK, GRAY = 'white', 'black', 'gray'


class Ruta(gr.Graph):

    def __init__(self, V, E):
        self.V = set(V)
        self.E = set(E)
        self.adjList = self.composeAdjList()
        self.adjMatrix = self.composeAdjMatrix()
        self.pedidos = self.crearPedidos(V)

    def crearPedidos(self, V):
        self.pedidos = {}
        for i in V:
            self.pedidos[i] = {"direccion": "", "nombre": "", "codigo": ""}
        return self.pedidos

    def nuevoPedido(self, direccion, nombre):
        if len(self.V) == 0:
            self.pedidos[0] = {"direccion": direccion, "nombre": nombre}
            self.V = self.V.union(set([0]))
            self.adjList = self.composeAdjList()
        else:
            key = len(self.V)
            self.E = self.crearArcos(key)
            self.pedidos[key] = {"direccion": direccion, "nombre": nombre}
            self.V = self.V.union(set([key]))
            self.adjList = self.composeAdjList()

    def crearArcos(self, key):
        for i in self.V:
            self.E = self.E.union(set([(i, key)]))
        return self.E

    def _crearArcos(self, key):
        for i in self.V:
            self.E = self.E.union(set([(i, key, randint(10, 10000))]))
        return self.E

    def _rutaMasCorta(self):
        """Solo por busqueda topologica"""
        values = self.BFSAdjList(0)
        return values

    def rutaMasCorta(self):
        print(st.MST_Kruskal(self))

    def _initializeSS(self, s):
        self.ss_values = {}
        for v in self.V:
            if v != s:
                self.ss_values[v] = {
                    'color': WHITE,
                    'distance': math.inf,
                    'phi': None,
                }
            else:
                self.ss_values[v] = {
                    'color': GRAY,
                    'distance': 0,
                    'phi': None,
                }

    def topologicalSort(self):
        visited = [False] * len(self.V)
        stack = []

        for i in range(len(self.V)):
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)

        print(stack[::-1])

    def topologicalSortUtil(self, v, visited, stack):
        visited[v] = True
        for i in self.adjList[v]:
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)
        stack.append(v)

    def dijkstra_pq(self, s):
        dj = self.dijkstra_priority_queue(s)
        for i in dj:
            print(str(i) + ":", self.printPath(i, dj), "Distancia:", dj[i]['distance'])

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


def composePath(v, answer):
    path = str(v)
    node = v
    while node is not None:
        node = answer[node]['phi']
        if node is not None:
            path = str(node) + '->' + path
    return path


def main():
    opc = ''
    while opc != '4':
        print("RUTAS EFICIENTES")
        print("1. Enviar pedido sin distancias. (BFS-DFS-Disyuntos)")
        print("2. Enviar pedido con distancias. (Arboles Expansión Minimo)")
        print("3. Recoger y enviar pedido con distancias. (Caminos Minimos)")
        print("4. Salir.")
        opc = input("--->")
        if opc == '1':
            print("Ingrese los datos:")
            V = list(map(int, stdin.readline().strip().split()))
            E = []
            for i in range(len(V)):
                arc = list(map(int, stdin.readline().strip().split()))
                E.append(tuple(arc))
            ruta = Ruta(V, E)
            answer = ruta.BFSAdjList(0)
            print("Ruta mas eficiente (BFS)")
            for v in answer.keys():
                print(v, ':', composePath(v, answer))
            print("Etiquetas de orden envio (DFS - Topological Sort)")
            ruta.topologicalSort()
            enter = input()
        elif opc == '2':
            print("Ingrese los datos:")
            V = list(map(int, stdin.readline().strip().split()))
            E = []
            arc = list(map(int, stdin.readline().strip().split()))
            while arc:
                E.append(tuple(arc))
                arc = list(map(int, stdin.readline().strip().split()))
            ruta = Ruta(V, E)
            print("Ruta mas corta (Kruskal)")
            ruta.rutaMasCorta()
            enter = input()
        elif opc == '3':
            print("Ingrese los datos para recoger el paquete:")
            V = list(map(int, stdin.readline().strip().split()))
            E = []
            arc = list(map(int, stdin.readline().strip().split()))
            while arc:
                E.append(tuple(arc))
                arc = list(map(int, stdin.readline().strip().split()))
            rutaR = Ruta(V, E)
            print("Ruta para recoger de peso minimo (Dijkstra)")
            rutaR.dijkstra_pq(0)
            print()
            print("Ingrese los datos para enviar el paquete:")
            V = list(map(int, stdin.readline().strip().split()))
            E = []
            arc = list(map(int, stdin.readline().strip().split()))
            while arc:
                E.append(tuple(arc))
                arc = list(map(int, stdin.readline().strip().split()))
            rutaE = Ruta(V, E)
            bellman_ford = rutaE.bellman_ford(0)
            print("Ruta de envio de peso minimo (Bellman Ford)")
            rutaE.printResult(bellman_ford)
            enter = input()


main()

"""
Casos prueba
Enviar Pedido sin distancias
0 1 2 3 4 5
0 1
0 2
1 2
2 3
4 3
4 5

Enviar Pedido con distancias
0 1 2 3 4 5
0 1 3
0 2 5
1 2 3
2 3 8
4 3 0
4 5 1
1 2 4
1 4 2
5 3 2
2 4 6

Recoger y Enviar pedido con distancias
Datos recoger
0 1 2 3 4
0 1 1
0 2 10
1 3 2
2 3 12
3 4 3
Datos Envio
0 1 2 3 4 5
0 1 3
0 2 5
1 2 3
2 3 8
4 3 0
4 5 1
1 2 4
1 4 2
5 3 2
2 4 6
"""
