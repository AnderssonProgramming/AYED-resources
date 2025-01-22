class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value = value

    def getNext(self):
        return self.next

    def setNext(self, next):
        if next is not None:
            self.next = next
            next.setPrev(self)
        else:
            self.next = next

    def setPrev(self, previous):
        self.prev = previous

    def getPrev(self):
        return self.prev

    def isTail(self):
        return self.next is None

    def __str__(self):
        return 'Node(' + str(self.value) + ')'


class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def getHead(self):
        return self.head

    def setHead(self, head):
        self.head = head
        self.prev = None

    def isEmpty(self):
        return self.head is None

    def getTail(self):
        tail = self.head
        while not tail.isTail():
            tail = tail.getNext()

        return tail

    def delete(self, value):
        node = self.getHead()
        while node.getNext() is not None and node.getValue() != value:
            node = node.getNext()
        if node.getPrev() is None:
            self.setHead(node.getNext())
        elif node.getNext() is None:
            node.getPrev().setNext(None)
        else:
            prev = node.getPrev()
            next = node.getNext()
            prev.setNext(next)
            next.setPrev(prev)

        return self

    def deleteDuplicates(self):
        s = []
        node = self.getHead()
        while node is not None:
            if node.getValue() not in s:
                s.append(node.getValue())
                node = node.getNext()
            else:
                self.delete(node.getValue())
                node = node.getNext()

        return self

    def linkLists(self, lst):
        tail = self.getTail()
        head = lst.getHead()
        tail.setNext(head)
        head.setPrev(tail)

    def _append(self, new_node):
        if self.isEmpty():
            self.head = new_node
        else:
            # Navegar hasta el final
            tail = self.getTail()
            # asignar siguiente del último nodo cómo new_node
            tail.setNext(new_node)

    def append(self, value):
        new_node = Node(value)
        self._append(new_node)

    def __len__(self):
        node, size = self.getHead(), 0
        while node is not None:
            size += 1
            node = node.getNext()
        return size

    def __str__(self):
        prt, node = "", self.getHead()
        while node is not None:
            prt += (str(node) + ' <--> ')
            node = node.getNext()
        prt += 'x'
        return prt

    def reverse(self):
        lst = LinkedList()
        node = self.getTail()
        lst.setHead(node)
        while node.getPrev() is not None:
            lst.append(node.getPrev().getValue())
            node = node.getPrev()
        return lst


class Queue(DoubleLinkedList):
    def dequeue(self):
        head = self.getHead()
        self.delete(self.getHead().getValue())
        self.setHead(head.getNext())

    def enqueue(self, value):
        self.append(value)

    def __str__(self):
        res = ""
        node = self.getHead()
        while node is not None:
            res += str(node.getValue()) + " "
            node = node.getNext()
        return res


class Stack(DoubleLinkedList):

    def pop(self):
        self.delete(self.getTail().getValue())

    def push(self, value):
        new_node = Node(value)
        self._append(new_node)

    def __str__(self):
        res = ""
        node = self.getHead()
        while node is not None:
            res += str(node.getValue()) + " "
            node = node.getNext()
        return res


def mainQueue():
    """
    Vamos a usar como ejemplo una cola de cine en donde habrán 6 personas que van para comprar sus boletos para
    ver James Bond No Time to Die, en los primeros 10 min 3 personas van a poder comprar boletos y llegan otras dos personas.
    """
    cola = Queue()
    cola.enqueue("Julián")
    cola.enqueue("Valentina")
    cola.enqueue("Felipe")
    print(cola)
    cola.dequeue()
    cola.dequeue()
    print(cola)
    cola.enqueue("Miguel Ángel")
    cola.enqueue("Juan Camilo")
    print(cola)


# mainQueue()

def mainStack():
    """
    Vamos a usar como ejemplo una pila de 8 libros, todos son los mismos (Introduction to algorithms, The MIT Press)
    tres estudiantes toman libros, 5 estudiantes regresan los libros que ya usaron y luego uno más toma otro libro
    """
    pila = Stack()
    pila.push("Unidad 1")
    pila.push("Unidad 2")
    pila.push("Unidad 3")
    pila.push("Unidad 4")
    pila.push("Unidad 5")
    pila.push("Unidad 6")
    pila.push("Unidad 7")
    pila.push("Unidad 8")
    print(pila)
    pila.pop()
    pila.pop()
    pila.pop()
    print(pila)
    pila.push("Unidad 7")
    print(pila)

print("Pila")
mainStack()
print("--------------------------------")
print("Cola")
mainQueue()
