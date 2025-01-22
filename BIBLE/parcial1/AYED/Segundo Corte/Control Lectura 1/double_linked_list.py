class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None
        self.prev = None

    def __str__(self):
        if self.data is not None:
            return "N({})".format(str(self.data))
        return ''

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def getPrev(self):
        return self.prev

    def setData(self, new_data):
        self.data = new_data

    def setNext(self, new_next):
        self.next = new_next

    def setPrev(self, new_prev):
        self.prev = new_prev

    def reset(self):
        self.setData(None)
        self.setNext(None)
        self.setPrev(None)


class double_linked_list:
    def __init__(self, data = []):
        self.head = None
        self.len = 0
        if data:
            for el in data:
                self.insert(el)


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

    def __len__(self):
        return  self.len

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

    # Insertar nuevo elemento

    def insert(self, data):
        newNode = Node(data)

        if self.is_empty():
            self.head = newNode

        else:
            node = self.tail()
            aux_node = node
            node.setNext(newNode)

            inserted = self.tail()
            inserted.setPrev(aux_node)

        self.len += 1

    def node_search(self, data):
        if self.is_empty():
            return None
        node = self.head
        while node is not None and node.getData() != data:
            node = node.getNext()

        return node

    def data_serch(self, data):
        node = self.node_search(data)
        print("Next node:", node.getNext())
        print("Prev node:", node.getPrev())

        return node.getData() if node else None

    def node_update(self, data, Next):
        node = self.node_search(data)
        if node:
            node.setNext(Next)

    def data_update(self, old_data, new_data):
        node =  self.node_search(old_data)
        if node:
            node.setData(new_data)

    # Eliminar un elemento dado su valor

    def remove(self, data):
        node = self.node_search(data)

        if node == self.head:
            self.head = node.getNext()
            self.len -= 1

        else:
            aux_node = self.head

            while aux_node is not None and aux_node.getNext() is not None and aux_node.getData() != data:
                aux_node = aux_node.getNext()

            if aux_node and node:
                aux_node.reset()
                next_deleted = node.getNext()
                node.reset()
                aux_node.setNext(next_deleted)
            self.len -= 1

        return node

    # Invertir

    def invertir(self):
        aux_node = self.head
        data = []
        while aux_node:
            data.append(aux_node.getValue())
            aux_node = aux_node.getNext()
        data.reverse()
        resp = double_linked_list()
        for dat in data:
            resp.insert(dat)
        return resp

    # Union dos listas

    def union(self, list2):
        node = list2.head
        while node:
            self.insert(node.getValue())
            node = node.getNext()

    # Eliminar duplicados

    def remove_duplicates(self):
        node = self.getHead()
        memo = {}
        memo[node.getData()] = 1
        while node.getNext() is not None:
            node = node.getNext()
            if node.getData() in memo.keys():
                self.remove(node.getData())
            else:
                memo[node.getData()] = 1

def main():
    lista = double_linked_list([1, 2, 3])
    lista_2 = double_linked_list([4, 5, 6])

    lista.insert(33)
    lista.data_update(33, 35)

    print(lista.data_serch(2))

    print(lista)
    print(len(lista))

    print(lista)

    print(lista.data_serch(35))

    lista.remove(1)
    print(lista)

    lista = double_linked_list([1,1,2,2,3,3,4,4,2,2,1,1,1,1])

    print(lista)
    lista.remove_duplicates()
    print(lista)
    print(lista.data_serch(1))

main()