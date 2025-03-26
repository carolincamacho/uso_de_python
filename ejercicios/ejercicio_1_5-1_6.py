'''
1.5
Escriba un programa que realice la comprobación de la división.
Recuerde:
Divisor * Cociente + Residuo = Dividendo
Tome como entrada dos números, realice la división entre ellos 
y entregue al usuario un texto descriptivo con la comprobación de la división.

1.6
Teniendo en cuenta el ejercicio anterior calcule el residuo con el símbolo de módulo % 
y entregue la comprobación con los valores resultantes de dividir dos números entregados
por el usuario del programa.
'''
# x=6 #dividendo
# y=2 #divisor

x=int (input ("favor entregar dividendo: ")) #dividendo
y=int (input ("favor entregar divisor: ")) #divisor

print("Dividimos dos numeros,",x,"entre",y)

#cociente
cociente=x//y
print("el cociente es:",cociente)

#residuo
residuo=x%y 
print("el residuo es:",residuo)

# final= y*cociente+residuo
# print("Aplicando la formula 'Divisor * Cociente + Residuo' se obtien el dividendo:",final)
print(f"aplicando la formula {y} por {cociente} mas {residuo} se obtiene el dividendo {x} ")