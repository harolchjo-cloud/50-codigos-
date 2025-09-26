# Ejercicio 38 - Calcular media, mediana y moda
from collections import Counter
def media(nums):
    return sum(nums)/len(nums) if nums else None
def mediana(nums):
    n=sorted(nums); L=len(n)
    if L==0: return None
    mid=L//2
    return n[mid] if L%2 else (n[mid-1]+n[mid])/2
def moda(nums):
    if not nums: return None
    c=Counter(nums); m=max(c.values())
    return [k for k,v in c.items() if v==m]
if __name__ == '__main__':
    datos=[1,2,2,3,4]; print(media(datos), mediana(datos), moda(datos))
