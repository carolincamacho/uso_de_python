'''
Problema: Solicitar al usuario 5 números enteros, almacenarlos en una lista y luego mostrar:

    La lista original.

    La lista en orden inverso.

    La suma de los números.
'''

numero_1=int (input ("favor digitar primer numero: "))
numero_2=int (input ("favor digitar segundo numero: "))
numero_3=int (input ("favor digitar tercero numero: "))
numero_4=int (input ("favor digitar cuarto numero: "))
numero_5=int (input ("favor digitar quinto numero: "))

lista= [numero_1,numero_2,numero_3,numero_4,numero_5]
print("La lista es: ", lista)

lista.reverse()     #muestra la lista al contrario como se llenó
print("La lista en orden contrario es: ", lista)

lista.sort(reverse=True)    #ordena descendente
print("La lista ordenada es: ", lista)

print("La suma de la lista es: ", sum(lista))       #suma la lista
