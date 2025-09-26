# Ejercicio 18 - Generar lista de cuadrados
def cuadrados(n):
    return [i*i for i in range(1,n+1)]
if __name__ == '__main__':
    print(cuadrados(6))
