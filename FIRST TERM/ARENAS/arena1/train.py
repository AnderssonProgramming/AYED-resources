from sys import stdin
def inputCase():
    dicTrain = {}
    n = int(stdin.readline().strip())
    for case in range(n):
        lenTrain = int(stdin.readline().strip())
        orderTrain = stdin.readline().strip().split()  # divide la cadena en una lista
        dicTrain[case] = [int(vagon) for vagon in orderTrain]  # convierte cada elemento de la lista a un entero
    return dicTrain
def orderList(listTrain):
    steps = 0
    n = len(listTrain)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if listTrain[j] > listTrain[j + 1]:
                listTrain[j], listTrain[j + 1] = listTrain[j + 1], listTrain[j]
                steps += 1
    return steps
def orderDic(dicTrain):
    dicCaseSteps = {}
    for key in dicTrain.keys():
        steps = orderList(dicTrain[key])
        dicCaseSteps[key] = steps
    return dicCaseSteps
def outputCase(dicCaseSteps):
    for key in dicCaseSteps.keys():
        print("Optimal train swapping takes", dicCaseSteps[key], "swaps.")
def main():
    dicTrain = inputCase()
    dicCaseSteps = orderDic(dicTrain)
    outputCase(dicCaseSteps)
main()
