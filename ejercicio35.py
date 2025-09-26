# Ejercicio 35 - Merge sort (implementación simple)
def merge_sort(a):
    if len(a)<=1: return a
    m=len(a)//2
    L=merge_sort(a[:m]); R=merge_sort(a[m:])
    res=[]; i=j=0
    while i<len(L) and j<len(R):
        if L[i]<=R[j]: res.append(L[i]); i+=1
        else: res.append(R[j]); j+=1
    res.extend(L[i:]); res.extend(R[j:])
    return res
if __name__ == '__main__':
    print(merge_sort([5,2,9,1,5,6]))
