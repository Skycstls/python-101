#estructura if-else

if True:
    print("Se cumple la condición")
else:
    print("No se cumple la condición")

#estructura if-elif-else
colores = ["verde", "amarillo", "rojo"]
temperatura = 37
if temperatura < 35:
    print(f"La temperatura es {temperatura}ºC, el color es {colores[0]}")
else:
    if temperatura < 37:
        print(f"La temperatura es {temperatura}ºC, el color es {colores[1]}")
    else:
        print(f"La temperatura es {temperatura}ºC, el color es {colores[2]}")

#estructura if-elif-else simplificada

if temperatura < 35:
    print(colores[0])
elif temperatura < 37:
    print(colores[1])
else:
    print(colores[2])

# solo con if y else no funcionaria, ya que se ejecutarian las dos condiciones
temperatura = 36
if temperatura < 35:
    print(colores[0])
if temperatura < 37:
    print(colores[1])
else:
    print(colores[2])