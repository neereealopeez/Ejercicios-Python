#Sentencias Condicionales

if (5==4):
    print("Verdadero")
else:
    print("Falso")
    
#Primer Ejercicio: Programa que lea tu edad por teclado e imprima por pantalla si eres mayor de edad o no.
edad=0
edad = (int)(input("Dime tu edad "))
#Input siempre devuelve str (poner delante int si queremos enteros o reales)
if (edad>=18) :
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")