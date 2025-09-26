# Ejercicio 39 - Validar número entero en rango [a,b]
def validar(n,a,b):
    try:
        n=int(n)
        return a<=n<=b
    except:
        return False
if __name__ == '__main__':
    print(validar('5',1,10), validar('x',1,10))
