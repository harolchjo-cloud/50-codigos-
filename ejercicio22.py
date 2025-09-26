# Ejercicio 22 - Merge two sorted lists
def merge(a,b):
    i=j=0; res=[]
    while i<len(a) and j<len(b):
        if a[i]<=b[j]:
            res.append(a[i]); i+=1
        else:
            res.append(b[j]); j+=1
    res.extend(a[i:]); res.extend(b[j:])
    return res
if __name__ == '__main__':
    print(merge([1,3,5],[2,4,6]))
