'''
Problema: Crear un diccionario con las calificaciones de 3 estudiantes 
y permitir que el usuario consulte la calificación de uno de ellos.
'''

calificaciones={
    "luisa": 3.8,
    "david": 4.6,
    "tatiana": 4.9
}
consulta=input("por favor ingresar el estudiante a consultar: ")
#print (calificaciones[consulta])
print (calificaciones.get(consulta,"el estudiante no esta"))
