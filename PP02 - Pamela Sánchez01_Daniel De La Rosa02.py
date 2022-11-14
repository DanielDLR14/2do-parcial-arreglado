# 2do Parcial - Ejercicio
# Valor: 70ptos.
# Realizar un programa que permita la ejecución de todos los ejercicios que se han hecho hasta el momento (TAR01 - TAR12).
# Indicaciones:
# 1- El programa debe tener un menú que permita seleccionar el ejercicio que se desea ejecutar.
# 2- Luego de seleccionar un ejercicio, además de su ejecución (entradas, y demás funcionalidades), se debe mostrar el enunciado del mismo.     (Esto debe aparecer arriba).
# 3- Se debe hacer uso de módulos: los ejercicios deben ser importados desde el programa principal.
# 4- Una vez terminada la ejecución de un ejercicio, el programa debe permitir volver al menú principal o terminar la ejecución de todo el programa.
# 5- El programa debe controlar la captura de data basura.
# 6- Recomendación: para aquellos ejercicios que no completaron correctamente y que tienen observaciones de mejora, favor de corregirlos para que se ejecuten 100% correctos.

# Pamela Sofía Sánchez Reyes ps21-1727.
# Daniel Arturo De La Rosa dd21-1799.

# Hicimos la importación de los ejercicios solicitado y luego cada uno de los ejercicios lo llamamos con la inicial T y el número del ejercicio que toca.
import TAR01 as T1
import TAR02 as T2
import TAR03 as T3
import TAR04 as T4
import TAR05 as T5
import TAR06 as T6
import TAR07 as T7
import TAR08 as T8
import TAR09 as T9
import TAR10 as T10
import TAR11 as T11
import TAR12 as T12


# Hicimos el primer print, para cuando se ejecute el programa lo primero que salga sea una bienvenida al proyecto.
print("======================= O ======================\n| Bienvenidos a nuestro Segundo Parcial        |\n======================= O ======================\n")

# Aquí hicimos el uso de la función def para hacer el menú y lo decoramos a nuestro gusto, una vez de haber terminado llamamos la función con el nombre que le pusimos para que aparezca en pantalla.
def MenuEjercicios():

    print("\n======================= O ======================\n|                Menú de Tareas                |")
    print(
        "======================= O ======================\n|[1] TAR01 - Operaciones Basicas.              |")
    print(
        "======================= O ======================\n|[2] TAR02 - Entrada Por Teclado.              |")
    print(
        "======================= O ======================\n|[3] TAR03 - Precio De Energía Eléctrica.      |")
    print(
        "======================= O ======================\n|[4] TAR04 - Veces que se repite una palabra.  |")
    print(
        "======================= O ======================\n|[5] TAR05 - Números de lotería.               |")
    print(
        "======================= O ======================\n|[6] TAR06 - Préstamos usando while.           |")
    print(
        "======================= O ======================\n|[7] TAR07 - Lista de caracteres usando while. |")
    print(
        "======================= O ======================\n|[8] TAR08 - Tablas de multiplicar.            |")
    print(
        "======================= O ======================\n|[9] TAR09 - Primer caracter que no se repite. |")
    print(
        "======================= O ======================\n|[10] TAR10 -  Más Funciones.                  |")
    print(
        "======================= O ======================\n|[11] TAR011 - Sets a partir de Listas.        |")
    print(
        "======================= O ======================\n|[12] TAR012 - Los Viajeros.                   |")
    print(
        "======================= O ======================\n|[13]           Abrir Menú                     |")
    print(
        "======================= O ======================\n|[14]        Cerrar el Programa                |\n======================= O ======================\n")

# Aquí es donde llamamos la función cuando terminamos el menú.
MenuEjercicios()

# Usamos el bucle while y este se utiliza para hacer algo repetidamente, bajo unas condiciones específicas, hasta que sea verdadero.
while True:

