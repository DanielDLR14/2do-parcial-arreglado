# Realizar un programa el cual determine el tiempo en meses para pagar un préstamo.
# Indicaciones:
# El monto del préstamo debe ser solicitado.
# Se debe solicitar la cantidad mensual que se desea pagar.
# Mediante el uso de while, determinar los meses (total) en los que se completará el pago del préstamo.

# Daniel De La Rosa 21-1799

# Hago el uso de def para poder llamar la función en el examen.
def PréstamosPago():
    # Uso el while y este se estará repitiendo hasta que sea verdadero.
    while True:
        
        # Uso el try que repetira el proceso de input hasta que ponga el dato correcto, se repetira por el while true.
        try:
            # Asignamos una variable donde se introducira la cantidad que deseemos tomar como prestamo
            MesesPrestamo = 12
            PrestamoMonto = float(input("¿De cuanto desea tomar su prestamo? "))
                

            print("Su préstamo tomado es de: $", PrestamoMonto)

                # Aignamos otra variable en donde estara almacenada la cantidad que deseemos pagar el prestamo
            CantidadMensual = float(input("¿Que cantidad desea pagar?: "))
            print(f"Mensual usted pagará {CantidadMensual} pesos dominicanos.")
                
                # Usamos un ciclo while en donde se calculara el monto del prestamo
            while PrestamoMonto >= 1:
                # Finalmente nos dara un print con los calculos totales y en donde se vera la cantidad de meses en que tomara poder pagar
                print(f"El total de meses que usted completara el pago es de {PrestamoMonto/CantidadMensual:.0f} meses")
                
                
                # Uso el break para que cuando llegue aqui se pare 
                
                
        # Aquí hago el uso de except para que lance el error, mediante un print
        except ValueError:
            print("Los datos que ha introducido no son números.")
            
    