# Ejercicio 40 - Rotar lista a la derecha k posiciones
def rotar(lista,k):
    k=k%len(lista) if lista else 0
    return lista[-k:]+lista[:-k]
if __name__ == '__main__':
    print(rotar([1,2,3,4,5],2))
