'''
Opción 1:
Lista para nombres
Lista para números de teléfono

Opción 2:
Lista para nombres y teléfonos
Ej: (Juan - Teléfono, Pepe - Teléfono)

'''
vNombres = []
vTeléfonos= []



#Creamos un menú para una agenda
'''
1 - Insertar contacto
2 - Borrar contacto
3 - Buscar contacto
4 - Ver todos los contactos
5- Salir
'''
#Función que pinta el menú y devuelve la opción seleccionada del 1 al 5
def pintaMenu():
    opc=0
    while (opc<1 or opc>5):
        print("****MENÚ INICIAL****")
        print("1 - Insertar contacto")
        print("2 - Borrar contacto")
        print("3 - Buscar contacto")
        print("4 - Ver todos los contactos")
        print("5 - Salir")
        print("********************")

        try:
            opc= int(input("Selecciona un número "))
        except:
            print("Las opciones son del 1 al 5")
    return opc

opc= pintaMenu()
while (opc!=5):
    opc(pintaMenu)