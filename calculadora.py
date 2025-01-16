
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División por cero no permitida."


def calculadora():
    print("Selecciona una operación:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")

    operacion = input("Ingresa el número de la operación 1/2/3/4: ")

    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))

    if operacion == '1':
        print(f"El resultado es: {sumar(num1, num2)}")
    elif operacion == '2':
        print(f"El resultado es: {restar(num1, num2)}")
    elif operacion == '3':
        print(f"El resultado es: {multiplicar(num1, num2)}")
    elif operacion == '4':
        print(f"El resultado es: {dividir(num1, num2)}")
    else:
        print("Operación no válida.")


calculadora()
