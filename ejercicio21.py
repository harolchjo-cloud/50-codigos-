# Ejercicio 21 - Ordenar palabras por longitud
def ordenar_por_longitud(words):
    return sorted(words, key=len)
if __name__ == '__main__':
    print(ordenar_por_longitud(['python','c','javascript','go']))
