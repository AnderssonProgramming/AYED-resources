class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def delete(self, value):
        current = self.head
        while current is not None:
            if current.value == value:
                if current.prev is not None:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next is not None:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                return
            current = current.next

class Stack:
    def __init__(self):
        self.list = DoublyLinkedList()

    def push(self, value):
        self.list.append(value)

    def pop(self):
        value = self.list.tail.value
        self.list.delete(value)
        return value

class Queue:
    def __init__(self):
        self.list = DoublyLinkedList()

    def enqueue(self, value):
        self.list.append(value)

    def dequeue(self):
        value = self.list.head.value
        self.list.delete(value)
        return value

def main():
    # Simulando la cola de un banco
    print("Simulando la cola de un banco:")
    bank_queue = Queue()
    bank_queue.enqueue("Cliente 1")
    bank_queue.enqueue("Cliente 2")
    bank_queue.enqueue("Cliente 3")
    print(bank_queue.dequeue())  # Debería imprimir: Cliente 1
    print(bank_queue.dequeue())  # Debería imprimir: Cliente 2

    # Simulando el apilamiento de libros
    print("\nSimulando el apilamiento de libros:")
    book_stack = Stack()
    book_stack.push("Libro 1")
    book_stack.push("Libro 2")
    book_stack.push("Libro 3")
    print(book_stack.pop())  # Debería imprimir: Libro 3
    print(book_stack.pop())  # Debería imprimir: Libro 2

main()
