from time import time
from random import randint

SEED = 1e3
SIZE = 1e4
TESTS = 10
#SandBoxing
#Pre : s1, s2 are sorted
def merge(s1, s2): #--> O(n) why ?
    result = []
    s1_index, s2_index = 0,0
    while s1_index < len(s1) and s2_index < len(s2):
        s1_element, s2_element = s1[s1_index], s2[s2_index]
        if s1_element <= s2_element:
            s1_index += 1
            result.append(s1_element)
        else:
            s2_index += 1
            result.append(s2_element)
    # Remaining elements on left-side
    if s1_index < len(s1):
        result += s1[s1_index:]
    # Remaining elements on right-side
    if s2_index < len(s2):
        result += s2[s2_index:]
    return result

def merge_sort( s ):
    # 0 -  La secuencia es divisible ?
    size = len(s)
    if size <= 1 :
            return s[:] #--> subsequence from 0 --> len(s)
    # 1 -  Dividir la secuencia en mitades
    # 2 -  Ordenar Las mitades ( n//2 )
    half_1,half_2 = merge_sort(s[:(size//2)]), merge_sort(s[(size//2):])
    # 3 -  Mezclar las mitades
    return merge(half_1, half_2)

def sortElement(index, s):
    element, k = s[index], index-1
    while k >= 0 and element < s[k]:
        s[k], s[index], index = element, s[k], k
        k= k-1

def insertionSort(s):
    w = s[:]
    for index in range(1,len(w)):
        sortElement(index, w)
    return w


def main():
    for tests in range(int(TESTS)):
        s = [randint(-1*SEED,SEED) for i in range(randint(1,SIZE))]
        time_0 = time()
        s_sorted_ms = merge_sort( s )
        time_1 = time()
        ms_time = time_1-time_0
        time_2 = time()
        s_sorted_is = insertionSort( s )
        time_3 = time()
        is_time = time_3-time_2

        #print('Sorting ', s, 'MS with result: ', s_sorted_ms)
        #print('Sorting ', s, 'IS with result: ', s_sorted_is)
        print('MS took', ms_time, 'IS took', is_time, (is_time > ms_time))


main()
