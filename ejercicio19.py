# Ejercicio 19 - Validar contraseña simple
def valida_pass(p):
    return len(p)>=8 and any(c.isdigit() for c in p) and any(c.isalpha() for c in p)
if __name__ == '__main__':
    print(valida_pass('abc12345'), valida_pass('short'))
