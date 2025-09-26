# Ejercicio 10 - Comprobar anagrama
from collections import Counter
def es_anagrama(a,b):
    return Counter(a.replace(' ','').lower())==Counter(b.replace(' ','').lower())
if __name__ == '__main__':
    print(es_anagrama('roma','amor'))
