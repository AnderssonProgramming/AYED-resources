from sys import stdin
import math


def potencia(size):
    if not math.log(size, 2).is_integer():
        return False
    else:
        return True


def one_matrix(b_list, size):
    matrix = [[0 for i in range(size)] for j in range(size)]
    index = 0
    for row in range(size):
        for column in range(size):
            if b_list[index] == 'T':
                matrix[row][column] = 1
            else:
                matrix[row][column] = -1
            index += 1
    return inner_product(matrix, size)


def inner_product(matrix, size):
    status = True
    product = 0
    for row in range(size-1):
        for column in range(size):
            product = product + matrix[row][column]*matrix[row+1][column]
        if product != 0:
            status = False
    return status


def main():
    size = int(stdin.readline().strip())
    if potencia(size):
        boolean_list = (stdin.readline().strip()).split()
        if size == 1 and boolean_list[0] == 'F':
            print("No Hadamard")
        elif one_matrix(boolean_list, size):
            print("Hadamard")
        else:
            print("No Hadamard")
    else:
        print("Imposible")


if __name__ == '__main__':
    main()
