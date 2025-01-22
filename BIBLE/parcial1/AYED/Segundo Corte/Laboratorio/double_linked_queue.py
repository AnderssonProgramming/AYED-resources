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
        self.next = data_Prev

    def reset(self):
        self.setNext(None)
        self.setPrev(None)

    def hasData(self, data):
        return self.data == data

class LinkedList:
    def __init__(self):
        self.head = None
        self.len = 0

    def __len__(self):
        return self.len

    def __str__(self):
        if self.len != 0:
            lista = []
            current_node = self.head

            count = 0

            while current_node is not None and count != self.len:
                lista.append(str(current_node))
                current_node = current_node.getNext()
                count += 1

            return str(lista)
        else:
            return '[]'

    def getHead(self):
        return self.head

    def setHed(self, new_head):
        self.head = new_head


    def is_empty(self):
        if len(self) == 0:
            return True
        else:
            return False

    def tail(self):
        node = self.head

        while node.getNext() is not None:
            node = node.getNext()

        return node

    def insert(self, value):
        node = Node(value)
        if self.is_empty():
            self.head = node
        else:
            tail = self.tail()
            tail.setNext(node)
            tail.setPrev(tail.getPrev())
        self.len += 1

    def search(self, data):
        aux_node = self.head
        while aux_node != None and not aux_node.hasData(data):
            aux_node = aux_node.getNext()
        return aux_node

    def update(self, data, new_Data):
        node = self.search(data)
        if node != None :
            node.setData(new_Data)


    def delete(self, value):
        aux_node = self.head
        if self.is_empty():
            return None
        if aux_node.hasData(value):
            self.head = aux_node.getNext()
            return aux_node
        else:
            next = aux_node.getNext()
            while next is not None and not next.hasData(value):
                aux_node, next = next, aux_node.getNext()
            if next:
                aux_node.setNext(next.getNext())
                next.setNext(None)

            return next

    def printList(self):
        listM, aux_node = [], self.head
        while aux_node is not None:
            listM += [aux_node.getData()]
            aux_node = aux_node.getNext()
        print(str(listM))


class Queue:
    def __init__(self):
        self.list = LinkedList()

    def enqueue(self, data):
        node = Node(data)
        if self.list.is_empty():
            self.list.head = node
        else:
            currentTail = self.list.tail()
            currentTail.setNext(node)
        self.list.len += 1

    def dequeue(self):
        if self.list.len == 1:
            self.list.head.reset()
            self.list.len -= 1
        else:
            self.list.delete(self.list.head.getData())

    def printQueue(self):
        aux_node = self.list.head
        temp = []
        while aux_node:
            temp += [aux_node.getData()]
            aux_node = aux_node.getNext()
        print(temp)


def main():
    print("**Se inicia la cola**")
    cola = Queue()
    cola.printQueue()
    print("Juan entra en la cola: ")
    cola.enqueue("Juan")
    cola.printQueue()
    print("Daniela entra en la cola: ")
    cola.enqueue("Daniela")
    cola.printQueue()
    print("Maradona entra en la cola: ")
    cola.enqueue("Maradona")
    cola.printQueue()
    print("El pepe entra en la cola: ")
    cola.enqueue("El pepe")
    cola.printQueue()
    print("Alguien sale de la cola: ")
    cola.dequeue()
    cola.printQueue()
    print("Un desconocido entra en la cola: ")
    cola.enqueue("Un desconocido")
    cola.printQueue()
    print("Se van dos personas de la cola: ")
    cola.dequeue()
    cola.dequeue()
    cola.printQueue()
    print("Al final la cola queda: ")
    cola.printQueue()

main()