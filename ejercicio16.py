# Ejercicio 16 - Transponer matriz
def transponer(m):
    return [list(row) for row in zip(*m)]
if __name__ == '__main__':
    M=[[1,2,3],[4,5,6]]
    print(transponer(M))
