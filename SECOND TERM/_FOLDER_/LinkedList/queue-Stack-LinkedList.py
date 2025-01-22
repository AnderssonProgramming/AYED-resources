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

    def pop(self):
        if self.head is None:
            return None
        value = self.tail.value
        self.tail = self.tail.prev
        if self.tail is None:
            self.head = None
        else:
            self.tail.next = None
        return value

    def peek(self):
        return self.tail.value if self.tail else None

    def popleft(self):
        if self.head is None:
            return None
        value = self.head.value
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        else:
            self.head.prev = None
        return value

class Stack:
    def __init__(self):
        self.list = DoublyLinkedList()

    def push(self, value):
        self.list.append(value)

    def pop(self):
        return self.list.pop()

    def peek(self):
        return self.list.peek()

class Queue:
    def __init__(self):
        self.list = DoublyLinkedList()

    def enqueue(self, value):
        self.list.append(value)

    def dequeue(self):
        return self.list.popleft()

    def peek(self):
        return self.list.head.value if self.list.head else None
def main():
    # Prueba de la pila
    print("Stack´s test:")
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack.pop())
    print(stack.peek())

    # Prueba de la cola
    print("\nQueue´s test:")
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(queue.dequeue())  
    print(queue.peek())

main()
