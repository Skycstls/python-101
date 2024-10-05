def pushy(str):
    # ABCD -> BCDA
    return str[1::]+str[0]

mensaje = "mundoHola "
for i in range(100):
    mensaje = pushy(mensaje)
    print(i, mensaje)



