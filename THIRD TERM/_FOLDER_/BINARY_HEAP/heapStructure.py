import math
import uuid
from random import randint
from sys import stdin

class Heap:
    def __init__(self, data=[], config=True):
        self.data = []
        self.config = config
        self.build(data[:])

    def left(self, index):
        return 2 * index + 1

    def right(self, index):
        return 2 * (index + 1)

    def parent(self, index):
        return (index - 1) // 2

    def height(self):
        return math.ceil(math.log(len(self.data), 2))

    def __len__(self):
        return len(self.data)

    def insert(self, new):
        self.data.append(new)
        self.build()

    def update(self, old, new):
        self.delete(old)
        self.insert(new)

    def delete(self, to_delete):
        if len(self) == 0:
            raise Exception("Heap is empty")
        if to_delete not in self.data:
            raise Exception("Element not in heap")
        self.data.remove(to_delete)
        self.build()

    def build(self, data=[]):
        if data and len(data) > 0 and isinstance(data, list):
            self.data = data
        for index in range(len(self) // 2, -1, -1):
            self.heapify(index)

    def heapify(self, index):
        if self.config:
            self.max_heapify(index)
        else:
            self.min_heapify(index)

    def max_heapify(self, index):
        left_index, right_index, largest_index = self.left(index), self.right(index), index
        if left_index < len(self) and self.data[largest_index] < self.data[left_index]:
            largest_index = left_index
        if right_index < len(self) and self.data[largest_index] < self.data[right_index]:
            largest_index = right_index
        if largest_index != index:
            self.data[largest_index], self.data[index] = self.data[index], self.data[largest_index]
            self.max_heapify(largest_index)

    def peek(self):
        return self.data[0]

    def min_heapify(self, index):
        left_index, right_index, largest_index = self.left(index), self.right(index), index
        if left_index < len(self) and self.data[largest_index] > self.data[left_index]:
            largest_index = left_index
        if right_index < len(self) and self.data[largest_index] > self.data[right_index]:
            largest_index = right_index
        if largest_index != index:
            self.data[largest_index], self.data[index] = self.data[index], self.data[largest_index]
            self.max_heapify(largest_index)

class PriorityQueue:
    def __init__(self, data=[], config=False):
        self.data = Heap(data, config)

    def enqueue(self, new):
        self.data.insert(new)

    def dequeue(self):
        if len(self) == 0:
            raise Exception("Underflow")
        to_dequeue = self.data.peek()
        self.data.delete(to_dequeue)
        return to_dequeue

class PrintJob:
    def __init__(self, priority):
        self.priority = priority

def print_job_time(queue, position):
    pq = PriorityQueue(queue, config=True)
    time = 0
    while len(pq) > 0:
        job = pq.dequeue()
        time += 1
        if position == 0:
            if job.priority == queue[position]:
                return time
        else:
            position -= 1
    return time

def main():
    test_cases = int(stdin.readline().strip())
    for _ in range(test_cases):
        n, m = map(int, stdin.readline().strip().split())
        queue = list(map(int, stdin.readline().strip().split()))
        print(print_job_time(queue, m))

main()
