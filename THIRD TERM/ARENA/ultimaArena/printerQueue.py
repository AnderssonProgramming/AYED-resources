from sys import stdin
from collections import deque

def calculate_print_time(n, m, priorities):
    # Crea una cola con tuplas (prioridad, es_mi_trabajo)
    queue = deque((priority, i == m) for i, priority in enumerate(priorities))

    # Ordena las prioridades en orden descendente
    sorted_priorities = sorted(priorities, reverse=True)

    time_until_printed = 0
    while True:
        # Toma el primer trabajo en la cola
        job = queue.popleft()

        # Si hay un trabajo en la cola con mayor prioridad, mueve el trabajo actual al final de la cola
        if job[0] < sorted_priorities[0]:
            queue.append(job)
        else:
            # Imprime el trabajo y aumenta el tiempo
            time_until_printed += 1
            sorted_priorities.pop(0)

            # Si el trabajo impreso es tu trabajo, termina el bucle
            if job[1]:
                break

    return time_until_printed

def main():
    test_cases = int(stdin.readline().strip())
    for _ in range(test_cases):
        n, m = map(int, stdin.readline().strip().split())
        priorities = list(map(int, stdin.readline().strip().split()))
        print(calculate_print_time(n, m, priorities))

main()
