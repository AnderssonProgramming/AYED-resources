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



class Stack:
    def __init__(self):
        self.stack = LinkedList()

    def push(self, x):
        node = Node(x)
        if self.stack.is_empty():
            self.stack.head = node
        else:
            new_top = node
            node.setNext(self.stack.head)
            self.stack.head, new_top = new_top, self.stack.head
        self.stack.len += 1

    def pop(self):
        if not self.stack.is_empty():
            aux = self.stack.head.getNext()
            self.stack.head.reset()
            self.stack.head = aux
        self.stack.len -= 1

    def search(self, data):
        aux_node = self.stack.head
        while aux_node != None and not aux_node.hasData(data):
            aux_node = aux_node.getNext()
        return aux_node

    def printStack(self):
        aux_node = self.stack.head
        while aux_node:
            print(aux_node.getData())
            aux_node = aux_node.getNext()

def judge(lista):
    simbolos = {')': '(', ']': '[', '}': '{'}
    errores = Stack()
    for index in lista:
        if index in simbolos.keys():
            if (errores.stack.head is None) or errores.stack.head.getData() != simbolos[index]:
                return False
            elif not errores.stack.is_empty():
                errores.pop()
        else:
            errores.push(index)
    return errores.stack.is_empty()


def main():
    n = int(stdin.readline().strip())
    while n > 0:
        lista = list(stdin.readline().strip())
        if judge(lista):
            print("Yes")
        else:
            print("No")
        n -= 1


main()
