from sys import stdin
import math
import queue


# DEFINIMOS ATRIBUTOS ESENCIALES PARA LA BUSQUEDA BFS Y DFS
WHITE = "white"
BLACK = "black"
GRAY = "gray"

# DEFINIMOS EL OBJETO GRAFO


class Graph:
    def __init__(self, vertices, arcos):
        # ATRIBUTOS VERTICE Y ARCOS SON UN CONJUNTO Y UN MATRIZ RESPECTIVAMENTE
        self.V = set(vertices)
        self.E = [[0 for i in range(len(self.V))] for j in range(len(self.V))]
        for arco in arcos:
            # RECORRIENDO CADA ARCO ASIGNAMOS LA RELACION ASI OBTENEMOS LA MATRIZ DE ADYACENCIA DEL GRAFO
            self.E[arco[0]][arco[1]] = 1

    def getNeightbors(self, v):
        # SELECCIONAR LOS CANDIDATOS DEL VERTICE DADO
        neightbors = []
        candidates = self.E[v]
        for vertice in range(len(candidates)):
            # RECORRER LOS POSIBLES CANDIDATOS Y SI EXIsTE LA RELACION AÑADIRLO A LOS VECINOS
            if candidates[vertice] == 1:
                neightbors.append(vertice)
        return neightbors


    def printArcs(self):
        # IMPRIME LA MATRIZ DE ADYACENCIA
        for line in self.E:
            print("".join(map(str,line)))


    # INICIALIZA EL VERTICE CON DIFERENTES ATRUBUTOS
    def intializeVertice(self, v):
        return {
            "value" : v,
            "color" : WHITE,
            "distancia": math.inf,
            "phi": None
        }


    def intializeVertice2(self):
        return {
            'color': WHITE,
            'distance': math.inf,
            'final_time': math.inf,
            'phi': None
        }


    # BUSQUEDA POR ANCHURA
    def BFS(self, s):
        verticeDicc = {}
        # RECORREOS TODOS LOS VERTICES EN EL CONJUNTO V Y LUEGO INICIALIZAMOS EL OBJETO VERTICE
        for vertice in self.V:
            verticeDicc[vertice] = self.intializeVertice(vertice)
            # CUANDO SE ENCUNTRE EL VERTICE CON EL VALOR ESPERADO LO MARCAMOS
            if vertice == s:
                verticeDicc[vertice]["color"] = GRAY
                verticeDicc[vertice]["distancia"] = 0

        # CREAMOS COLA DE VECINOS Y AÑADIMOS EL NODO INICIAL
        Q = queue.Queue()
        Q.put(s)
        # MIENTRAS LA COLA NO ESTE VACIA
        while Q.qsize() > 0:
            # TOMANDO EL VERTICE A PROCESAR Y TOMANDOLO COMO OBJETO
            vertice = Q.get()
            verticeObj = verticeDicc[vertice]
            # TOMAMOS TODOS LOS VECINOS UBICANDOLOS EN EL DICCIONARIO LOS MARCAMOS Y LOS AÑADIMOS A LA COLA
            for neightbor in self.getNeightbors(vertice):
                neightborObj = verticeDicc[neightbor]
                if neightborObj["color"] == WHITE:
                    verticeDicc[neightbor]["color"] = GRAY
                    verticeDicc[neightbor]["distancia"] = verticeObj["distancia"] + 1
                    verticeDicc[neightbor]["phi"] = vertice
                    Q.put(neightbor)
            verticeDicc[vertice]['color'] = BLACK
        return verticeDicc


    def printBFSResult(self, result):
        for vertice in result.keys():
            print(vertice, result[vertice])

    # RECORRIDO POR  PROFUNDIDAD
    def DFS_VISIT(self, u, time, verticeDicc):
        time = time + 1
        verticeDicc[u]['distance'] = time
        verticeDicc[u]['color'] = GRAY
        for v in self.getNeightbors(u):
            if verticeDicc[v]['color'] == WHITE:
                verticeDicc[v]['phi'] = u
                time = self.DFS_VISIT(v, time, verticeDicc)
        verticeDicc[u]['color'] = BLACK
        time = time + 1
        verticeDicc[u]['final_time'] = time
        return time

    def DFS(self):
        verticeDicc = {}
        # RECORREOS TODOS LOS VERTICES EN EL CONJUNTO V Y LUEGO INICIALIZAMOS EL OBJETO VERTICE
        for vertice in self.V:
            verticeDicc[vertice] = self.intializeVertice2()
        for v in verticeDicc:
            verticeDicc[v]['color'] = WHITE
            verticeDicc[v]['phi'] = None
        time = 0
        for v in verticeDicc:
            if verticeDicc[v]['color'] == WHITE:
                self.DFS_VISIT(v, time, verticeDicc)
        return verticeDicc

    def printCurrentState(self, result):
        for vertex in result.keys():
            print(vertex, result[vertex])

    def isStartingPoint(self, v, verticeDicc):
        return verticeDicc[v]["phi"] == None

