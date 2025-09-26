# Ejercicio 06 - Factorial (recursivo)
def factorial(n):
    if n<0: raise ValueError('n negativo')
    return 1 if n<=1 else n*factorial(n-1)
if __name__ == '__main__':
    print('5! =', factorial(5))
