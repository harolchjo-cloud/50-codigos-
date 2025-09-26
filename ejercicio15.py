# Ejercicio 15 - multiplicar matrices (2x2 ejemplo)
def mul2x2(a,b):
    return [[a[0][0]*b[0][0]+a[0][1]*b[1][0], a[0][0]*b[0][1]+a[0][1]*b[1][1]],
            [a[1][0]*b[0][0]+a[1][1]*b[1][0], a[1][0]*b[0][1]+a[1][1]*b[1][1]]]
if __name__ == '__main__':
    A=[[1,2],[3,4]]
    B=[[2,0],[1,2]]
    print(mul2x2(A,B))
