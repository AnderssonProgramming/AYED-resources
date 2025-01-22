from sys import stdin

class QueueWithTwoStacks:
    def __init__(self):
        self.enqueue_stack = []
        self.dequeue_stack = []

    def put(self, value):
        self.enqueue_stack.append(value)

    def pop(self):
        if not self.dequeue_stack:
            while self.enqueue_stack:
                self.dequeue_stack.append(self.enqueue_stack.pop())
        return self.dequeue_stack.pop()

    def peek(self):
        if not self.dequeue_stack:
            while self.enqueue_stack:
                self.dequeue_stack.append(self.enqueue_stack.pop())
        return self.dequeue_stack[-1]

def process_queries(queries):
    queue = QueueWithTwoStacks()
    results = []
    for query in queries:
        if query[0] == 1:
            queue.put(query[1])
        elif query[0] == 2:
            queue.pop()
        elif query[0] == 3:
            results.append(queue.peek())
    return results

def main():
    while True:
        line = stdin.readline().strip()
        if not line:
            break
        q = int(line)
        queries = [list(map(int, stdin.readline().strip().split())) for _ in range(q)]
        results = process_queries(queries)
        for result in results:
            print(result)

if __name__ == "__main__":
    main()


