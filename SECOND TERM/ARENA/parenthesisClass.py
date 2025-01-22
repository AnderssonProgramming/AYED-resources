from sys import stdin

def check_parentheses(s):
    stack = []

    for c in s:
        if c in '([':
            stack.append(c)
        elif c == ')' and stack and stack[-1] == '(':
            stack.pop()
        elif c == ']' and stack and stack[-1] == '[':
            stack.pop()
        else:
            return "No"

    return "Yes" if not stack else "No"

def main():
    n = int(stdin.readline().strip())
    for _ in range(n):
        s = stdin.readline().strip()
        print(check_parentheses(s))

if __name__ == "__main__":
    main()


