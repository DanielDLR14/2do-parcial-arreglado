#Escriba una función que reciba 2 listas de productos (de forma dinámica), y retorne un conjunto (Set) de los productos comunes en las mismas. En caso de que no hayan productos comunes, retornar:
#  "No hay productos comunes en las listas".

# Pamela Sánchez 21-1727


# Hago un llamado con def para poder importarlo en el examen.
def ListasProductos():
    # Hago dos variable y las declaro como lista para que se almacenen la información que va en cada una.
    listaproductos = []
    listaproductos2 = []
    

    # Creo una función para que salga al final en la terminal.
    def Listas(j):

        
                # Declaro tres variables y le doy un valor a cada una.
                acumulador = "Empezar"
                acumuladorNumero = 0
                acumuladorNumero2 = 0
                

                # Uso el while y mientras se cumpla esa función se estará ejecuntando, al igual que la condición if
                while acumulador != "Fin":
                    
                    if acumulador == "Empezar":
                        acumulador = "Continuar"
                        
                        # Luego hago un print con la lista de productos
                        print("\nLista de productos\n")
                        for x in range(1, j+1):
                            Prod = input("Producto: ")
                            listaproductos.append(Prod)

                        # Hago el uso de len que se utiliza para la longitud de la lista de productos
                        print("\nProductos contados en lista: ", len(listaproductos))
                        for producto in listaproductos:
                            print("Producto: ", listaproductos[acumuladorNumero])
                            acumuladorNumero += 1
                        print("Lista: ", listaproductos)
                        
                        continue
                    # Uso un elif para que si el acumulador es igual a continuar se ejecutara una entrada por teclado.
                    elif acumulador == "Continuar":
                        prodCantidad = int(input("\nIngrese cantidad producto lista 2: "))
                        
                        # Uso el while y mientras se cumpla esa función se estará ejecuntando
                        while prodCantidad  != acumuladorNumero2:
                            print("\nLista de productos 2\n")
                            for x in range(1, prodCantidad+1):
                                Prod = input("Producto: ")
                                listaproductos2.append(Prod)


                            print("\nProductos contados en lista: ", len(listaproductos2))
                            for producto in listaproductos2:
                                print("Producto: ", listaproductos2[acumuladorNumero2])
                                acumuladorNumero2 += 1
                            print("Lista: ", listaproductos2)
                            acumulador == "Fin"
                            break
                        
            

    def prodcomunes(x, y):
        
        listaproductos_set = set(x)
        listaproductos2_set = set(y)
        
        ProductosComunes = listaproductos_set.intersection(listaproductos2_set)
        
        if len(ProductosComunes) == 0:
            print("\nNo hay productos comunes en las listas.")
        elif len(ProductosComunes) >= 1:
            print("Comunes en lista 1 y lista 2: ", ProductosComunes)
        
        
    
    Listas(int(input("Cantidad producto lista 1: ")))
    prodcomunes(listaproductos, listaproductos2)