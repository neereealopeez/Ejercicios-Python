#Bucle #While
'''
i=0
bandera=True
while (bandera==True):
    print("No hagas esto nunca", i)
    i=i+1
    if(i==30000):
        bandera=False
'''

'''
i=0
num=0
num= (int)(input("Dime un número "))
bandera=True
while (i <=10):
    print(num, " * ", i, " = ", num*i)
    i=i + 1
'''

palabrasecreta= "albondigas"

palabrasecreta= input("Dime una palabra: ")

if(palabrasecreta!= "albondigas"):
   while(palabrasecreta!= "albondigas"):
    print("Contraseña incorrecta. Pruebe de nuevo.")
    palabrasecreta= input("Dime una palabra ")
else:
    if(palabrasecreta="albondigas"):
        print("Contraseña correcta. Felicidades")