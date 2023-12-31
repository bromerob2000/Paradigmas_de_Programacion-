#================
#Uso de filtros
#================

#===========================================
#Hacer una lista de los numeros 
#por arriba del promedio
#===========================================

# Módulo de estadística
import statistics

bigdata= [1.2,2.7,0.8,4.1,4.3,-0.1]
promedio = statistics.mean(bigdata)
print(promedio)

#===========================================
# Hazme una lista de lementos que cumplan
# la condición x > promedio
#
# filter( condición, datos )
#===========================================

print(list(filter(lambda x: x > promedio, bigdata)))

#===================
# Limpiar los datos
#===================

paises = ["", " Argentina", "", "Brasil", "", "Chile", "México", "", "Colombia", "", "", "Cuba", 
        "Venezuela"]


#=======================
# Filtra los que no 
# contiene nada
#=======================
print(list(filter(None, paises)))
