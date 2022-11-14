# Escriba un programa que calcule el precio a pagar por el suministro de energía eléctrica.
# Se debe preguntar la cantidad de kwh consumidos y el tipo de instalación: R para residencias, 
# I para industrias y C para comercios. Calcule el precio a pagar de acuerdo con la siguiente tabla.
# Daniel Arturo De La Rosa 21-1799


# Hago el uso de def para poder llamar la función en el examen.
def PrecioEnergia():

    # Uso el while y este se estará repitiendo hasta que sea verdadero.
    while True:

        # Uso el try que repetira el proceso de input hasta que ponga el dato correcto, se repetira por el while true.
        try:
            Residencial = "R"

            Comercial = "C"

            Instalacion = "I"
            # Declaro las variables que voy a utilizar, con entradas por teclado para que el usuario escriba lo que se le pida.
            tipoinstalacion = input("Introduzca el tipo de instalación: ")
            kwhconsumido = float(input("Cantidad de kwh a consumido: "))
            # Hago el uso de las condiciones y cuando el usario digite la letra que desee y luego pondra el costo, le lanzara cuanto debe pagar.
            if tipoinstalacion == 'R':
                if kwhconsumido <= 500:
                    precio = 550
                else:
                    precio = 850

            elif tipoinstalacion == 'C':
                if kwhconsumido <= 1000:
                    precio = 1300
                else:
                    precio = 2500

            elif tipoinstalacion == 'I':
                if kwhconsumido <= 5000:
                    precio = 3800

                else:
                    precio = 4200

            if precio:
                print("Precio = ", precio)
            break

         # Aquí hago el uso de except para que lance el error, mediante un print
        except ValueError:
             print("\nEl dato que introdujo no es un número.")
   
        # Hago un print con los tipos de luz que hay 
        print("""
    Residencial = "R"

    Comercial = "C"

    Instalación = "I"
    """)
        
       