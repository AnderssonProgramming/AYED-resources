from sys import stdin
def countPosition(W, H, subregions):
    uncoveredPositions = 0
    for i in range(1, W+1):
        for j in range(1, H+1):
            covered = False
            for subregion in subregions:
                if i >= subregion[0] and i <= subregion[2] and j >= subregion[1] and j <= subregion[3]:
                    covered = True
                    break
            if not covered:
                uncoveredPositions += 1
    return uncoveredPositions

# Leer múltiples entradas desde un archivo
for line in stdin:
    if line.strip() == '':
        continue
    W, H, N = map(int, line.split())
    if W == H == N == 0:
        break

    subregions = []
    for i in range(N):
        X1, Y1, X2, Y2 = map(int, stdin.readline().split())
        subregions.append((min(X1, X2), min(Y1, Y2), max(X1, X2), max(Y1, Y2)))  # Asegurarse de que X1 < X2 y Y1 < Y2

    result = countPosition(W, H, subregions)
    if result == 0:
        print("There is no empty spots.")
    elif result == 1:
        print("There is one empty spot.")
    else:
        print("There are", result, "empty spots.")
