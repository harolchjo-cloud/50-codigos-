# Ejercicio 50 - Generador de contraseñas aleatorias (seguras)
import random, string
def generar_password(long=12):
    pool = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(pool) for _ in range(long))
if __name__ == '__main__':
    print(generar_password(12))
