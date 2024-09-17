# Función para sumar
def sumar(a, b):
    return a + b

# Función para restar
def restar(a, b):
    return a - b

# Función para multiplicar
def multiplicar(a, b):
    return a * b

# Función para dividir
def dividir(a, b):
    if b == 0:
        return "Error: No se puede dividir por cero"
    return a / b

# Función para potencia
def potencia(a, b):
    return a ** b

# Función principal de la calculadora
def calculadora():
    print("Bienvenido a la calculadora en Python")
    print("Selecciona una operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Potencia")

    # Leer la opción del usuario
    opcion = input("Elige una opción (1/2/3/4/5): ")

    if opcion in ['1', '2', '3', '4', '5']:
        # Leer los números
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))

        # Realizar la operación
        if opcion == '1':
            print(f"El resultado de la suma es: {sumar(num1, num2)}")
        elif opcion == '2':
            print(f"El resultado de la resta es: {restar(num1, num2)}")
        elif opcion == '3':
            print(f"El resultado de la multiplicación es: {multiplicar(num1, num2)}")
        elif opcion == '4':
            print(f"El resultado de la división es: {dividir(num1, num2)}")
        elif opcion == '5':
            print(f"El resultado de la potencia es: {potencia(num1, num2)}")
    else:
        print("Opción no válida")

# Ejecutar la calculadora
calculadora()
