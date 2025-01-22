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


class LinkedList:
    #Create
    def __init__(self):
       self.head = None
       self.len = 0

    #Is Empty
    def isEmpty(self):
        return self.head == None

    def goToTail(self):
        currentNode = self.head
        while currentNode.getNext() != None:
            currentNode = currentNode.getNext()
        return currentNode

    def search(self, value):
        currentNode= self.head
        while currentNode != None and not currentNode.hasVal(value):
            currentNode = currentNode.getNext()
        return currentNode

    def update(self, value, newValue):
        nodeToSearch = self.search(value)
        if nodeToSearch != None :
            nodeToSearch.setValue(newValue)

    def __len__(self):
        return self.len

    def __str__(self):
        listMembers, currentNode = [], self.head
        while currentNode is not None:
            listMembers += [currentNode.getValue()]
            currentNode = currentNode.getNext()
        return str(listMembers)

    def printList(self):
        listMembers, currentNode = [], self.head
        while currentNode is not None:
            listMembers+=[currentNode.getValue()]
            currentNode = currentNode.getNext()
        print(str(listMembers))

    def delete(self, value):
        currentNode = self.head
        #Caso Vacío
        if self.isEmpty():
            return None
        #Caso primer valor solicitado
        if currentNode.hasVal(value):
            self.head = currentNode.getNext()
            return currentNode
        else:
            next = currentNode.getNext()
            while next is not None and not next.hasVal(value):
                currentNode, next = next, currentNode.getNext()
            if next:
                currentNode.setNext(next.getNext())
                next.setNext(None)
            return next


class Stack:
    def __init__(self):
        self.stack = LinkedList()

    def push(self, x):
        """
        Función que inserta un elemento al inicio de la pila
        :Cualquier Tipo x:
        :return type(x):
        """
        node = Node(x)
        if self.stack.isEmpty():
            self.stack.head = node
        else:
            newTop = self.stack.head.getPrev()
            newTop = node
            node.setNext(self.stack.head)
            self.stack.head, newTop = newTop, self.stack.head

    def pop(self):
        """
        Función que elimina un elemento de pila siguiendo la política LIFO
        """
        if not self.stack.isEmpty():
            aux = self.stack.head.getNext()
            self.stack.head.clear()
            self.stack.head = aux

    def search(self,value):
        """
        Función que busca si un elemento en la pila
        :Cualquier Tipo value:
        :return type(value):
        """
        currentNode = self.stack.head
        while currentNode != None and not currentNode.hasVal(value):
            currentNode = currentNode.getNext()
        return currentNode

    def printStack(self):
        """
        Función que imprime la pila en una linea separando los elementos por un espacio
        """
        currentNode = self.stack.head
        while currentNode:
            print(currentNode.getValue(), end=' ')
            currentNode = currentNode.getNext()
        print()
