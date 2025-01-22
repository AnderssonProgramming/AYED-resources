import sys         #Librería para entradas estándar
def pSum(total, n_termino, potencia):               #Power Sum en general con las condiciones
    n_potenciado = n_termino ** potencia
    if total == 0 or total == n_potenciado:
        return 1
    if total < 0 or total < n_potenciado:
        return 0
    return (pSum(total - n_potenciado, n_termino+1, potencia) +
            pSum(total, n_termino+1, potencia))

def pSumP(total, n_termino, potencia, M = {}):        #PowerSum de almacenamiento de información en la memoria
    n_potenciado = n_termino ** potencia
    if total == 0 or total == n_potenciado:
        return 1
    if total < 0 or total < n_potenciado:
        return 0
    return (pSumM(total - n_potenciado, n_termino+1, potencia, M) +
            pSumM(total, n_termino+1, potencia, M))

def pSumM(total, n_termino, potencia, M = {}):          #PowerSum memoria para no repetir cálculos
    if (total, n_termino, potencia) in M.keys():
        return M[(total, n_termino, potencia)]
    M[(total, n_termino, potencia)] = pSumP(total, n_termino, potencia, M)
    return M[(total, n_termino, potencia)]

def main():
    lines = sys.stdin.readlines()                  #Lee entradas estándar por consola
    for i in range(0, len(lines), 2):             #Poner las entradas por línea separada y sin espacio de por medio
        total = int(lines[i].strip())             #Convierte a entero el total quitando el espacio
        potencia = int(lines[i+1].strip())        #Convierte la potencia en entero quitando el espacio
        print(pSum(total, 1, potencia))

main()