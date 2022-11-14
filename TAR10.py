#Escriba un programa que, mediante el uso de funciones realice lo siguiente:

#Dado un número entero, realice la suma de sus dígitos.
#Con el resultado de la suma, realizar lo siguiente:
#Generar los números del 1 al s (suma), y a su vez hacer las siguientes condiciones:
#Si el número es divisor de 3, mostrar el número y la palabra "Fizz".
#Si el número es divisor de 5, mostrar el número y la palabra "Buzz".
#Si el número es divisor de 3 y 5 (ambos), mostrar el número y la palabra "FizzBuzz".
#Si el número no es divisor de ninguno (3 y 5), únicamente mostrar el número.

# Daniel Arturo De La Rosa 21-1799

def JuegoFizzBuzzOriginal():
    
    while True:
        try:

    
            # Se nombra varias variables en donde indicara el comienzo que es 0
            NumSuma, extNum = 0, 0
            # Se aplica una variable en donde ira almacenado el numero que deseemos usar
            numEntero = int(input("Ingrese un numero entero: "))
            # Asignamos un while en donde iran los distontos procedimientos
            while numEntero != 0:
                # una variable en se aplicara un modulo
                extNum = numEntero % 10
                # una variable en donde se aplicara division
                numEntero //= 10
                # variable en donde hara suma de los procesos anteriores
                NumSuma += extNum
                
        except ValueError:
            print("El valor que introdujo no es un numero.")
    # un print en donde se imprimira las suma de los digitos que vayamos a usar
            print("La suma de los digitos es: {}".format(NumSuma))
                
            

    
    # Hago el uso de una función para poder llanarla y que aparezca en pantalla.
        def JuegoFizzBuzz():
        # se aplica un for con otra variable en almacenara la variable de los digitos que usemos
            for VarOracion in range(1, NumSuma+1):
            # un if donde dira que si es divisible entre 3 o 5 imprimira fizzbuzz
                if VarOracion% 3 == 0 and VarOracion % 5 == 0:
                    print(VarOracion)
                    print("fizzbuzz")
                    continue
            # un elif donde si solo es divisible entre 3 pues pondra fizz
                elif VarOracion % 3 == 0:
                    print(VarOracion)
                    print("fizz")
                    continue
            # un elif en donde si solo es divisible entre 5 pues pondra buzz
                elif VarOracion % 5 == 0:
                    print(VarOracion)
                    print("buzz")
                    continue
            # ya finalmente pues si imprime la variable donde aplica todo el proceso    
                else:
                    print(VarOracion)
        JuegoFizzBuzz()