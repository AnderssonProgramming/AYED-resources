from sys import stdin
from collections import deque

def time_to_print(n,m,priorities):

    queue = deque([(priority, i == m) for i, priority in enumerate(priorities)])

    sorted_time = sorted(priorities,reverse = True)

    time_until_printed = 0

    while True:
        job = queue.popleft()

        if job[0] < sorted_time[0]:
            queue.append(job)

        else:
            time_until_printed += 1
            sorted_time.pop(0)

            if job[1]:
                break
    return time_until_printed

def main():
    n = int(stdin.readline().strip())

    for i in range(n):

        n,m = map(int, stdin.readline().strip().split())
        priorities = list(map(int,stdin.readline().strip().split()))

        print(time_to_print(n,m,priorities))
main()
