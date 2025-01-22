from sys import stdin


def cambio(amount, mem, coins):
    if mem[amount] == 0:
        for coin in coins:
            for index in range(1, len(mem)):
                if index >= coin:
                    mem[index] += mem[index - coin]

    return mem[amount]


def main():
    coins = [1, 5, 10, 25, 50]
    amount = stdin.readline()
    mem = [0 for index in range(30001)]
    mem[0] = 1
    while amount:
        amount = int(amount)
        initial_amount = amount
        maneras = cambio(amount, mem, coins)
        if maneras == 1:
            print("There is only", maneras, "way to produce", initial_amount, "cents change.")
        elif maneras >= 2:
            print("There are", maneras, "ways to produce", initial_amount, "cents change.")

        amount = stdin.readline()


if __name__ == '__main__':
    main()