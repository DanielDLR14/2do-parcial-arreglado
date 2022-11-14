#Escriba un programa que permita crear una lista de palabras y que, a continuación,
#pida una palabra y diga cuántas veces aparece esa palabra en la lista.
#Ps21-1727 Pamela Sanchez

# Uso una función para poder llamar el programa al examen.
def listac():
    # Hago el uso de while true para que el programa se ejecute mientras sea verdadero.
    
        # Uso el try que repetira el proceso de input hasta que ponga el dato correcto, se repetira por el while true
        
            #se declara la variable lista, tipo lista
        
            lista = [] 

        #se crea la funcion for y se pone en parentesis del range las veces que quiero que de vuelta 
            for i in range(5): 
                
                lista.append(input("Escriba una palabra: "))
            
        #luego se imprime la lista
            print(lista)

        #se declara la variable y luego se pone una entrada por teclado para que el usuario busque la palabra
            palabra_a_buscar=(input("Escribe la palabra a buscar en la lista: "))

        #la funcion del count es contar cuantas veces aparece la palabra
            veces_que_aparece= lista.count(palabra_a_buscar)

        #por ultimo se izmprime la palabra repetida
            print("La palabra:",palabra_a_buscar,"aparece",veces_que_aparece, "veces en la lista.")
            
        # Aquí hacemos el uso de except KeyError para controlar la data basura
        