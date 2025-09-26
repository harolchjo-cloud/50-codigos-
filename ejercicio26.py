# Ejercicio 26 - Conversor romano (n<=3999)
def a_romano(n):
    valores=[(1000,'M'),(900,'CM'),(500,'D'),(400,'CD'),
             (100,'C'),(90,'XC'),(50,'L'),(40,'XL'),
             (10,'X'),(9,'IX'),(5,'V'),(4,'IV'),(1,'I')]
    res=''
    for val,sim in valores:
        while n>=val:
            res+=sim; n-=val
    return res
if __name__ == '__main__':
    print(a_romano(1994))
