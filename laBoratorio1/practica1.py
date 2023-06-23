'''
   ESTE ES UN SUPER COMENTARIO
   DE INICIO A NUESTRO RESUMEN
'''

#===========================
#Operaciones básicas
#===========================
print(2+3)
print(2*3)
print(2/3)
print(2**10)
print(2**0.5)   #Raiz cuadrada
print(10%2)
print(10%0.1)   #exclusivo de python 

#===========================
# Para saber el tipo de 
#objetos se usa type
#============================

t=0
print(type(t))  #entero
t=3.6
print(type(t))  #real (flotante)
t=True
print(type(t))  # booleano (bool)


#===========================
#Mensajes en pantalla
#===========================
print("Este es un comnado de python. " , "Este es otro enunciado.", t)
print('id : ',1)
print('Firs Name:  ', 'Steve')
print('Last Name: ', 'Jobs')
print("Vamos a sumar esto" + " con esto otro")

#==============================
#Continuar una instrucción en 
# varios renglones.
#==============================
if 100>99 and \
        200 <= 300 and \
        True != False:
            print('Hello World!')

#==============================
# Comandos diferentes en la 
# misma linea
#==============================

print(" Hola "); print("tu!!")     #Se considera mala practica

#==============================
# Usando paréntesis redondos,
# cuadrados o llaves se puede
# escribir en varios renglones.
#==============================

list = [1,2,3,4,
        5,6,7,8,
        9,10,11,12]
matriz = [ [1,2,3,4],[5,6,7,8],[9,10,11,12] ]

print(list)
print(matriz)

#=============================
# Identificación estricta para 
# procesos dependientes de :
#   (dos puntos)
#=============================

if 10>5:
    print(" Diez es mayor a cinco. ")
    print(" Otra indetanción ")
    for i in list:
        print(i)
        print(" Ok ")
        if 10>5:
            print(" Verdadero ")
            if 10<20:
               print(" Verdadero ")
        elif 5>3: # Comienza segundo condicional.
            print(" Esto no se imprimira ")
        else:
            print(" Aquí nunca llega ")
        #======================
        #      Funciones
        #======================
        def say_hello(name):
            print("Hello ", name)
            print("Welcome to python Tutorials")

