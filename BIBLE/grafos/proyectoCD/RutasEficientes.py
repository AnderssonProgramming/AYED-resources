import Graphs as gr
import DisjointSets as ds
import SpanningTrees as st
from random import randint
import math
from collections import defaultdict

WHITE, BLACK, GRAY = 'white', 'black', 'gray'

class Ruta(gr.Graph):

    def __init__(self, V, E):
        self.V = set(V)
        self.E = set(E)
        self.adjList = self.composeAdjList()
        self.adjMatrix = self.composeAdjMatrix()
        self.pedidos = self.crearPedidos(V)


    def _rutaMasCorta(self):
        values = self.BFSAdjList(0)
        return values

    def _initializeSS(self, s):
        self.ss_values = {}
        for v in self.V:
            if v != s :
                self.ss_values[v] = {
                    'color' : WHITE,
                    'distance': math.inf,
                    'phi' : None,
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
            if not visited[i]:
                self.topologicalSortUtil(i, visited, stack)

        print(stack[::-1])

    def topologicalSortUtil(self, v, visited, stack):
        visited[v] = True
        for i in self.adjList[v]:
            if not visited[i]:
                self.topologicalSortUtil(i, visited, stack)
        stack.append(v)

def composePath(v, answer):
    path = str(v)
    node = v
    while node is not None:
        node = answer[node]['phi']
        if node is not None:
            path = str(node) + '->' + path
    return path

def main():
    ruta2 = Ruta([0, 1, 2, 3, 4, 5], [(0, 1), (0, 2), (1, 2), (2, 3), (4, 3), (4, 5)])

    answer = ruta2.BFSAdjList(0)
    for v in answer.keys():
        print(v, ':', composePath(v, answer))
    print("--------------------------------------------------------")
    ruta2.topologicalSort()
