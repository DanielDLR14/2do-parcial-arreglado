#Escriba un programa con funciones definidas por usted, que realice lo siguiente:
#Almacene una lista de 10 tuplas que correspondan a los siguientes viajeros de un aeropuerto. Nota: La estructura 
# de los datos de cada viajero es Nombre, Edad, Destino:
#Juan, 30, Madrid.
#Fernanda, 42, Portugal.
#Raúl, 28, Brazil.
#Julio, 32, Venezuela.
#Mateo, 26, Argentina.
#María, 32, Portugal.
#José, 29, Madrid.
#Marcos, 29, Venezuela.
#Juana, 41, Venezuela.
#Paulina, 35, Madrid.
#Muestre los destinos almacenados (sin repetir).
#Devuelva una lista de diccionarios de los pasajeros cuyo destino sea el solicitado por teclado.
#Si se coloca un destino que no se encuentra en los almacenados, el programa debe mostrar un mensaje diciendo:
#"No hay pasajeros para este destino".

# Pamela Sánchez 21-1727 

# Hago una función para poder la lista de viajeros, antes de creando una lista para que se almacene ahí.
def Principal():
    print("========================= Viajeros con Destinos Diferentes =========================""\n")
    TuplasLista = [
        ('Juan', 30, 'Madrid'),
        ('Fernanda', 42, 'Portugal'),
        ('Raúl', 28, 'Brazil'),
        ('Julio', 32, 'Venezuela'),
        ('Mateo', 26, 'Argentina'),
        ('María', 32, 'Portugal'),
        ('José', 29, 'Madrid'),
        ('Marcos', 29, 'Venezuela'),
        ('Juana', 41, 'Venezuela'),
        ('Paulina', 35, 'Madrid')
    ]

    # Creo una variable y la pongo en forma de lista para almacenar los destinos.
    destinos=["Madrid","Portugal", "Brazil", "Venezuela", "Argentina", "Portugal", "Madrid", "Venezuela", "Venezuela", "Madrid"]

    # Creo una lista para que la información vaya a donde tiene que ir y se guarde en forma de lista
    Dec = []
    
    # Hago una función para poner los destinos y convertirlos en set
    def OrdenarDestinos():
        Destinatarios = set(destinos)
        print("Los destinos son: ",Destinatarios, "\n")

    def DestinoDeLosPasajerosABuscar(l):
        acumulador = 0
        # Por ultimo hago un for y dentro de ese for ponga la condicion if para que si se cumple imprima lo que se pide y de lo contrario imprimiria no hay destinos asi alla.
        if l in destinos:
            for x in TuplasLista:
                if x[2] == l:
                    Dec.append({"Nombre": x[0], "Edad": x[1], "Destino": x[2]})
                    Diccionario = Dec[acumulador]
                    print(Diccionario)
                    
                    acumulador += 1

        else:
            print("No hay pasajeros para este destino." "\n")

    
    OrdenarDestinos()
    DestinoDeLosPasajerosABuscar(input("Buscar pasajeros con destino a: "))
    print("========================= Fin del programa =========================")
