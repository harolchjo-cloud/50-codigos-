# Ejercicio 31 - Sumar matrices (misma dimension)
def adicionr_matrices(A,B):
    return [[A[i][j]+B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
if __name__ == '__main__':
    print(adicionr_matrices([[1,2],[3,4]], [[5,6],[7,8]]))
