#Escribir un programa que mediante el uso de variables y operadores aritméticos, almacene la suma, resta, multiplicación y división de 2 números. 
# Luego, mostrar los resultados.
# Pamela Sánchez 21-1727

# Uso una función para poder llamar el programa al examen.
def OperadoresAritmeticos():
    # Declaro una variable y le asigno un valor para que cuando se muestre en pantalla aparezcan, al igual que con las demás
    num1 = 20
    print("1er número dado: ",num1)

    num2 = 10
    print("2do número dado: ",num2)
    
    suma = num1+num2
    print("\nLa suma de los números dados es: ",suma)

    resta = num1-num2
    print("La resta de los números dados es: ",resta)

    multiplicacion = num1*num2
    print("La multiplicación de los números dados es: ",multiplicacion)

    division = num1//num2
    print("La división de los números dados es: ",division)