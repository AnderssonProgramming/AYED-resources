from sys import stdin


def isCorrect(cadena):
    A = ["(", "["]
    dictA = {"(": "A", "[": "B"}
    dictC = {")": "A", "]": "B"}
    s = []
    for i in range(len(cadena)):
        if cadena[i] in A:
            s.insert(0, dictA[cadena[i]])
        elif len(s) == 0:
            return False
        else:
            if dictC[cadena[i]] == s[0]:
                s.pop(0)
            else:
                return False
    if len(s) == 0:
        return True
    return False


def main():
    n = stdin.readline().strip()
    for i in range(int(n)):
        cadena = stdin.readline().strip()
        if isCorrect(cadena):
            print("Yes")
        else:
            print("No")


main()
