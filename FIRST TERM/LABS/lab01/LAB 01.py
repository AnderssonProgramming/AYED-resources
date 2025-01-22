from sys import stdin
import math
from time import time
from random import randint
SIZE = 1e3
LOWER_BOUND = 33
UPPER_BOUND = 169
DICT_SIZE = 256
def createRandomString():
    s = [ chr(randint(LOWER_BOUND, UPPER_BOUND)) for i in range(int(SIZE))]
    return str(s)
def contar(ci, s):
    ocurrencias = 0
    for c in s:
        if c == ci:
            ocurrencias = ocurrencias + 1
    return ci, ocurrencias
def contar_two(ci, s, ocurrencies = {}):
    ocurrencies[ci] = (ocurrencies[ci] + 1) if ci in ocurrencies.keys() else 1
    return ci, ocurrencies[ci]
def contar_three(ci, s, ocurrencies = []):
    ocurrencies[ord(ci)] = ocurrencies[ord(ci)] + 1
    return ci, ocurrencies[ord(ci)]
def determineMaxFreq(s):
    max_occur, max_char = -math.inf, None
    for ci in s:
        ci, occur_ci = contar(ci, s)
        if occur_ci >= max_occur:
            max_occur, max_char = occur_ci, min(ci, max_char) if max_char else ci
    return "{} --> {}".format(max_char, max_occur)
def determineMaxFreq_two(s):
    max_occur, max_char, ocurrencies = -math.inf, None, {}
    for ci in s:
        ci, occur_ci = contar_two(ci, s, ocurrencies)
        if occur_ci >= max_occur:
            max_occur, max_char = occur_ci, min(ci, max_char) if max_char else ci
    return "{} --> {}".format(max_char, max_occur)
def determineMaxFreq_three(s):
    max_occur, max_char, ocurrencies = -math.inf, None, [ 0 for i in range(DICT_SIZE)]
    for ci in s:
        ci, occur_ci = contar_three(ci, s, ocurrencies)
        if occur_ci >= max_occur:
            max_occur, max_char = occur_ci, min(ci, max_char) if max_char else ci
    return "{} --> {}".format(max_char, max_occur)
def main():
    line = stdin.readline().strip()
    while line:
        print(determineMaxFreq_two(line))
        line = stdin.readline().strip()
#main()
def measureOcurrencies():
   s = createRandomString()
   t0 = time()
   determineMaxFreq(s)
   t1 = time()
   print("Time for max ocurrencies #1 {}".format(t1-t0))
   t0 = time()
   determineMaxFreq_two(s)
   t1 = time()
   print("Time for max ocurrencies #2 {}".format(t1-t0))
   t0 = time()
   determineMaxFreq_three(s)
   t1 = time()
   print("Time for max ocurrencies #3 {}".format(t1-t0))
measureOcurrencies()
