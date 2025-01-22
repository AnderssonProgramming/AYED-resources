from Grafos import *
from Montones_Colas import *


def prototipo():
    print("Acceda a las funcionalidades:")
    print("Presione 1 para domiciliario ")
    print("Presione 2 para administrador")
    print("Presione 0 para acabar")
    line = int(stdin.readline().strip())
    while line:
        if line == 1:
            domiciliario()
            print("listo")
        else:
            administrador()
        line = int(stdin.readline().strip())


def domiciliario():
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
        if i > 0:
            resultado2[i]["value"] = "Cliente" + str(i)
    trayecto = ruta(resultado2)
    print("el trayecto que tiene que seguir el domiciliario esta dado por los vertices con distancias", trayecto[0],
          trayecto[1])


def administrador():
    print("Buenos dias administrador acceda a alguna de las siguientes subfunciónes:")
    print("Presione 1 para ubicar la central de abastos ")
    print("Presione 2 para ver la productividad de los Domiciliarios")
    line = int(stdin.readline().strip())
    if line == 1:
        print("introdusca los mapas de vertices de distribucion posibles")
        n, m = list(map(int, stdin.readline().strip().split()))
        arcos = []
        vertices = [i for i in range(n)]
        for i in range(m):
            pair = list(map(int, stdin.readline().strip().split()))
            arcos.append(pair)
        grafo_ruta = Graph(vertices, arcos)
        current_state = grafo_ruta.DFS()
        startingpoints = []
        for v in current_state.keys():
            if grafo_ruta.isStartingPoint(v, current_state):
                startingpoints.append(v)
        print("las centrales de abastos pueden ser", startingpoints)
    else:
        data = [
            ('2020-11-06', 'Melissa', 90),
            ('2020-11-06', 'Juan', 87),
            ('2020-11-06', 'Ernesto', 10),
            ('2020-11-06', 'Andres', 24),
            ('2020-11-06', 'Javier', 120),
            ('2020-11-06', 'Vanessa', 65)
        ]
        print("Domiciliarios:", data)
        print("Si desea insertar Domicilirios presione 1")
        print("Si desea visualizar la cola prioridad presione 2")
        line = int(stdin.readline().strip())
        if line == 1:
            print("Ingrese los datos con el sigiente formato")
            print('AAAA-MM-DD', 'Nombre', 'Puntuación')
            line = stdin.readline().strip().split()
            while line:
                trabajador = list(map(str, line))
                trabajador[2] = int(trabajador[2])
                trabajador = (trabajador[0], trabajador[1], trabajador[2])
                data.append(trabajador)
                line = stdin.readline().strip().split()
            print(data)
            print("Ingrese la forma de la cola de prioridad")
            print("Max, si quiere ver los trabajadores con mejor desempeño")
            print("Min, si quiere ver los trabajadores con peor desempeño")
            line = stdin.readline().strip()
            if line == "Min":
                pq = PriorityQueue(data, 2, "Min")
                while len(pq) > 0:
                    print('Next element ...', pq.pop())
            else:
                pq = PriorityQueue(data, 2, "Max")
                while len(pq) > 0:
                    print('Next element ...', pq.pop())
        else:
            print("Ingrese la forma de la cola de prioridad")
            print("Max, si quiere ver los trabajadores con mejor desempeño")
            print("Min, si quiere ver los trabajadores con peor desempeño")
            line = stdin.readline().strip()
            if line == "Min":
                pq = PriorityQueue(data, 2, "Min")
                while len(pq) > 0:
                    print('Next element ...', pq.pop())
            else:
                pq = PriorityQueue(data, 2, "Max")
                while len(pq) > 0:
                    print('Next element ...', pq.pop())

        return None


if __name__ == '__main__':
    prototipo()