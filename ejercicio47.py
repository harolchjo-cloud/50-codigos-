# Ejercicio 47 - Guardar y leer texto en archivo
def guardar_texto(ruta, texto):
    with open(ruta,'w',encoding='utf-8') as f: f.write(texto)
def leer_texto(ruta):
    with open(ruta,'r',encoding='utf-8') as f: return f.read()
if __name__ == '__main__':
    ruta='/mnt/data/ejemplo_ej47.txt'
    guardar_texto(ruta, 'Hola desde ejercicio 47')
    print(leer_texto(ruta))
