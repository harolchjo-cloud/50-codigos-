# Ejercicio 45 - Cuenta monedas (cambio mínimo con monedas ilimitadas - greedy para monedas canonicas)
def cambio_minimo(cantidad, monedas=[100,50,20,10,5,1]):
    res={}
    for m in monedas:
        res[m]=cantidad//m; cantidad%=m
    return res
if __name__ == '__main__':
    print(cambio_minimo(289))
