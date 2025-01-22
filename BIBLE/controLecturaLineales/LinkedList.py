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

    def setNext(self, nextV):
        if nextV is not None:
            self.next = nextV
            nextV.setPrev(self)
        else:
            self.next = next

    def setPrev(self, prev):
        self.prev = prev

    def getPrev(self):
        return self.prev

    def isTail(self):
        return self.next is None

    def __str__(self):
        return 'Node(' + str(self.value) + ')'


class LinkedList:
    def __init__(self):
        self.head = None

    def getHead(self):
        return self.head

    def setHead(self, head):
        self.head = head

    def isEmpty(self):
        return self.head is None

    def getTail(self):
        tail = self.head
        while not tail.isTail():
            tail = tail.getNext()

        return tail

    def delete(self, value):
        node = self.getHead()
        while node is not None and node.getValue() != value:
            node = node.getNext()
        if node.getPrev() is None:
            self.setHead(node.getNext())
            node.getNext().setPrev(None)
        elif node.getNext() is None:
            node.getPrev().setNext(None)
        else:
            prev1 = node.getPrev()
            next1 = node.getNext()
            prev1.setNext(next1)
            next1.setPrev(prev1)
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
            tail = self.getTail()
            tail.setNext(new_node)

    def append(self, value):
        new_node = Node(value)
        self._append(new_node)

    def __str__(self):
        prt, node = "", self.getHead()
        while node is not None:
            prt += (str(node) + ' --> ')
            node = node.getNext()
        prt += 'x'
        return prt

    def reverse(self):
        lista = LinkedList()
        node = self.getTail()
        lista.setHead(node)
        while node.getPrev() is not None:
            lista.append(node.getPrev().getValue())
            node = node.getPrev()
        return lista
