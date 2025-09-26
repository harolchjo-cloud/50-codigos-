# Ejercicio 20 - Contador de frecuencia (diccionario)
def frecuencias(seq):
    d={}
    for s in seq:
        d[s]=d.get(s,0)+1
    return d
if __name__ == '__main__':
    print(frecuencias('abracadabra'))
