# Escribir un programa que capture una lista de caracteres.

# Indicaciones:

# La longitud de la lista debe ser dinámica (capturada).
# Si el usuario ingresa un dígito (cualquiera), se debe terminar la ejecución del programa con el mensaje: "Lo sentimos, no se permiten dígitos.", y mostrar la lista con los caracteres que se lograron capturar (en caso de que se hayan capturado).
# Si el usuario ingresa una palabra, se debe de omitir y continuar con el bucle.
# Mostra la lista con los caracteres capturados y el total.

# Daniel Arturo De La Rosa 21-1799
def ListaCaracteres():
     
        
        lista1 = []

        
        CantCaracteres = int(input("Introduzca el limite e caracteres: "))
        print("Introduce solamente numeros") 
        CantCaracteres = int(input("Introduzca el limite e caracteres: "))

        while len(lista1)!= CantCaracteres:
            Caracteres = input("Ingrese el caracter: ")
            if Caracteres  == "0" or Caracteres == "1" or Caracteres ==   "2" or Caracteres ==   "3" or Caracteres ==   "4" or Caracteres ==   "5" or Caracteres ==   "6" or Caracteres ==   "7" or Caracteres ==   "8" or Caracteres ==  "9":
                print("Lo sentimos, no se permiten dígitos.")
                break
            
            elif len(Caracteres) > 1:
                continue
            else:
                lista1.append(Caracteres)
                print(lista1)
                print(len(lista1))