def simulacionRutas():
    # Simulacion de las Rutas posibles
    # Nos encontramos trabajando como ingenieros de una empresa domiciliaria de alimentos
    # Tenemos que proporcionar las ruta que debe tomar el domiciliario para cubrir todos
    # los clientes que solicitarón el servicio (grafo de clientes)
    print("============================== Simulacion Rutas Domicilios =======================")
    #Se definen los pedidos de los clientes y los caminos que se pueden tomar
    print("entran  3 pedidos y los caminos son")
    pedidos1 =  """tienda  cliente1 \ntienda  cliente2 \ntienda  cliente3 \ncliente1 tienda \ncliente1 cliente3 \ncliente3 tienda \ncliente3 cliente2 \ncliente2 tienda"""
    print(pedidos1)
    pedidos1 = pedidos1.split()
    verticesclientes = ["tienda, cliente1, cliente2, cliente3"]
    #Se definen los vertices y los caminos
    # estos se puede ingresar a la main de la siguiente manera
    # 4 9
    # 0 1
    # 0 2
    # 0 3
    # 1 0
    # 1 3
    # 3 2
    # 3 0
    # 3 2
    # 2 0
    vertices = [i for i in range(4)]
    arcos = [[0,1],[0,2],[0,3],[1,0],[1,3],[3,2],[3,0],[3,2],[2,0]]
    #CREAMOS EL GRAFO DE CLIENTES
    grafo_clientes = Graph(vertices, arcos)
    print("-------------matriz de adyacencia------------")
    grafo_clientes.printArcs()
    print("------------------- Ruta de domicilios ---------------------")
    resultado = grafo_clientes.BFS(0)
    for i in range(len(resultado)):
        if i == 0:
            resultado[i]["value"] = "tienda"
        else:
            resultado[i]["value"] = "Cliente"+ str(i)
    grafo_clientes.printBFSResult(resultado)
    print("==============================================================================================")
    print("entran  3 pedidos y los caminos son")
    pedidos1 = """tienda  cliente \ncliente1 cliente2 \ncliente2 cliente1 \ncliente cliente23 \ncliente3 tienda"""
    print(pedidos1)
    pedidos1 = pedidos1.split()
    verticesclientes = ["tienda, cliente1, cliente2, cliente3"]
    # Se definen los vertices y los caminos
    # estos se puede ingresar a la main de la siguiente manera
    # 4 5
    # 0 2
    # 2 1
    # 2 3
    # 1 2
    # 3 0
    vertices = [i for i in range(4)]
    arcos = [[0, 2], [2, 1], [2, 3], [1, 2], [3, 0]]
    # CREAMOS EL GRAFO DE CLIENTES
    grafo_clientes2 = Graph(vertices, arcos)
    print("-------------matriz de adyacencia------------")
    grafo_clientes2.printArcs()
    print("------------------- Ruta de domicilios ---------------------")
    resultado2 = grafo_clientes2.BFS(0)
    for i in range(len(resultado2)):
        if i == 0:
            resultado2[i]["value"] = "tienda"
        if resultado2[i]["phi"] == 0:
            resultado2[i]["phi"] = "tienda"
        if resultado2[i]["phi"] == 1:
            resultado2[i]["phi"] = "Cliente1"
        if resultado2[i]["phi"] == 2:
            resultado2[i]["phi"] = "Cliente2"
        if resultado2[i]["phi"] == 3:
            resultado2[i]["phi"] = "Cliente3"
        if i>0:
            resultado2[i]["value"] = "Cliente" + str(i)
    grafo_clientes.printBFSResult(resultado2)
    trayecto = ruta(resultado2)
    print("el trayecto que tiene que seguir el domiciliario esta dado por los vertices con distancias", trayecto[0],trayecto[1])
    # AHORA SE NOS ENTREGA UN MAPA CON DISTINTOS CLIENTES Y CON ESTE VIENEN UN COJUNTO DE GRAFOS QUE REPRESENTA
    # LA MOVILIDAD DEL DOMICILIARIO NUESTRO TRABAJO ES DETERMINAR CUAL VA A SER VERTICE BASE DONDE DEBEMOS ESTABLECER
    # UNA CENTRAL DE ABASTOS DEL PRODUCTO PARA QUE SU DISTRIBUCION SE OPTIMA
    print("------------------- CENTRAL DE ABASTOS ---------------------")
    currentState = grafo_clientes2.DFS()
    grafo_clientes2.printCurrentState(currentState)
    startingpoints = []
    for v in currentState.keys():
        if grafo_clientes2.isStartingPoint(v, currentState):
            startingpoints.append(v)
    print("las centrales de abastos pueden ser", startingpoints)

