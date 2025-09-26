# Ejercicio 37 - Conversión de lista a diccionario index:valor
def a_dict(lista):
    return {i:lista[i] for i in range(len(lista))}
if __name__ == '__main__':
    print(a_dict(['a','b','c']))
