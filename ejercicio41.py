# Ejercicio 41 - Contador de letras (solo alfabeticas)
def contar_letras(s):
    d={}
    for ch in s.lower():
        if ch.isalpha(): d[ch]=d.get(ch,0)+1
    return d
if __name__ == '__main__':
    print(contar_letras('Hola Mundo!!!'))
