'''
Problema: Crear un diccionario con algunos productos 
y permitir que el usuario agregue un nuevo producto con su precio.
'''

productos={
    "chorizo": 1500,
    "arepa": 2400,
    "queso" : 3200
}
print (productos)
producto=input ("ingrese el nombre del producto: ")
precio=float (input ("ingrese el precio: "))
productos[producto]=precio
print (productos)
