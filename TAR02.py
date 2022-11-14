# Escribir un programa que pida 2 números y muestre paso a paso el cálculo de la raíz cuadrada 
# de la suma del cuadrado de ambos.
# daniel arturo 21-1799


# primero importamos la libreria math
import math

# Uso una función para poder llamar el programa al examen.
def EntradaTeclado():

    # Hago el uso de while true para que el programa se ejecute mientras sea verdadero.
    while True:
        # Uso el try que repetira el proceso de input hasta que ponga el dato correcto, se repetira por el while true
        try:

            # Declaro dos variables con entrada por teclado para que el usuario pueda digitar y mas abajo hice cuatro print.
            VarNum1 = int(input("\nInserte un numero deseado: "))
            VarNum2 = int(input("\nInserte otro numero deseado: "))
            NumExponente1 = VarNum1**2
            NumExponente2 = VarNum2**2
            ExponenteSuma = NumExponente1+NumExponente2
            print("El numero 1 su valor al cuadrado es: ", NumExponente1)
            print("El numero 2 su valor al cuadrado es: ", NumExponente2)
            print("La suma tiene como resultado: ", ExponenteSuma)
            print(f"\nLa raiz cuadrada del numero {ExponenteSuma} es: ", math.sqrt(ExponenteSuma))
            break
        # Aquí hago el uso de except para que lance el error, mediante un print
        except ValueError:
            print("\nEl dato que inserto no es un número.")
            

    


    