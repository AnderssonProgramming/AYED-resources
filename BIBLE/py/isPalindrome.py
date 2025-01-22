from sys import stdin

def isPalindrome(s):
    is_palindrome, index = True, 0
    while index < len(s) and is_palindrome:
        is_palindrome = ( s[index] == s[len(s)-(index+1)] )
        index+=1
    return is_palindrome

def main():
    s = stdin.readline().strip()
    while s:
        print(isPalindrome(s))
        s = stdin.readline().strip()

main()

