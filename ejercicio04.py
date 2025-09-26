# Ejercicio 04 - Verificar número primo
def es_primo(n):
    if n<2: return False
    i=2
    while i*i<=n:
        if n%i==0: return False
        i+=1
    return True
if __name__ == '__main__':
    for x in [1,2,3,4,16,17,19,20]:
        print(x, 'es primo?' , es_primo(x))
