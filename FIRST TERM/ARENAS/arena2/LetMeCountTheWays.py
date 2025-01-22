import sys

def coin_change(coins, amount):
    dp = [0] * (amount + 1)
    dp[0] = 1
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] += dp[i - coin]
    return dp[amount]

coins = [1, 5, 10, 25, 50]
dp = [0] * 30001
dp[0] = 1
for coin in coins:
    for i in range(coin, 30001):
        dp[i] += dp[i - coin]

for line in sys.stdin:
    amount = int(line.strip())
    ways = dp[amount]
    if ways == 1:
        print(f"There is only 1 way to produce {amount} cents change.")
    else:
        print(f"There are {ways} ways to produce {amount} cents change.")


