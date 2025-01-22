"""ANDERSSON DAVID SÁNCHEZ MÉNDEZ"""

START = 1
def addElement(element, seq):                                          
    element_index = 0                                                        
    while element_index < len(seq) and not (seq[element_index][1] > element[1]):                                                                 
        element_index = element_index + 1                                          
    return seq[:element_index] + [element] + seq[element_index:]            

def insertionSort(seq):                              
    result = seq[:START]                           
    for e in range(START, len(seq)):           
        result = addElement(seq[e], result)
    return result

personas = [("Juan", 25), ("María", 30), ("Pedro", 20), ("Luisa", 18)]
ordenarPersonas= insertionSort(personas)
print("Lista ordenada por edad:", ordenarPersonas)
print("Persona más joven:", ordenarPersonas[0][0])


