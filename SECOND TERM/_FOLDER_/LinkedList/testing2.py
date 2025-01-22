from sys import stdin

def parenthesis(s):

    stack = []

    for c in s:
        if c in ("(["):
            stack.append(c)
        elif c == ")" and stack and stack[-1] == "(":
            stack.pop()
        elif c == "]" and stack and stack[-1] == "[":
            stack.pop()
        else:
            return "No"

    return "Yes" if not stack else "No"

def main():
    n = int(stdin.readline().strip())

    for i in range(n):
        s = stdin.readline().strip()
        print(parenthesis(s))

main()