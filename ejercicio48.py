# Ejercicio 48 - Validar matriz identidad
def es_identidad(m):
    n=len(m)
    for i in range(n):
        for j in range(n):
            if (i==j and m[i][j]!=1) or (i!=j and m[i][j]!=0):
                return False
    return True
if __name__ == '__main__':
    print(es_identidad([[1,0,0],[0,1,0],[0,0,1]]))
