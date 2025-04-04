x= 344
y=34

'''
condicionales if elif else
if then else

if <condicion>:
    operacion 1
    operacion 2

'''
#caso 1  if
# if x > y:
#     print (" x es mayor a y")

#caso 2  if  - - else
# if x<y:
#     print ("x es menor que y")
# else:
#     print("x es mayor que y")


# #caso 3 if  elif  else
# if x<y:  # condiciones
#      print ("x es menor que y")
# elif x==y:  # condiciones
#      print("x es igual y")
# elif x/8==8:  #condiciones
#      print("x dividio en y igual a 8")
# else: # de lo contrario
#      print("x es mayor que y")


# #variante 1
# if x%2==0 and x>500:
#     print ("x es par y mayor que 500")  #multiples condiciones


# #caso de uso login a una aplicacion
# usuario=input("por favor ingrese su usuario: ")
# password=input("por favor ingrese su password: ")

# if usuario=="carolina" and password=="1234":
#      print ("usuario puede ingresar")
# else: # de lo contrario
#      print("usuario o contraseña incorrecto")


#caso de uso login a una aplicacion otro caso
usuario=input("por favor ingrese su usuario: ")

if usuario=="carolina":
     password=input("por favor ingrese su password: ")
     if password == "1234":
        print ("usuario puede ingresar")
     else: # de lo contrario
        print("contraseña incorrecto")
else:
    print("usuario incorrecto")

print ("ejecucion terminada")