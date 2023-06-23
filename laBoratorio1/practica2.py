#=================================================
# Input permite obtener datos del usuario 
#    en prompter 
#=================================================
nombre = input("Dame tu nombre:   " )
print("Hola como estás", nombre)

#=================================================
# Los enteros son de precisión limitada
#=================================================
y = 5000000000000000000000000000000000
print(y)

#=================================================
# Se puede delimitar números con guión bajo pero
#    pero no con coma
#=================================================
Y = 5_000_000
print(y)

#=================================================
# La función int() cambia string y floats a 
# enteros
#=================================================
numero = int(input("Dame tu edad:  "))
type(numero)

#=================================================
# La notación cinetífica de flotantes utiliza 
#                e o E
#=================================================
#1.2 x 10^{-9}
#=================================================
y = 1.2E-09
print(y)

#=================================================
# Los complejos se escriben con la raiz de menos 
# uno.
# i siempre con un número como prefijo.
# No acepta la j suelta
#=================================================
z = 1+1j

# suma
# resta
# multiplicación
# división
# módulo %
# exponente**
# // función piso
# Funciones para transformar números int() float () complex()
# Operaciones abs() round()  pow()

print(round(3.14159,4))


#=================================================
# String de varias lineas
#=================================================
parrafo = """ En el bosque de la china
la chinita se perdió """
print(parrafo)

#=================================================
# La función len() obtiene el tamaño del string
#=================================================
n= len(parrafo)
print(n)

#=================================================
# Las letrasen un string ocupan lugares como en un
# arreglo.
# (También de atrás para adelante comenzando en 
#          -1 el último)
#=================================================
palabra = "hola"
print(palabra[0])
print(palabra[-4])

