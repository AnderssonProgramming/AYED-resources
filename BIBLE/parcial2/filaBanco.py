from sys import stdin


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def setNext(self, next):
        self.next = next

    def setPrev(self, prev):
        self.prev = prev

    def setValue(self, value):
        self.value = value

    def getNext(self):
        return self.next

    def getPrev(self):
        return self.prev

    def getValue(self):
        return self.value

    def clear(self):
        self.setNext(None)
        self.setPrev(None)

    def hasVal(self, val):
        return self.value == val



class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, value):
        """
        Función que agrega un elemento a la cola al final de esta
        :Cualquier Tipo value:
        :return type(value):
        """
        node = Node(value)
        if self.isEmpty():
            self.head = node
            self.tail = node

        else:
            self.tail.setNext(node)
            node.setPrev(self.tail)
            self.tail = node
            self.tail.setNext(None)

    def dequeue(self):
        """
        Función que elimina un elemento de la cola manteniendo la política FIFO
        """
        returnValue = self.head

        if returnValue:
            siguiente = returnValue.getNext()
            self.head = siguiente

            if not self.head:
                self.tail = None
            else:
                self.tail.setPrev(None)

        else:
            self.tail = None

        return returnValue

    def isEmpty(self):
        return self.head is None and self.tail is None


def main():
    n = stdin.readline().strip()
    for x in range(int(n)):
        fila = Queue()
        m = stdin.readline().strip()
        for y in range(int(m)):
            linea = stdin.readline().strip()
            if linea == "Siguiente":
                if fila.isEmpty():
                    print("No hay fila")
                else:
                    remove = fila.dequeue()
                    print(remove.getValue())
            else:
                fila.enqueue(linea)


main()
