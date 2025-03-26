"TIPOS DE DATOS"
"strings: cadenas de texto <class 'str'>"
""

# dato="Enca24"
# dato_2='Enca24'

# print(type(dato))
# print(type(dato_2))

# #concatenacion
# texto_1="programa "
# texto_2="Desarrollador junior"

# enunciado=texto_1+texto_2
# print(enunciado)

# #indexacion de string
# #indexar se refiere a acceder un elemento de una cadena enuna posicion
nombre="Carolina Camacho"
# print(nombre[0])
# print(nombre[4])
# print(nombre[-1])   #para ver la ultima posición
# print(nombre[-3])

# #slicing de cadenas - porciond euna cadena
# print(nombre[:])
# print(nombre[0:3]) #muestra las posiciones de la 0 a la 2
# print(nombre[0:-5]) #muestras las posiciones de la 0 hasta la que este antes de la 5 posicion

# "TIPOS DE DATOS NUMERICOS"
# "<class <'float'>"

# x=5
# print (type(x))
# print
# y=5.0
# print (type(y))

# asistencia =True
# print (type(asistencia))
# print(not asistencia)

# #TIPOS ESCTRUCTURAS
# 'sets: se define con {}'
# '"tuplas: se define con ()'
# '"listas: se define con []'
# #diccionario: se define con {'clave':'valor','clave_2:'valor_2',,}"'

# #sets o conjuntos
# 'se utiliza para alamacenar ifnormacion cuando no interesa el orden ni la posicion'
# 'no permite valores duplicados'
conjunto_1= {'a','b','c'}
conjunto_2= {'d','e','f'}

# print(type(conjunto_1))
# print(conjunto_1)

# #metodos de los conjuntos
# #los metodos indican las cosas que podemos hacer con los objetos.

# conjunto_1.add("h")
# print (conjunto_1)

# conjunto_2.remove("f")
# print (conjunto_2)

# #hace la union de varios objetos.
# conjunto_3=conjunto_1.union(conjunto_2)
# print(conjunto_3)

# #aplicar un metodo
# conjunto_2.update(conjunto_1)
# print(conjunto_2)

# conjunto_2.clear()
# print(conjunto_2)

# # 'tuplas
# # son estrucutras mas rigidas, son inmutables.'
# #almacenan diferentes tipos de datos.

tupla_1=(1,"a",True)
print(type(tupla_1))

print(tupla_1.count("a"))
print(tupla_1.index(1))

