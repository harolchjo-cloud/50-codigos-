# Ejercicio 32 - Generar tabla de multiplicar (n)
def tabla(n, hasta=10):
    return [n*i for i in range(1,hasta+1)]
if __name__ == '__main__':
    print(tabla(7))
