#Listas en Python
#Definición e Inicialización
vNombres= []

#Insertar un dato
vNombres.insert(0, "Juan")
vNombres.insert(1, "Pepe")
vNombres.insert(2, "Inés")
vNombres.append("Minerva") #Inserta en última posición, sin tener que asignar un número de posición
vNombres.insert(1, "Julián") #No se sobreescriben los elementos, solamente se desplazan.

#Eliminar elementos.
#vNombres.clear()
vNombres.remove("Pepe")
#NombreBorrado = vNombres.pop(1) "Arranca" el nombre de la lista
print("El nombre borrado es", vNombres.pop(1))

#Ordenar una lista
vNombres.sort(reverse=True) #Para ordenar de mayor a menor.

#Contar el ńumero de elementos de una lista.
print(vNombres.count("Inés")) #Cuenta el número de veces que sale un elemento en una lista.
print("La lista tiene", len(vNombres))
print(vNombres)
