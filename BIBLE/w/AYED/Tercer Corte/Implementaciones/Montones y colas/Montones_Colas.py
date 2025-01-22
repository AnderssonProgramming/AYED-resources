import math

# Politica de cola - MAX/MIN

class PriorityQueue:
    def __init__(self, A, property_check=0, typeHeap= "Max"):
        self.heap = Heap(A, property_check, typeHeap)
        self.typeHeap = typeHeap

    def push(self, element):
        if self.typeHeap == "Max":
            self.heap.insertMax(element)
        else:
            self.heap.insertMin(element)

    def pop(self):
        element = self.heap.getRoot()
        if self.typeHeap == "Max":
            self.heap.deleteMax(element)
        else:
            self.heap.deleteMin(element)
        return element

    def __len__(self):
        return len(self.heap)


class Heap:
    def __init__(self, A, property_check = 0, typeHeap = "Max"):
        self.property_check = property_check
        self.elements = []
        self.typeHeap = typeHeap
        if typeHeap == "Max":
            for e in A:
                self.insertMax(e)
        else:
            for e in A:
                self.insertMin(e)

    def getElements(self):
        return self.elements

    def left(self, i):
        return 2*i + 1

    def right(self, i):
        return 2*(i + 1)

    def height(self):
        return math.floor(math.log(len(self.elements), 2)) + 1

    def parent(self, i):
        return (i-1)//2 if i % 2 != 0 else (i//2 - 1)

    def buildMaxHeapify(self):
        for i in range(len(self.elements)//2, -1, -1):
            self.maxHeapify(i)

    def buildMinHeapify(self):
        for i in range(len(self.elements)//2, -1, -1):
            self.minHeapify(i)

    def getRoot(self):
        return self.elements[0]

    def insertMax(self, e):
        self.elements.append(e)
        self.buildMaxHeapify()

    def insertMin(self, e):
        self.elements.append(e)
        self.buildMinHeapify()

    def deleteMax(self, key):
        self.elements.remove(key)
        self.buildMaxHeapify()

    def deleteMin(self, key):
        self.elements.remove(key)
        self.buildMinHeapify()

    def updateMax(self, old_key, new_key):
        self.deleteMax(old_key)
        self.insertMax(new_key)

    def updateMin(self, old_key, new_key):
        self.deleteMin(old_key)
        self.insertMin(new_key)

    # Funcion que matiene la politca de la raiz mayor que sus hijos
    def maxHeapify(self, root):
        left, right, largest = self.left(root), self.right(root), root
        if left < len(self.elements) and self.elements[root][self.property_check] < self.elements[left][self.property_check]:
            largest = left
        if right < len(self.elements) and self.elements[largest][self.property_check] < self.elements[right][self.property_check]:
            largest = right
        if largest != root:
            self.elements[largest], self.elements[root] = self.elements[root], self.elements[largest]
            self.maxHeapify(largest)

    # Funcion que matiene la politca de la raiz mayor que sus hijos
    def minHeapify(self, root):
        left, right, largest = self.left(root), self.right(root), root
        if left < len(self.elements) and self.elements[root][self.property_check] > self.elements[left][self.property_check]:
            largest = left
        if right < len(self.elements) and self.elements[largest][self.property_check] > self.elements[right][self.property_check]:
            largest = right
        if largest != root:
            self.elements[largest], self.elements[root] = self.elements[root], self.elements[largest]
            self.minHeapify(largest)

    def __len__(self):
        return len(self.elements)


def main():
    #minHeap = Heap([2, 3, 4, 6, 7, 9, 11])
    #print("Before Heap", minHeap.getElements())
    #minHeap.maxHeapify(1)
    #print("After Heap", minHeap.getElements())
    data = [
        ('2020-11-06', 'Melissa', 90),
        ('2020-11-06', 'Juan', 87),
        ('2020-11-06', 'Ernesto', 10),
        ('2020-11-06', 'Andres', 24),
        ('2020-11-06', 'Javier', 120),
        ('2020-11-06', 'Vanessa', 65)
    ]

    pq = PriorityQueue(data, 2, "Min")

    while len(pq) > 0:
        print('Next element ...', pq.pop())


#main()
