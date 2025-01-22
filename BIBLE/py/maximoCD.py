def divisores(num1):
    listaD = [i for i in range(1, num1+1) if num1 % i == 0]
    return listaD
    

def MCD(num1, num2):
    divs1 = divisores(num1)
    divs2 = divisores(num2)
    maxC = 0
    for num in divs1:
        if num in divs2:
            maxC = num
    print(maxC)
MCD(2, 6)
