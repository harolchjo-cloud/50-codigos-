# Ejercicio 44 - Encontrar subcadena más larga sin repetir caracteres (sliding window)
def mas_larga_sin_repetir(s):
    seen={}; start=0; maxs=''
    for i,ch in enumerate(s):
        if ch in seen and seen[ch]>=start:
            start=seen[ch]+1
        if i-start+1>len(maxs):
            maxs=s[start:i+1]
        seen[ch]=i
    return maxs
if __name__ == '__main__':
    print(mas_larga_sin_repetir('abrkaabcdefghijjxxx'))
