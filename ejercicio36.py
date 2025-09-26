# Ejercicio 36 - Número capicúa (num igual invertido)
def capicua(n): return str(n)==str(n)[::-1]
if __name__ == '__main__':
    print(capicua(12321), capicua(12345))
