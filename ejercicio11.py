# Ejercicio 11 - Suma de cuadrados hasta n
def adicion_cuadrados(n):
    return sum(i*i for i in range(1,n+1))
if __name__ == '__main__':
    print(adicion_cuadrados(5))
