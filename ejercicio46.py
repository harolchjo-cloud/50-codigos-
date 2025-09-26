# Ejercicio 46 - Simulación simple de fila (cola) con listas
from collections import deque
def procesar_eventos(eventos):
    q=deque(); procesados=[]
    for ev in eventos:
        if ev[0]=='push': q.append(ev[1])
        elif ev[0]=='pop' and q: procesados.append(q.popleft())
    return procesados
if __name__ == '__main__':
    evs=[('push',1),('push',2),('pop',None),('push',3),('pop',None)]
    print(procesar_eventos(evs))
