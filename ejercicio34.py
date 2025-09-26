# Ejercicio 34 - Conteo de dígitos pares e impares
def pares_impares(n):
    pares=impares=0
    for d in str(abs(int(n))):
        if int(d)%2==0: pares+=1
        else: impares+=1
    return pares,impares
if __name__ == '__main__':
    print(pares_impares(1234567890))
