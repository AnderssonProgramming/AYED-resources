from sys import stdin


matriz = ['*...', '....', '.*..', '....']#...  , ... , *..
fila = 2
colum = 0
campo2 = matriz[fila - 1: fila + 2]
campo3 = []
for fila in campo2:
    if colum == 0:
        for i in range(colum, colum + 2):
            campo3.append(fila[i])

    else:
        for i in range(colum - 1, colum + 2):
            campo3.append(fila[i])

print(campo2)
print(campo3)