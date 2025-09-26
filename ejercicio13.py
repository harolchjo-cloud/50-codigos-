# Ejercicio 13 - Contar palabras en una frase
def contar_palabras(s):
    return len([w for w in s.strip().split() if w])
if __name__ == '__main__':
    print(contar_palabras('  Hola  mundo desde Python  '))
