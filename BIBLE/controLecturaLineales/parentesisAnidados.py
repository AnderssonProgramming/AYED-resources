from sys import stdin


def parentAnind(cadena):
    s = []
    parentesis = {"(": ")", "[": "]", "{": "}"}
    for i in range(len(cadena)):
        if cadena[i] in parentesis:
            s.append(cadena[i])
        elif len(s) > 0:
            if s[-1] not in parentesis.values():
                if cadena[i] == parentesis[s[-1]]:
                    s.pop()
        else:
            return False

    if len(s) == 0:
        return True
    return False


def main():
    for i in range(3):
        cadena = stdin.readline().strip()
        print(parentAnind(cadena))



main()

"""
[{((())())()}]{[]}
(({}))[]
)([])(
(){[]([]
[{((())())()}]{{[]}
"""
