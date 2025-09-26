# Ejercicio 43 - Conversor de base (entero a base b <=36)
def a_base(n,b):
    if n==0: return '0'
    digs = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    neg = n<0; n=abs(n)
    res=''
    while n>0:
        res = digs[n%b] + res
        n//=b
    return ('-' if neg else '')+res
if __name__ == '__main__':
    print(a_base(255,16))
