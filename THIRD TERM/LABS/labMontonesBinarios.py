import math
import uuid
from random import randint


class Heap:
    def __init__(self, data=[], config=True):
        self.data = []
        self.config = config
        self.build (data[:])

    def left(self, index):
        return 2 * index + 1

    def right(self, index):
        return 2 * (index + 1)

    def parent(self, index):
        return (index - 1) // 2

    def height(self):
        return math.ceil (math.log (len (self.data), 2))

    def __len__(self):
        return len (self.data)

    def insert(self, new):
        self.data.append (new)
        self.build ()

    def update(self, old, new):
        self.delete (old)
        self.insert (new)

    def delete(self, to_delete):
        if len (self) == 0:
            raise Exception ("El montón está vacío")
        if to_delete not in self.data:
            raise Exception ("El elemento no está en el montón")
        self.data.remove (to_delete)
        self.build ()

    def build(self, data=[]):
        if data and len (data) > 0 and isinstance (data, list):
            self.data = data
        for index in range (len (self) // 2, -1, -1):
            self.heapify (index)

    def heapify(self, index):
        if self.config:
            self.max_heapify (index)
        else:
            self.min_heapify (index)

    def max_heapify(self, index):
        left_index, right_index, largest_index = self.left (index), self.right (index), index
        if left_index < len (self) and self.data[largest_index] < self.data[left_index]:
            largest_index = left_index
        if right_index < len (self) and self.data[largest_index] < self.data[right_index]:
            largest_index = right_index
        if largest_index != index:
            self.data[largest_index], self.data[index] = self.data[index], self.data[largest_index]
            self.max_heapify (largest_index)

    def min_heapify(self, index):
        left_index, right_index, smallest_index = self.left (index), self.right (index), index
        if left_index < len (self) and self.data[smallest_index] > self.data[left_index]:
            smallest_index = left_index
        if right_index < len (self) and self.data[smallest_index] > self.data[right_index]:
            smallest_index = right_index
        if smallest_index != index:
            self.data[smallest_index], self.data[index] = self.data[index], self.data[smallest_index]
            self.min_heapify (smallest_index)

    def peek(self):
        return self.data[0]


class PriorityQueue:
    def __init__(self, data=[], config=True):
        self.data = Heap (data, config)

    def __len__(self):
        return len (self.data)

    def enqueue(self, new):
        self.data.insert (new)

    def dequeue(self):
        if len (self) == 0:
            raise Exception ("Underflow")
        to_dequeue = self.data.peek ()
        self.data.delete (to_dequeue)
        return to_dequeue


class Persona:
    def __init__(self, nombre="", edad=1,deporte = None):
        self.nombre = nombre
        self.edad = edad
        self.deporte = deporte
    def __lt__(self, other):
        return self.edad < other.edad

    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad},Deporte: {self.deporte}"


def heapSort(lst, config=True):
    result = []
    heap = Heap(lst, config)
    while len(heap) > 0:
        result.append(heap.data[0])  # Añadir la raíz actual al resultado
        last_element = heap.data.pop()  # Extraer el último elemento del montón
        if len(heap) > 0:
            heap.data[0] = last_element  # Colocar el último elemento en la raíz
            heap.heapify(0)  # Reorganizar el montón para mantener la propiedad del montón
    return result




MAX_BOUND = 72
MIN_BOUND = 18
SIZE = 10


def main():
    lst = [Persona (uuid.uuid1 (), randint (MIN_BOUND, MAX_BOUND),uuid.uuid1()) for _ in range (SIZE)]

    print ("Lista original:")
    print ("\n".join (map (str, lst)))
    print ()

    print ("HeapSort (Maximal):")
    print ("\n".join (map (str, heapSort (lst, config=True))))
    print ()

    print ("HeapSort (Minimal):")
    print ("\n".join (map (str, heapSort (lst, config=False))))


main ()
