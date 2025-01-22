START = 1
def addElement(element, seq):                                         #Cost (O)    #Times (O)  #Cost (Ohm)    #Times (Ohm)
    element_index = 0                                                 #c1             1            c1             1
    while not (seq[element_index] > element):                         #c2            n+1           c2             1
        element_index = element_index + 1                             #c3             n            c3             0
    return seq[:element_index] + [element] + seq[element_index:]      #(n+1)          1            (n+1)          1
                                                                            #T(n) = O(n)                  T(n) = Ohm(n)
def insertionSort(seq):                         #Cost (O)    Times(O)    Cost(Ohm)      Times(Ohm)
    result = seq[:START]                        #   1           1             1               1
    for e in range(START, len(seq)):            #   c2           n            c2              n
        result = addElement(seq[e], result)     #   n           n-1           n               n-1
    return result                               #   c4            1            c4              1
                                                     # T(n) = O(n^2)            T(n) = Ohm(n^2)
print(insertionSort([4, 3, 2, 1, -5]))