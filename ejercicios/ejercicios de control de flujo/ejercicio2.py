'''
Solicitar una edad y clasificarla en:
menores de edad (0-17)
adultos (18-64)
adultos mayores (65+)
para este ejercicio usar if elif else y match/case
'''

menor=range(0,18)
adulto=range(18,65)
mayores=range(65,120)

edad=int(input("ingrese su edad: "))

if edad in menor:
    print("usted es un menor de edad: ")
elif edad in adulto:
    print ("usted es un adulto: ")
else:
    print ("usted es un adulto mayor: ")
