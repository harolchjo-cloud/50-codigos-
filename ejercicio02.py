# Ejercicio 02 - Calculadora simple (funciones)
def adicionr(a,b): return a+b
def diferenciar(a,b): return a-b
def multiplicar(a,b): return a*b
def dividir(a,b):
    if b==0: raise ValueError('Division por cero')
    return a/b
if __name__ == '__main__':
    print('5 + 3 =', adicionr(5,3))
    print('10 / 2 =', dividir(10,2))
