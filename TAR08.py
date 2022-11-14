# Escriba un programa que, mediante una función, retorne las tablas de multiplicar del n al m.
# Ejemplo:
# Ingrese el número por el que comenzarán a mostrarse las tablas: 1
# Ingrese el número por el que terminarán a mostrarse las tablas: 3
# Pamela Sánchez 21-1727

# Uso una función para poder llamar el programa al examen.
def TablasMultiplicar():

# Declarar las variables y darle una entrada por teclado.
    while True:
        try:
            tablaInicio = int(input("Introduzca el numero por la tabla que quiere empezar: "))
            tablaFinal = int(input("Introduzca por cuál numero quiere que termine su tabla: "))

        
            print("\n")
            
            # Le doy valor a cada variable que creo.
            validation = 0
            acumulador = 1
            tablaMedio = 0
            # Se pone este while y su función es ejecutar hasta que sea verdadero, y en las demás líneas puse condiciones para que cumpla con cada función.
            while validation <= tablaFinal:
                if tablaMedio == 0:
                    print("\nTabla del: ", tablaInicio)
                    for cifras in range(0,11):
                        resultado = tablaInicio*cifras
                        print(tablaInicio,"x", cifras, "=", resultado)
                    tablaMedio = 1
                    continue
                elif tablaMedio==1:
                    while validation <= tablaFinal:
                        print("\nTabla del: ", tablaInicio+acumulador)
                        for cifras in range(0,11):
                                resultado = cifras*(tablaInicio+acumulador)
                                print(tablaInicio+acumulador,"x",cifras, "=", resultado)
                        acumulador += 1
                        validation = tablaInicio + acumulador
            break
        except ValueError:  
            print("Los datos que ha digitado no son números")
        