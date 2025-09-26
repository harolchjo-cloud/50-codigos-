# Ejercicio 42 - Suma recursiva de lista
def adicion_lista(a):
    if not a: return 0
    return a[0]+adicion_lista(a[1:])
if __name__ == '__main__':
    print(adicion_lista([1,2,3,4,5]))
