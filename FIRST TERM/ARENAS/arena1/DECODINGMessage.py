from sys import stdin
def write(line):                                                                    # costo   pasos
    words = []                                                                      #   1       1
    index = 0                                                                       #   1       1

    for i in line:
        # si el tamaño de la palabra es mayor que index entonces se
        # agrega la letra i-sima de la palabra i-sima y la variable aumenta
        if len(i) > index:                                                          #   1       n - 1
            words.append(i[index])                                                  #   1       n - 1
            index += 1                                                              #   1       n - 1
    # unimos las letras y las imprimimos como palabras
    words = map(str, words)                                                         #   1       1
    print("".join(words))                                                           #   1       1                                                                           # Total O = (n), omega = 1
def main():                                                                         # costo   pasos
    # leemos la primera linea - rango
    rango = int(stdin.readline().strip())                                           #   1       1
    empty = stdin.readline()                                                        #   1       1
    for i in range(rango):                              #   1       j
        print("Case #" + str(i + 1) + ":")                                          #   1       j - 1
        line = stdin.readline().strip().split(" ")                                  #   1       j - 1
        while len(line[0]) > 0:                                                     #   1       j - 1
            write(line)                                                              # write(n)  j - 1
            line = stdin.readline().strip().split(" ")                              # 1         j - 1                                                                               # Total O = (n), omega = 1
main()