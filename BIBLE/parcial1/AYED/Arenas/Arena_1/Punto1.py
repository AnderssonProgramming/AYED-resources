from sys import stdin


def readline():
    return stdin.readline().strip()


def processWords(words):
    index, result = 0, []
    for word in words:                                      # n
        if index < len(word):                               # n - 1
            result.append(word[index])                      # n - 1
            index += 1                                      # n - 1
    return ''.join(map(str, result))


def main():
    cases = int(readline())                                 # 1
    readline()                                              # 1
    for case in range(cases):                               # n
        print('Case #'+str(case+1)+':')                     # n - 1
        # Message Start
        line = readline()                                   # n - 1
        while len(line) > 0:                                # n
            # Process Words
            print(processWords(line.split()))               # n
            line = readline()                               # n - 1
        print()                                             # n -1


main()