def ruta(diccionarioRuta):
    lista = [-1 for i in diccionarioRuta]
    lista[0] = diccionarioRuta[0]["distancia"]
    for vertice in diccionarioRuta:
        if diccionarioRuta[vertice]["distancia"] > lista[vertice-1]:
            lista[vertice] = diccionarioRuta[vertice]["distancia"]
        if diccionarioRuta[vertice]["distancia"] == lista[vertice-1]:
            lista.append(diccionarioRuta[vertice]["distancia"])
            lista[vertice] = lista[vertice-2]


        if diccionarioRuta[vertice]["distancia"] < lista[vertice - 1]:
            lista[vertice-1], lista[vertice] = diccionarioRuta[vertice]["distancia"], diccionarioRuta[vertice-1]["distancia"]
    lista1 = []
    for i in range(len(lista)):
        for j in range(len(diccionarioRuta)):
            if diccionarioRuta[j]["distancia"]==lista[i]:
                lista1.append(diccionarioRuta[j]["value"])
    return lista, lista1

def prototipo():
    print("acceda a las funcionalidades 1 para domiciliario ó 2 para ubicar la central de abastos")
    line = int(stdin.readline().strip())
    while line:
        if line==1:
            print("querido domiciliario diseñemos la ruta para entregar los pedidos")
            print("introdusca sus pedidos y caminos tenieniendo en cuanta que 0 es la tienda de distrubucion ")
            n, m = list(map(int, stdin.readline().strip().split()))
            arcos = []
            vertices = [i for i in range(n)]
            for i in range(m):
                pair = list(map(int, stdin.readline().strip().split()))
                arcos.append(pair)
            grafo_ruta = Graph(vertices, arcos)
            resultado2 = grafo_ruta.BFS(0)
            for i in range(len(resultado2)):
                if i == 0:
                    resultado2[i]["value"] = "tienda"
                if resultado2[i]["phi"] == 0:
                    resultado2[i]["phi"] = "tienda"
                if resultado2[i]["phi"] == 1:
                    resultado2[i]["phi"] = "Cliente1"
                if resultado2[i]["phi"] == 2:
                    resultado2[i]["phi"] = "Cliente2"
                if resultado2[i]["phi"] == 3:
                    resultado2[i]["phi"] = "Cliente3"
                if i>0:
                    resultado2[i]["value"] = "Cliente" + str(i)
            trayecto = ruta(resultado2)
            print("el trayecto que tiene que seguir el domiciliario esta dado por los vertices con distancias", trayecto[0],
                  trayecto[1])
        else:
            print("introdusca los los mapas de vertices de distribucion posibles")
            n, m = list(map(int, stdin.readline().strip().split()))
            arcos = []
            vertices = [i for i in range(n)]
            for i in range(m):
                pair = list(map(int, stdin.readline().strip().split()))
                arcos.append(pair)
            grafo_ruta = Graph(vertices, arcos)
            currentState = grafo_ruta.DFS()
            startingpoints = []
            for v in currentState.keys():
                if grafo_ruta.isStartingPoint(v, currentState):
                    startingpoints.append(v)
            print("las centrales de abastos pueden ser", startingpoints)
        line = int(stdin.readline().strip())

def main():
    n, m = list(map(int, stdin.readline().strip().split()))
    arcos = []
    vertices = [i for i in range(n)]
    for i in range(m):
        pair = list(map(int, stdin.readline().strip().split()))
        arcos.append(pair)
    g1 = Graph(vertices, arcos)
    g1.printArcs()
    g1.printBFSResult(g1.BFS(1))
    currentState = g1.DFS()
    g1.printCurrentState(currentState)
    startingpoints = []
    for v in currentState.keys():
        if g1.isStartingPoint(v, currentState):
            startingpoints.append(v)
    print(startingpoints)


if __name__ == '__main__':
    simulacionRutas()





