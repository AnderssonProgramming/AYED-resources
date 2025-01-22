# -*- coding: utf-8 -*-

from unidecode import unidecode   #Unicode describe cómo se representan los caracteres mediante puntos de código

def leer_cadenas():
    with open('entrada2.txt', 'r') as f:
        return [linea.strip() for linea in f]

def determinar_palindromo(palabra):
    palabra = "".join(unidecode(palabra.lower()).split())
    return palabra == palabra[::-1]

def escribir_resultados(resultados):
    with open('salida2.txt', 'w') as f:
        for cadena, es_palindromo in resultados.items():      #.items se utiliza para obtener una vista de los pares clave-valor (key-value) de un diccionario
            f.write(f"{cadena}: {es_palindromo}\n")

def main():
    print("Determinar si una cadena S es un palíndromo, un palíndromo es aquella sucesión de caracteres en donde ci = cn-i para todo i > 0 : ")

    cadenas = leer_cadenas()
    resultados = {}

    for cadena in cadenas:
        resultados[cadena] = determinar_palindromo(cadena)

    escribir_resultados(resultados)


main()
