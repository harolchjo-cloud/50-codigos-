# Ejercicio 33 - Buscar número máximo y mínimo en lista
def min_max(lista):
    if not lista: return None,None
    mn=mx=lista[0]
    for x in lista[1:]:
        if x<mn: mn=x
        if x>mx: mx=x
    return mn,mx
if __name__ == '__main__':
    print(min_max([3,7,1,9,2]))
