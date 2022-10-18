#Funciones definidas por el usuario

def imprimirHola(nombre:str, apellido:str):
    print("Hola", nombre, apellido)
    
imprimirHola("Juan", "Zamora")

#Función que reciba dos números enteros y muestre por pantalla
def imprimirSuma(num1:int, num2:int):
    print ("Su suma es", num1+num2)
    return num1+num2
suma= imprimirSuma(2,3)
print("La suma es:", suma)