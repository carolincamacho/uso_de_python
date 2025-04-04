# uso de case

dia=input("ingrese el dia de la semana: ").lower()
match dia:
    case "sabado" | "domingo":
        print(f"{dia} es fin de semana")
    case "lunes":
        print(f"{dia} es un dia dificil")
    case "martes" |"miercoles" | "jueves" | "viernes":
        print(f"{dia} es dia de la semana")
    case _: #es el default del case
        print("no es un dia de la semana")
