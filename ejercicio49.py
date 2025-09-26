# Ejercicio 49 - Calculadora de promedio por grupos (dict)
def promedios_por_grupo(pares):
    d={}
    for grupo,valor in pares:
        if grupo not in d: d[grupo]=[]
        d[grupo].append(valor)
    return {g: sum(v)/len(v) for g,v in d.items()}
if __name__ == '__main__':
    datos=[('A',5),('B',8),('A',7),('B',6)]
    print(promedios_por_grupo(datos))
