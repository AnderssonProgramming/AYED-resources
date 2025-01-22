from sys import stdin
from random import randint

class HashTable:
    def __init__(self, size):
        self.elements = [[] for x in range(size)]


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
        print('Inserting', value, 'with key', key, 'on index', index)
        self.assign(index, (key,value))

    def search(self, key):
        index = self.hash(key)
        for e in self.elements[index]:
            if e[0] == key:
                return e[1]
        return None

    def update(self, key, value2):
        index = self.hash(key)
        for e in self.elements[index]:
            if e[0] == key:
                e[1] = value2

    def delete(self, key):
        index = self.hash(key)
        element = self.search(key)
        if element:
            self.elements[index].remove(element)

def main():
    print("Ingrese cuantos pedidos va a agenedar: ")
    print("Para el ejemplo es usuario va a ingresar 6")
    size = int(stdin.readline().strip())
    hashtable = HashTable(size)

    cont = size
    print("Acontinuacion ingrese los pedidos un por uno de la forma ""Nombre fecha"": ")
    lista = []
    while cont > 0:
        el1, el2 = stdin.readline().strip().split()
        lista += [(el1, el2)]
        cont -= 1
    print(lista)

    for elem in lista:
        hashtable.insert(elem[0], elem[1])

    action = "4"

    while action != "0":
        print("Si desea buscar la hora de algun pedido ingrese 1, si desea ver todos sus pedidos ingrese 2, si deasea salir ingrese 0")
        if action == "4":
            print("*Para el ejemplo el usuario va a ingresar todas las opciones en orden*")
        action = stdin.readline().strip()
        if action == "1":
            print("Ingrese el nombre de la entrega que desa saber la hora: ")
            print("*Para el ejemplo va a buscar Juan*")
            key = stdin.readline().strip()
            print(hashtable.search(key))
        if action == "2":
            hashtable.printElements()


print("Señor gerente si desea aguendar sus pedidos ingrese 0")
resp = stdin.readline().strip()
if resp == "0":
    main()
