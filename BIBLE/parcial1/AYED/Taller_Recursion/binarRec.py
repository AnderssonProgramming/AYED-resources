def binary(n):
    return [] if n < 1 else binary(n // 2) + [n % 2]

def main(n):
    return binary(n)


print(binary(123))
print(binary(12))
print(binary(53))
print(binary(544))
