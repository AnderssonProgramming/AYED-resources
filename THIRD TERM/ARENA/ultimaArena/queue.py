from sys import stdin
import math

def max_j(queue):
    max_el = -math.inf
    for el in queue:
        if el[1] > max_el:
            max_el = el[1]
    return max_el


def find_max_el(queue):
    if len(queue) == 1:
        return True
    aux_q = queue
    aux_q.pop(0)
    if queue[0] < max(aux_q):
        return False
    return True


def main_1():
    n = int(stdin.readline().strip())
    for index in range(n):
        jobs, index = tuple(map(int, stdin.readline().strip().split()))
        lista = list(map(int, stdin.readline().strip().split()))
        temp = []
        for index in range(len(lista)):
            if index == index:
                t = (9999, lista[index])
            else:
                t = (index, lista[index])
            temp += [t]
        modify_queue(temp)

def modify_queue(queue):
    time = 0
    while queue:
        if queue[0][1] == find_max_el(queue):
            time += 1
            if queue[0][0] == 9999:
                break
            del queue[0]
        else:
            temp = queue[0]
            del queue[0]
            queue.append(temp)
    print(time)

def main():
    cases = int(stdin.readline().strip())
    while cases > 0:
        timer = 0
        jobs, my_job = tuple(map(int, stdin.readline().strip().split()))
        initial_q = list(map(int, stdin.readline().strip().split()))
        my_job += initial_q[my_job]
        id = {}
        for index in range(jobs):
            id[index] = index
            print(id[index])
        j = initial_q[0]
        new_queue = initial_q
        print(id[j], id[my_job])

        while id[j] != id[my_job]:
            if j is max_j(new_queue):
                timer += 1
                new_queue.pop(0)
            else:
                aux = j
                new_queue.pop(0)
                new_queue.append(aux)
            j = new_queue[0]
        timer += 1
        print(timer)
        cases -= 1


if __name__ == '__main__':
    main_1()
