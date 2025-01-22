from sys import stdin


def main():
    casos = int(stdin.readline().strip())
    for n in range(casos):
        intL = int(stdin.readline().strip())
        permut = stdin.readline().strip().split()
        swaps = 0
        for i in range(1, intL):
            for k in range(i, -1, -1):
                if int(permut[i]) < int(permut[k]):
                    print(permut[i])
                    print(permut[k])
                    swaps += 1
        print('Optimal train swapping takes {} swaps.'.format(swaps))
main()
