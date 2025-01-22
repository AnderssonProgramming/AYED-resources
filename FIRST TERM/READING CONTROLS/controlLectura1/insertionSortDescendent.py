START=1

def addElement(element, seq):
    element_index = 0
    while element_index < len(seq) and not (seq[element_index] > element):
        element_index = element_index + 1
    return seq[:element_index] + [element] + seq[element_index:]

def insertionSort(seq):
    result = seq[:START]
    for e in range(START, len(seq)):
        result = addElement(seq[e], result)
    return result[::-1]

input_list = [5, 8, -1, 4, 6]

print(insertionSort(input_list))
