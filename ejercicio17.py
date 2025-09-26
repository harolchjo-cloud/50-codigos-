# Ejercicio 17 - Buscar elemento en lista (retorna índice o -1)
def buscar(lista, x):
    for i,val in enumerate(lista):
        if val==x: return i
    return -1
if __name__ == '__main__':
    print(buscar([3,5,7,9],7))
