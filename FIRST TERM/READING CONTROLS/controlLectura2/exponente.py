from sys import stdin
def power(a, n):
    # base case
    if n == 0:
        return 1
    elif n == 1:
        return a
    else:
        #Recursive case
        temp = power(a, n // 2)        # temp = temporal   Guardar la potencia
        if n % 2 == 0:
            return temp * temp
        else:
            return a * temp * temp

def main():
    line = stdin.readline().strip()
    while line:
        a, n = map(int, line.split())
        result = power(a, n)
        print("Result:", result)
        line = stdin.readline().strip()

main()
