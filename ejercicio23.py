# Ejercicio 23 - Número de dígitos de un número
def cuenta_digitos(n):
    return len(str(abs(int(n))))
if __name__ == '__main__':
    print(cuenta_digitos(12345))
