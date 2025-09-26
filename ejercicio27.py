# Ejercicio 27 - Rot13 (cifrado sencillo)
def rot13(s):
    res=''
    for ch in s:
        if 'a'<=ch<='z': res+=chr((ord(ch)-97+13)%26+97)
        elif 'A'<=ch<='Z': res+=chr((ord(ch)-65+13)%26+65)
        else: res+=ch
    return res
if __name__ == '__main__':
    print(rot13('Hola Mundo'))
