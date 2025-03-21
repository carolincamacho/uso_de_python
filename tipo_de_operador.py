'''
Operadores aritmeticos
20 marzo
'''
# # operador suma
# print(2+6)

# #operador resta
# # print(8-4)

# # #operador multiplicacion
x=4
y=6
# # print(x*y)

# #operador division
# z=12/4
# print (z)
# print (type(z)) #el resultado de a division siempre es flotante (decimales)

# #operador division piso
# print (10/3)    #division tradicional
# print (10//3)   #division piso: nos devuelve el entero mas proximo hacia abajo
# print (14.5/5)

# #operador modulo
# print (20/3)
# print(20%3) # operador para generar el residuo de una division

# print (8//-3)   #tener en cuenta el negativo para redondear.
# print (8/-3)

# #operador potencia
# print (x**2)

'''operadores de comparación
Este tipo de operadores los usamos cuando deseamos comparar expresiones o variables. 
Python evalúa si se cumple la comparación y nos devuelve (retorna) un valor True o False
'''

# #es igual a
# print("enca"=="Enca")
# print(8==8)
# print(3==3)
# print(3==3.000000000000000000000000001)
# print(3==3.000000000000001)

#es diferente de
# print("palabra"!="Palabra")
# print("palabra"!="palabra")

'''operadores de asignacion'''

#asignaciond e igualdad o defnicion
w=5

# #incremento
# saldo=100
# #saldo=saldo+1
# saldo+=8
# print(saldo)

# #decremento
# saldo_b=200
# #saldo=saldo+1
# saldo_b-=8
# print(saldo_b)

'''operadores logicos
and: comprueba si todas las condiciones se cumplen, true, false de los contrario
or: comprueba si alguna de las condiciones se cumple, true, false de lo contrario
not: negar el estado de una variable
'''
# print(x==4 and y==6)
# print(x==5 or y==8)

usuario_logueado=True
click_logout=True
print(not usuario_logueado)
