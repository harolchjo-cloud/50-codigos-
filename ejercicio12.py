# Ejercicio 12 - Conversión de grados (Celsius-Fahrenheit)
def c_a_f(c): return c*9/5+32
def f_a_c(f): return (f-32)*5/9
if __name__ == '__main__':
    print('0C =', c_a_f(0),'F')
    print('32F =', f_a_c(32),'C')
