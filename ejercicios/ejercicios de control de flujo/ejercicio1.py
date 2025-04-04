'''
Crear una lista de palabras definidas y pedir al usuarios una palabra. Indicar si esta en la lista o no.
'''

mi_lista=["enero","febrero","marzo"]
consulta=input("ingrese el mes a buscar: ").lower()

if consulta in mi_lista:
    print ("el mes esta en al lista")
else:
    print ("el mes no esta en la lista")
