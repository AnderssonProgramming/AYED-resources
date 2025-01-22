from sys import stdin

def trib(n, back):
    n, back = int(n), int(back)
    global cont
    cont = cont + 1
    if n <= 1:
        return 0
    elif n == 1:
        return 1
    acum = 0
    for i in range(1, back + 1):
        acum = acum + trib(n - i, back)
    return acum


def main():
    case = 1
    n, back = stdin.readline().strip().split()
    while n:
        global cont
        cont = 0
        trib(n, back)
        print("Case {}:".format(case), cont)
        case += 1
        n, back = stdin.readline().strip().split()


main()
