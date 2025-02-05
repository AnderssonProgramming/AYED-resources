from random import randint
from time import time
from uuid import uuid1

SIZE = int(2e6)

class Node:
    def __init__(self, value = None):
        self.value = None
        self.next = None
        self.prev = None  # Nuevo atributo para el nodo anterior
        self.setValue(value)

    def setValue(self, value):
        self.value = value

    def getValue(self):
        return self.value

    def getNext(self):
        return self.next

    def getPrev(self):  # Nuevo método para obtener el nodo anterior
        return self.prev

    def setNext(self, next):
        if not( isinstance(next, Node) or next is None):
            raise Exception("El tipo del atributo next no es del tipo de dato esperado.")
        self.next = next

    def setPrev(self, prev):  # Nuevo método para establecer el nodo anterior
        if not( isinstance(prev, Node) or prev is None):
            raise Exception("El tipo del atributo prev no es del tipo de dato esperado.")
        self.prev = prev

    def __str__(self):
        return "Node({}) <--> {}".format(self.value, self.next if self.next else "X")

class LinkedList:
    def __init__(self, elements = []):
        self.head = None
        self.tail = None
        self.len = 0
        for e in elements:
            self.append(e)

    def __len__(self):
        return self.len

    def setHead(self, node):
        if not isinstance(node, Node):
            raise Exception("El tipo del atributo head no es del tipo de dato esperado.")
        self.head = node

    def setTail(self, node):
        if not isinstance(node, Node):
            raise Exception("El tipo del atributo tail no es del tipo de dato esperado.")
        self.tail = node
        if self.tail is not None:
            self.tail.setNext(None)

    def append(self, value):
        new_node = Node(value)
        if self.isEmpty():
            self.setHead(new_node)
            self.setTail(new_node)
        else:
            tail = self.tail
            tail.setNext(new_node)
            new_node.setPrev(tail)  # Establece el nodo anterior del nuevo nodo
            self.setTail(new_node)
        self.len += 1

    def find(self, value):
        node_result = self.head
        while node_result is not None and node_result.getValue() != value:
            node_result = node_result.getNext()
        return node_result

    def update(self, old_value, new_value):
        node_to_update = self.find(old_value)
        if node_to_update is not None:
            node_to_update.setValue(new_value)

    def isEmpty(self):
        return self.head is None

    def __str__(self):
        return str(self.head)

    def join(self, ll2):
        if not isinstance(ll2, LinkedList):
            raise Exception("El tipo del parametro ll2 no es del tipo de dato esperado.")
        if self.isEmpty():
            return ll2
        if not ll2.isEmpty():
            self.tail.setNext(ll2.head)
            ll2.head.setPrev(self.tail)  # Establece el nodo anterior del primer nodo de ll2
            self.tail = ll2.tail
            self.len = self.len + len(ll2)
        return self

def main():
    ll = LinkedList([1,2,3])
    print(ll, len(ll))
    ll.append(500)
    print(ll, len(ll))
    ll2 = LinkedList([3, 4, 5])
    result = ll.join(ll2)
    print(result, len(result))
    arr1 = [ uuid1() for i in range(SIZE)]
    arr2 = [ uuid1() for i in range(SIZE)]
    ll1 = LinkedList(arr1)
    ll2 = LinkedList(arr2)
    t0 = time()
    arr3 = arr1 + arr2
    t1 = time()
    print("Classic Join {}".format(t1-t0))
    t0 = time()
    ll3 = ll1.join(ll2)
    t1 = time()
    print("New Join {}".format(t1-t0))

main()
