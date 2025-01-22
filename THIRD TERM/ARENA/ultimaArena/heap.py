from sys import stdin

def main():
    n = int(stdin.readline().strip())
    queue = []
    for i in range(n):
        row = stdin.readline().strip().split()
        if row[0] == 'saque' and len(queue) > 0:
            print(queue.pop())
        elif row[0] == 'inserte':
            num = int(row[1])
            queue.append(num)
            queue.sort()


main()

