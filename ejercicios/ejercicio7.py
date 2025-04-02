'''
Problema: Almacenar los nombres de 3 ciudades en una tupla y luego mostrar:

    La primera y la última ciudad.

    La cantidad de caracteres de cada ciudad.
'''
ciudad_1=str (input ("favor digitar primera ciudad: "))
ciudad_2=str (input ("favor digitar segunda ciudad: "))
ciudad_3=str (input ("favor digitar tercera ciudad: "))


ciudades= (ciudad_1,ciudad_2,ciudad_3)
print("La tupla es: ", ciudades)

print(ciudades[0],ciudades[2])
print(len(ciudades[0]),len(ciudades[1]),len(ciudades[2])) #usar f para texto
print (len(ciudades))
