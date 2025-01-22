from sys import stdin


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
            return self.sets[len(self.sets)-1]
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
            print('After processing arc', e, self.sets)
        result = []
        for si in self.sets:
            if len(si) > 1:
                result.append(si)
        return result

def main():

    print("Acontinuacion ingrese los pedidos, si desea añadir dos pedidos para un repartidor escriba ""nombre1, nombre2"", de lo contrario separe cada pedido de cada repartidor por espacios en blanco " )
    print("*para el ejemplo el gerente ingresa: anuel,barbara camilo andres,juan fran,fred esteban *")
    repartidores = list(stdin.readline().strip().split())
    dj = DisjointSets(repartidores)
    print('Sus pedidos son:', dj.getSets())
    action = "4"
    while action != "0":
        print("Si desea añadir un pedido presione 1, si deasea juntar pedidos presiones 2, si deasea ver sus pedidos presione 3, si deasea salir presione 0")
        if action == "4":
            print("*Para el ejemplo el usuario ingresara cada una de las acciones en orden*")
        action = stdin.readline().strip()
        if action == "1":
            print("*Para le ejemplo el usuario ingresa pepe*")
            print("Ingrese el pedido que desea añadir: ")
            nuevo = stdin.readline().strip()
            dj.makeSet(nuevo)
        if action == "2":

            print("*Para le ejemplo el usuario une camilo y esteban*")
            print("Ingrese los pedidos que desea juntar")
            x, y = stdin.readline().strip().split()
            dj.union(x, y)

        if action == "3":
            print("Sus pedidos son: ", dj.getSets())



print("Señor gerente si desea crear un conjunto de pedidos ingrese 0")
resp = stdin.readline().strip()
if resp == "0":
    main()
