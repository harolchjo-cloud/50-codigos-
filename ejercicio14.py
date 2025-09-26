# Ejercicio 14 - Lista de números pares hasta n
def pares_hasta(n):
    return [i for i in range(2,n+1,2)]
if __name__ == '__main__':
    print(pares_hasta(20))
