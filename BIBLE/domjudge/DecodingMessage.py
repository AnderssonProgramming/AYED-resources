from sys import stdin

def decoding(message):
    real = ''#['Hey', 'good', 'lawyer']
    i = 0
    j = 0
    while i < len(message):
        if len(message[i]) > j:
            real += message[i][j] #How
            j += 1
        i += 1
    return real

def main():
    casos = int(stdin.readline().strip())
    blanck = stdin.readline().strip()
    for c in range(casos):
        print('Case #{}:'.format(c+1))
        message = stdin.readline().strip().split()
        while message:
            print(decoding(message))
            message = stdin.readline().strip().split()

main()

'''
2

Hey good lawyer
as I previously previewed
yam does a soup

First I give money to Teresa
after I inform dad of
your horrible soup

'''