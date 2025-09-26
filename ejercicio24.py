# Ejercicio 24 - Suma de elementos pares de una lista
def adicion_pares(lista):
    return sum(x for x in lista if x%2==0)
if __name__ == '__main__':
    print(adicion_pares([1,2,3,4,5,6]))
