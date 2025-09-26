# Ejercicio 09 - Contar vocales en una cadena
def contar_vocales(s):
    return sum(1 for ch in s.lower() if ch in 'aeiouáéíóúü')
if __name__ == '__main__':
    print(contar_vocales('Hola Mundo'))
