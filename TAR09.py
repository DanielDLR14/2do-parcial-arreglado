#Escriba un programa que, mediante una función, dada una cadena de caracteres (sin espacios), muestre el primer caracter que no se repite.
# Ejemplo:
# Ingrese una cadena de caracteres: aaabbbcdddefefef
# El primer caracter que no se repite es: 
# Pamela Sánchez 21-1727

# Uso una función para poder llamar el programa al examen.
def Principal2():

	
	
	def PrimerCaracterNoRepetido(Caracter):
		#Una lista vacia donde iran los caracteres
		ListaCaracteres = []
		#Un diccionario vacio donde se contaran los caracteres repetidos
		contador = {}

		# Uso el for para definir un bucle el cual se repite un número de veces se le asigne
		for aa in Caracter:
			if aa in contador:

				contador[aa] += 1
			# Si el caracter aparece una vez pues solamente  se dirigira al siguiente caracter
			else:
				contador[aa] = 1

				ListaCaracteres.append(aa)
			# Se estable que solamente imprimira el caracter que haya aparecido 1 vez
		for aa in ListaCaracteres:
			# Si en el contador aparece 1 sola aparicion de un caracter pues este lo mostrara
			if contador[aa] == 1:
				# devuelve el caracter no repetido
				return aa
		return None

	print("El caracter que no se repite es: ",PrimerCaracterNoRepetido('thisisit'))

	PrimerCaracterNoRepetido('thisisit')