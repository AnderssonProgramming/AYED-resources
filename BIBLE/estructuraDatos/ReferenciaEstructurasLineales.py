import queue
import collections


# Author: Sebastian Martinez Reyes
# El siguiente es un ejemplo de las funciones, usos y definiciones disponibles para Colas(LIFO y FIFO), Listas circulares y listas Encadenadas
# El proposito de este material es de consulta, a continuación las definiciones disponibles:
# Colas sincronizadas (FIFO y LIFO): https://docs.python.org/3/library/queue.html?highlight=queue#module-queue
# Listas circulares: https://docs.python.org/3/library/collections.html?highlight=deque#collections.deque

# Linked List Node definition
class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext


# Linked List definition
class LinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        node = Node(item)
        node.setNext(self.head)
        self.head = node

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()
        return count

    def printList(self):
        current = self.head
        while current != None:
            if current.getData() is not None:
                print(current.getData())

            current = current.getNext()

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def head(self):
        return self.head

    def remove(self, item):
        try:
            current = self.head
            previous = None
            found = False
            while current != None and not found:
                if current.getData() == item:
                    found = True
                else:
                    previous = current
                    current = current.getNext()

            if previous == None:
                self.head = current.getNext()
            else:
                previous.setNext(current.getNext())
        except:
            return -1


# El siguiente es un ejemplo de las funciones, usos y definiciones disponibles para Colas(LIFO y FIFO), Listas circulares
# El proposito de este material es de consulta, a continuación las definiciones disponibles:
# Colas sincronizadas (FIFO y LIFO): https://docs.python.org/3/library/queue.html?highlight=queue#module-queue
# Listas circulares: https://docs.python.org/3/library/collections.html?highlight=deque#collections.deque

# FIFO(First in First out) Queue
def queueSample(orden):
    print('========================================= EJEMPLO DE COLAS FIFO ========================================= ')
    fifoQueue = queue.Queue()
    for i in orden:
        fifoQueue.put(i)
    print('\nEl tamaño de la Cola FIFO es: ', fifoQueue.qsize())
    print('\nEl contenido de la cola FIFO es: ')
    while not fifoQueue.empty():
        print(fifoQueue.get())
    print(
        '========================================= FIN EJEMPLO DE COLAS FIFO ========================================= ')


# LIFO(Last in Last out) Queue
def LIFOQueueSample(orden):
    print('=========================================  EJEMPLO DE COLAS LIFO ========================================= ')
    lifoQueue = queue.LifoQueue()
    for i in orden:
        lifoQueue.put(i)
    print('\nEl tamaño de la Cola LIFO es: ', lifoQueue.qsize())
    print('\nEl contenido de la cola LIFO es: ')
    while not lifoQueue.empty():
        print(lifoQueue.get())
    print(
        '=========================================  FIN EJEMPLO DE COLAS LIFO ========================================= ')


def dequeSample(orden):
    print(
        '=========================================  EJEMPLO DE LISTAS CIRCULARES =========================================')
    deque = collections.deque()
    for i in orden:
        deque.append(i)  # añadir elementos a la derecha

    print('\nEl tamaño de la lista circular es: ', len(deque))
    print('\nEl contenido de la lista circular es: ')
    print(deque)
    # rotar la lista 2 posiciones a la derecha
    deque.rotate(2)
    print(deque)
    # rotar la lista 5 posiciones a la izquierda (Desde la ultima instruccion)
    deque.rotate(-5)
    print(deque)

    deque.appendleft('kalash kalash')  # añadir elementos a la izquierda
    print(deque)

    # Extender la lista
    deque.extend(['ex1', 'ex2', 'ex3'])
    print(deque)

    # Reversar la lista
    reverdesDeque = collections.deque(reversed(deque))
    print(reverdesDeque)

    print('\nLos elementos de la lista son:')
    for elem in deque:  # recorrer los elementos de la lista
        print(elem)

    print('\nElementos indexados :')
    # Elementos indexados por derecha
    print(deque[3])

    # Elementos indexados por izquierda
    print(deque[-6])

    print('\nLos elementos de la lista son:')
    # Otra manera de recorrer eliminando
    while True:
        try:
            print(deque.pop())
        except IndexError:
            break

    print('\nLos elementos de la lista son:')
    # Otra manera de recorrer eliminando por izquierda
    while True:
        try:
            print(reverdesDeque.pop())
        except IndexError:
            break
    print(
        '=========================================  FIN EJEMPLO DE LISTAS CIRCULARES ========================================= ')


def linkedListSample(orden):
    print(
        '=========================================  EJEMPLO DE LISTAS ENLAZADAS ========================================= ')

    list = LinkedList()
    print('La lista es Vacia ? :', list.isEmpty())
    for i in orden:
        list.add(i)
    print('\nEl tamaño de la lista enlazada es: ', list.size())
    print('La lista es Vacia ? :', list.isEmpty())
    print('Buscando un elemento en la Lista :', list.search('Spaguetti'))
    print('Buscando un elemento en la Lista que no existe :', list.search('Spaguetti232323'))
    print('\nLos elementos de la lista son:')
    list.printList()
    print('\nEliminación correcta:')
    print(list.remove('Pizza'))  # Eliminando elementos de la lista
    print('\nEliminación errada:')
    print(list.remove('pizza'))  # Eliminando elementos de la lista que no esta
    print('\nLos elementos de la lista son:')
    list.printList()
    print(
        '========================================= FIN EJEMPLO DE LISTAS ENLAZADAS ========================================= ')


def main():
    pedido = []

    pedido.append('Pizza')
    pedido.append('Spaguetti')
    pedido.append('Carne en salsa')
    pedido.append('Hamburguesa')
    pedido.append('Pollo a la Naranja')
    pedido.append('Huevos fritos con tocineta.')
    pedido.append('Shawarma')
    pedido.append('Carpaccio de lomito')
    pedido.append('Sopa de pollo')
    pedido.append('Causa limeña.')
    pedido.append('Lomo saltado')

    queueSample(pedido[:])
    LIFOQueueSample(pedido[:])
    dequeSample(pedido[:])
    linkedListSample(pedido[:])


main()
