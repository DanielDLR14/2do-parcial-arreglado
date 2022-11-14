# Escriba un programa que pregunte al usuario los números de su ticket de lotería, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor
# Daniel Arturo De La Rosa 21-1799

# Hago el uso de def para poder llamar la función en el examen.
def NumeroLoteria():

    # Uso el while y este se estará repitiendo hasta que sea verdadero.
    while True:
        # Uso el try que repetira el proceso de input hasta que ponga el dato correcto, se repetira por el while true.
        try:
            # Creo la lista que voy  a utilizar
            NumeroGanador = []

            # Hago el uso del for con un range que se itere las veces que yo quiera y dentro del parentesís le pongo el rango de veces que quiero que se repita.
            for i in range(6):

                # Declaro una variable con una entrada por teclado para que el usuario digite el número.
                NumeroGanador.append(int(input("Introduce un número ganador: ")))

            NumeroGanador.sort()
            
            # Hago el print con los numeros ganadores
            print("Los números ganadores son " + str(NumeroGanador))
            break

        # Aquí hago el uso de except para que lance el error, mediante un print
        except ValueError:
            print("Los datoss que ha introducido no son numeros.")
            
            