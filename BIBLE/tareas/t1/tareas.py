Function mystery(n)               # Cost    Time
    r := 0      	   	          #   1    	  1
    for i := 1 to n – 1 do        #   1      n-1
        for j := i + 1 to n do    #   1       n
            for k := 1 to j do    #   1       n
                r := r + 1	      #   1      n-1
    return r		              #   1       1
    #n^3-n^2+n-1 ---> O(n^3)

Function pesky(n)                   # Cost      Times
    r := 0                          #    C1       1
    for i := 1 to n do              #    C2       n
        for j := 1 to i do          #    C3       n
            for k := j to i + j do  #    C4       n
                r := r + 1          #    C5      n-1
    return r                        #    C6       1

# n ^ 3 + n + 1 ---> O(n^3)

Function prestiferous(n)                  # Cost     Times
    r := 0				                  #  C1        1
    for i := 1 to n do                    #  C2        n
        for j := 1 to i do                #  C3        n
            for k := 1 to i + j do        #  C4        2n
                for l := 1 to i + j – k do#  C5        n
                    r := r + 1            #  C6        n-1
    return r                              #  C7        1

#2n^4 + n + 1 ---> O(n^4)
