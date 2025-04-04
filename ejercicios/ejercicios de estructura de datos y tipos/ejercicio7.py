'''
Problema: Almacenar los nombres de 3 ciudades en una tupla y luego mostrar:

    La primera y la última ciudad.

    La cantidad de caracteres de cada ciudad.
'''
ciudad_1=str (input ("favor digitar primera ciudad: "))
ciudad_2=str (input ("favor digitar segunda ciudad: "))
ciudad_3=str (input ("favor digitar tercera ciudad: "))


ciudades= (ciudad_1,ciudad_2,ciudad_3)
print("Las ciudades en la tupla son: ",ciudades)

print("La primera y ultima ciudad de la tupla son: ",ciudades[0]," y ",ciudades[2])
print("La cantidad de caracteres de ",ciudad_1,"es: ",len(ciudades[0]),'\n',
      "La cantidad de caracteres de ",ciudad_2,"es: ",len(ciudades[1]),'\n',
      "La cantidad de caracteres de ",ciudad_3,"es: ",len(ciudades[2])) #usar f para texto
print ("La cantidad de ciudades en la tupla es de: ",len(ciudades))
