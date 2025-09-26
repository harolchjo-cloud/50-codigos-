# Ejercicio 30 - Validar correo simple
import re
def valida_email(e):
    return re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', e) is not None
if __name__ == '__main__':
    print(valida_email('test@example.com'), valida_email('no-valido@'))
