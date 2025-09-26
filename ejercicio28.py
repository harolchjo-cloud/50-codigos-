# Ejercicio 28 - Juego adivina número (versión sin input para tests)
import random
def jugar(suponer):
    secreto = 42  # fijo para pruebas
    if suponer < secreto: return 'Más alto'
    if suponer > secreto: return 'Más bajo'
    return '¡Acertaste!'
if __name__ == '__main__':
    print(jugar(50))
    print(jugar(42))
