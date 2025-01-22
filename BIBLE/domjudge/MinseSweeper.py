from sys import stdin

def transformXY(i,j):
    return (i+1, j+1)

def propagateSectorCalculation(matrix, row, column):
    pointTransformed = transformXY(row, column)
    for i in range(-1, 2):  # [-1,0,1]
        for j in range(-1, 2):  # [-1,0,1]
            if (i != 0 or j != 0) and matrix[pointTransformed[0] + i][pointTransformed[1] + j] != '*':
                matrix[pointTransformed[0] + i][pointTransformed[1] + j] += 1
    matrix[pointTransformed[0]][pointTransformed[1]] = '*'

def calculateMineSweeper(field, rows, columns):
    calc_f = [[ 0 for j in range(columns + 2)] for i in range(rows + 2)]
    for row in range(rows):
        for column in range(columns):
             if field[row][column] == '*':
                 propagateSectorCalculation(calc_f, row, column)
    return calc_f

def printCalculationMatrix(matrix):
    matrix_print = matrix[1:len(matrix)-1]
    for row in matrix_print:
        print(''.join(map(str, row[1:len(row)-1])))

def problemOutput(formatter, index, matrix):
    print(formatter.format(index))
    printCalculationMatrix(matrix)
    print()

def main():
    fieldMessage, index = 'Field #{}:', 1
    rows, columns = map(int, stdin.readline().strip().split())
    while rows != 0 or columns != 0 :
        field = []
        for row in range(rows):
            field.append(stdin.readline().strip())
        problemOutput(fieldMessage, index, calculateMineSweeper(field, rows, columns))
        index+=1
        rows, columns = map(int, stdin.readline().strip().split())

main()