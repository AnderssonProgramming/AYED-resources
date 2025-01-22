#H. Para la implementación de Merge en el algoritmo merge_sort visto en
# clase, haga el análisis temporal por métdodo de factores con función
# cáracteristica para el peor y el mejor de los casos

                                                                # Peor caso: (len(s1)) = len((s2))
def merge(s1, s2):                                              # Costo     #Tiempo
    result = []                                                 # c1         1
    s1_index, s2_index = 0,0                                    # c2         1
    while s1_index < len(s1) and s2_index < len(s2):            # c3         n
        s1_element, s2_element = s1[s1_index], s2[s2_index]     # c4         n - 1
        if s1_element <= s2_element:                            # c5         n - 1
            s1_index += 1                                       # c6         n - 1
            result.append(s1_element)                           # c7         n - 1
        else:                                                   # c8         n - 1
            s2_index += 1                                       # c9         n - 1
            result.append(s2_element)                           # c10        n - 1
    if s1_index < len(s1):                                      # c11        1
        result += s1[s1_index:]                                 # c12        1
    if s2_index < len(s2):                                      # c13        1
        result += s2[s2_index:]                                 # c14        1
    return result

                                                                # Total = n(c3 + c4 + c5 + c6 + c7 + c8 + c9 + c10)
                                                                # + c1 + c2 - c4 - c5 - c6 - c7 - c8 - c9 - c10 + c11
                                                                # + c12 + c13 + c14
                                                                # O(n) : Lineal


                                                                # Mejor caso: (len(s1)) = len((s2)) = 1
def merge(s1, s2):                                              # Costo     # Tiempo
    result = []                                                 # c1         1
    s1_index, s2_index = 0,0                                    # c2         1
    while s1_index < len(s1) and s2_index < len(s2):            # c3         2
        s1_element, s2_element = s1[s1_index], s2[s2_index]     # c4         1
        if s1_element <= s2_element:                            # c5         1
            s1_index += 1                                       # c6         1
            result.append(s1_element)                           # c7         1
        else:                                                   # c8         1
            s2_index += 1                                       # c9         1
            result.append(s2_element)                           # c10        1
    if s1_index < len(s1):                                      # c11        1
        result += s1[s1_index:]                                 # c12        1
    if s2_index < len(s2):                                      # c13        1
        result += s2[s2_index:]                                 # c14        1
    return result

                                                                    # Total = c1 + c2 + 2*c3 + c4 + c5 + c6 + c7
                                                                    # + c8 + c9 + c10 +c11 + c12 + c13 + c14
                                                                    # O(1) : Primitiva / Constante