# Declaramos una variable de tipo int y con una entrada por teclado, para que el usario digite el número del ejercicio que desea realizar en dicho programa.                      
    opcion = int(input("\nIntroduzca el ejercicio que desee: "))

    # Hicimos el uso de la condición if que está se ejecutará si el número digitado es igual a 1.
    if opcion == 1:

        # Hicimos un print, haciendo enfasis en el ejercicio que ha seleccionado el usario.
        print("=====================OO======================\n|Usted ha seleccionado el ejercicio número 1|\n=====================OO======================")
        # Este es otro print con el enunciado del ejercicio, para que el usuario sepa que hara a la hora de ejecutar.
        print("\nEscribir un programa que mediante el uso de variables y operadores aritméticos, almacene la suma, resta, multiplicación y división de 2 números. \nLuego, mostrar los resultados.\n")
        # Llamamos la función con el nombre asignado en el ejercicio solicitado, para que se presente en la terminal.
        T1.OperadoresAritmeticos()
        
         
    # Hicimos el uso de la condición else que está se ejecutará si el número digitado es igual a 2.
    elif opcion == 2:

        # Hicimos un print, haciendo enfasis en el ejercicio que ha seleccionado el usario.
        print("=====================OO======================\n|Usted ha seleccionado el ejercicio número 2|\n=====================OO======================")
        # Este es otro print con el enunciado del ejercicio, para que el usuario sepa que hara a la hora de ejecutar.
        print("\nEscribir un programa que pida 2 números y muestre paso a paso el cálculo de la raíz cuadrada de la suma del cuadrado de ambos.")
        # Llamamos la función con el nombre asignado en el ejercicio solicitado, para que se presente en la terminal.
        T2.EntradaTeclado()
         
    # Hicimos el uso de la condición else que está se ejecutará si el número digitado es igual a 3.
    elif opcion == 3:

        # Hicimos un print, haciendo enfasis en el ejercicio que ha seleccionado el usario.
        print("=====================OO======================\n|Usted ha seleccionado el ejercicio número 3|\n=====================OO======================")
        # Este es otro print con el enunciado del ejercicio, para que el usuario sepa que hara a la hora de ejecutar.
        print("\nEscriba un programa que calcule el precio a pagar por el suministro de energía eléctrica. Se debe preguntar la cantidad de kwh consumidos y el tipo de instalación: R para residencias, I para industrias y C para comercios.")
        # Llamamos la función con el nombre asignado en el ejercicio solicitado, para que se presente en la terminal.
        T3.PrecioEnergia()
         
    # Hicimos el uso de la condición else que está se ejecutará si el número digitado es igual a 4.
    elif opcion == 4:

        # Hicimos un print, haciendo enfasis en el ejercicio que ha seleccionado el usario.
        print("=====================OO======================\n|Usted ha seleccionado el ejercicio número 4|\n=====================OO======================")
        # Este es otro print con el enunciado del ejercicio, para que el usuario sepa que hara a la hora de ejecutar.
        print("\nEscriba un programa que permita crear una lista de palabras y que, a continuación, pida una palabra y diga cuántas veces aparece esa palabra en la lista.")
        # Llamamos la función con el nombre asignado en el ejercicio solicitado, para que se presente en la terminal.
        T4.listac()
         
    # Hicimos el uso de la condición else que está se ejecutará si el número digitado es igual a 5.
    elif opcion == 5:

        # Hicimos un print, haciendo enfasis en el ejercicio que ha seleccionado el usario.
        print("=====================OO======================\n|Usted ha seleccionado el ejercicio número 5|\n=====================OO======================")
        # Este es otro print con el enunciado del ejercicio, para que el usuario sepa que hara a la hora de ejecutar.
        print("\nEscriba un programa que pregunte al usuario los números de su ticket de lotería, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor. ")
        # Llamamos la función con el nombre asignado en el ejercicio solicitado, para que se presente en la terminal.
        T5.NumeroLoteria()
         
    # Hicimos el uso de la condición else que está se ejecutará si el número digitado es igual a 6.
    elif opcion == 6:
        # Hicimos un print, haciendo enfasis en el ejercicio que ha seleccionado el usario.
        print("=====================OO======================\n|Usted ha seleccionado el ejercicio número 6|\n=====================OO======================")
        # Este es otro print con el enunciado del ejercicio, para que el usuario sepa que hara a la hora de ejecutar.
        print("\nRealizar un programa el cual determine el tiempo en meses para pagar un préstamo.")
        # Llamamos la función con el nombre asignado en el ejercicio solicitado, para que se presente en la terminal.
        T6.PréstamosPago()
         
    # Hicimos el uso de la condición else que está se ejecutará si el número digitado es igual a 7.
    elif opcion == 7:

        # Hicimos un print, haciendo enfasis en el ejercicio que ha seleccionado el usario.
        print("=====================OO======================\n|Usted ha seleccionado el ejercicio número 7|\n=====================OO======================")
        # Este es otro print con el enunciado del ejercicio, para que el usuario sepa que hara a la hora de ejecutar.
        print("\n")
        # Llamamos la función con el nombre asignado en el ejercicio solicitado, para que se presente en la terminal.
        T7.ListaCaracteres()

    # Hicimos el uso de la condición else que está se ejecutará si el número digitado es igual a 8.
    elif opcion == 8:

        # Hicimos un print, haciendo enfasis en el ejercicio que ha seleccionado el usario.
        print("=====================OO======================\n|Usted ha seleccionado el ejercicio número 8|\n=====================OO======================")
        # Este es otro print con el enunciado del ejercicio, para que el usuario sepa que hara a la hora de ejecutar.
        print("\n")
        # Llamamos la función con el nombre asignado en el ejercicio solicitado, para que se presente en la terminal.
        T8.TablasMultiplicar()

    # Hicimos el uso de la condición else que está se ejecutará si el número digitado es igual a 9.
    elif opcion == 9:

        # Hicimos un print, haciendo enfasis en el ejercicio que ha seleccionado el usario.
        print("=====================OO======================\n|Usted ha seleccionado el ejercicio número 9|\n=====================OO======================")
        # Este es otro print con el enunciado del ejercicio, para que el usuario sepa que hara a la hora de ejecutar.
        print("\nEscriba un programa que, mediante una función, dada una cadena de caracteres (sin espacios), muestre el primer caracter que no se repite.")
        # Llamamos la función con el nombre asignado en el ejercicio solicitado, para que se presente en la terminal.
        T9.Principal2()
         
         
    # Hicimos el uso de la condición else que está se ejecutará si el número digitado es igual a 10.
    elif opcion == 10:

        # Hicimos un print, haciendo enfasis en el ejercicio que ha seleccionado el usario.
        print("======================OO======================\n|Usted ha seleccionado el ejercicio número 10|\n======================OO======================")
        # Este es otro print con el enunciado del ejercicio, para que el usuario sepa que hara a la hora de ejecutar.
        print("\nEscriba un programa que, mediante el uso de funciones realice lo siguiente: Dado un número entero, realice la suma de sus dígitos. \nCon el resultado de la suma, realizar lo siguiente: Generar los números del 1 al s (suma), y a su vez hacer las siguientes condiciones: Si el número es divisor de 3, mostrar el número y la palabra Fizz. Si el número es divisor de 5, mostrar el número y la palabra Buzz. \nSi el número es divisor de 3 y 5 (ambos), mostrar el número y la palabra FizzBuzz Si el número no es divisor de ninguno (3 y 5), únicamente mostrar el número.")
        # Llamamos la función con el nombre asignado en el ejercicio solicitado, para que se presente en la terminal.
        T10.JuegoFizzBuzzOriginal()

    # Hicimos el uso de la condición else que está se ejecutará si el número digitado es igual a 11.
    elif opcion == 11:

        # Hicimos un print, haciendo enfasis en el ejercicio que ha seleccionado el usario.
        print("======================OO======================\n|Usted ha seleccionado el ejercicio número 11|\n======================OO======================")
        # Este es otro print con el enunciado del ejercicio, para que el usuario sepa que hara a la hora de ejecutar.
        print("\n")
        # Llamamos la función con el nombre asignado en el ejercicio solicitado, para que se presente en la terminal.
        T11.ListasProductos()
         
    # Hicimos el uso de la condición else que está se ejecutará si el número digitado es igual a 12.
    elif opcion == 12:

        # Hicimos un print, haciendo enfasis en el ejercicio que ha seleccionado el usario.
        print("======================OO======================\n|Usted ha seleccionado el ejercicio número 12|\n======================OO======================")   
        # Este es otro print con el enunciado del ejercicio, para que el usuario sepa que hara a la hora de ejecutar.
        print("\n")
        # Llamamos la función con el nombre asignado en el ejercicio solicitado, para que se presente en la terminal.
        T12.Principal()
        
    # Hicimos el uso de la condición else que está se ejecutará si el número digitado es igual a 13 y este volverá a presentar el menú.
    elif opcion == 13:

        # Aquí llamamos la función para que aparezca el menú otra vez.
        MenuEjercicios()

    # Hicimos el uso de la condición else que está se ejecutará si el número digitado es igual a 14 y aquí se parara el programa.
    elif opcion == 14:

        # Cuando llegue aquí el programa se va a parar, porque el break es una sentencia que permite parar un bucle por completo en cuanto se da o deja de darse una condición externa.
        break

    # Por último usamos el else que esté se ejecutara cuando el usario digite un número que no esté en la lista
    else:
        print(
             
            "==================================== OO ===============================\n|El número seleccionado no aparece en la lista, favor introducir otro. :(\n|==================================== OO ===============================")
    




