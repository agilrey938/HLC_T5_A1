def suma(a, b):
    return a + b

def calculadora():
    a = int(input("Introduce el primer valor: "))
    b = int(input("Introduce el segundo valor: "))
    resultado = suma(a, b)
    print("La suma de", a, "y", b, "es", resultado)
calculadora()