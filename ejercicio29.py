# Ejercicio 29 - Eliminación de duplicados preservando orden
def sin_duplicados(seq):
    vistos=set(); res=[]
    for x in seq:
        if x not in vistos:
            vistos.add(x); res.append(x)
    return res
if __name__ == '__main__':
    print(sin_duplicados([1,2,2,3,1,4]))
