# Ejercicio 08 - Ordenar lista (ordenamiento por burbuja)
def burbuja(a):
    n=len(a)
    for i in range(n):
        for j in range(0,n-i-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
    return a
if __name__ == '__main__':
    l=[5,3,8,1,2]
    print('Original:', l)
    print('Ordenado:', burbuja(l.copy()))
