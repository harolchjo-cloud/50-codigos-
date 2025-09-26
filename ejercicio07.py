# Ejercicio 07 - Palíndromo
def es_palindromo(s):
    s = ''.join(ch.lower() for ch in s if ch.isalnum())
    return s == s[::-1]
if __name__ == '__main__':
    for t in ['Ana', 'reconocer', 'Python']:
        print(t, es_palindromo(t))
