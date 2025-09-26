# Ejercicio 03 - Cuenta de banco básica (encapsulamiento)
class CuentaBanco:
    def __init__(self, saldo=0):
        self.__saldo = saldo
    def depositar(self, monto):
        if monto>0: self.__saldo += monto
    def retirar(self, monto):
        if 0<monto<=self.__saldo: self.__saldo -= monto
        else: print('Fondos insuficientes')
    def saldo(self): return self.__saldo
if __name__ == '__main__':
    c = CuentaBanco(100)
    c.depositar(50)
    c.retirar(30)
    print('Saldo:', c.saldo())
