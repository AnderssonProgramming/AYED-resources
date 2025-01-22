from sys import stdin
import heapq

class Cell:
    def __init__(self, number):
        self.number = number
        self.connections = {}  # {destination cell number: time required}

def dijkstra(maze, start, time_limit):
    distances = {cell_num: float('inf') for cell_num in maze}
    distances[start] = 0
    pq = [(0, start)]

    while pq:
        curr_dist, curr_cell = heapq.heappop(pq)

        if curr_dist > distances[curr_cell]:
            continue

        for neighbor, time_cost in maze[curr_cell].connections.items():
            total_time = curr_dist + time_cost
            if total_time < distances[neighbor]:
                distances[neighbor] = total_time
                heapq.heappush(pq, (total_time, neighbor))

    return sum(1 for dist in distances.values() if dist <= time_limit)

def main():
    test_cases = int(stdin.readline().strip())

    for _ in range(test_cases):
        stdin.readline()  # Leer línea en blanco
        N = int(stdin.readline().strip())
        line = stdin.readline().split()
        if len(line) == 1:
            E = int(line[0])
            T = int(stdin.readline().strip())
        else:
            E, T = map(int, line)

        maze = {i: Cell(i) for i in range(1, N+1)}

        M = int(stdin.readline().strip())
        for _ in range(M):
            a, b, time = map(int, stdin.readline().split())
            maze[a].connections[b] = time

        mice_reached_exit = dijkstra(maze, E, T)
        print(mice_reached_exit)

        if _ < test_cases - 1:
            print()

if __name__ == "__main__":
    main()
