from sys import stdin

def maxCharOcurrence(s):
    # On initial state all characters had zero ocurrencies
    char_count, maxChar, maxOcurrencies = {}, None, 0
    for c in s:
        char_count[c] = 1 + (char_count[c] if c in char_count.keys() else 0)
        if char_count[c] > maxOcurrencies:
            maxOcurrencies, maxChar = char_count[c], c
    return (maxChar, maxOcurrencies)

def main():
    s = stdin.readline().strip()
    print(maxCharOcurrence(s))


main()
