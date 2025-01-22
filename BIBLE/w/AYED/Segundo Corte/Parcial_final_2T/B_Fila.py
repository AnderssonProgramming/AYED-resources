from sys import stdin


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def getPrev(self):
        return self.prev

    def setData(self, data):
        self.data = data

    def setNext(self, data_Next):
        self.next = data_Next

    def setPrev(self, data_Prev):
        self.prev = data_Prev

    def reset(self):
        self.setNext(None)
        self.setPrev(None)

    def hasData(self, data):
        return self.data == data




class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None and self.tail is None

    def enqueue(self, data):
        node = Node(data)
        if self.is_empty():
            self.head = node
            self.tail = node

        else:
            self.tail.setNext(node)
            node.setPrev(self.tail)
            self.tail = node
            self.tail.setNext(None)


    def dequeue(self):
        to_return = self.head

        if to_return:
            siguiente = to_return.getNext()
            self.head = siguiente

            if not self.head:
                self.tail = None
            else:
                self.tail.setPrev(None)

        else:
            self.tail = None

        return to_return

    def printQueue(self):
        aux_node = self.head
        temp = []
        while aux_node:
            temp += [aux_node.getData()]
            aux_node = aux_node.getNext()
        print(temp)

def main():
    n = int(stdin.readline().strip())
    for x in range(n):
        fila = Queue()
        m = int(stdin.readline().strip())
        for y in range(m):
            linea = stdin.readline().strip()
            if linea == "Siguiente":
                if fila.is_empty():
                    print("No hay fila")
                else:
                    el = fila.dequeue()
                    print(el.getData())
            else:
                fila.enqueue(linea)
main()