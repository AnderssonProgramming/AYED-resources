from sys import stdin


## Wonder Square
def longitudCentro(x, y, size):
    A = (size//2, size//2)
    B = (x,y)
    return max(abs(B[0] - A[0]), abs(B[1] - A[1]))

def wonderSquare(n):
    size = 2*n - 1
    square = [[0 for j in size] for i in size]
    return square

wonderSquare(3)
