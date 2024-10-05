
# elif es una abreviatura de else if, nos sirve para evaluar múltiples condiciones en un solo bloque de código.

rol = "moderador"
if rol == "administrador":
    print("Acceso completo: puedes modificar usuarios y configuraciones.")
else:
    if rol == "moderador":
        print("Acceso limitado: puedes gestionar el contenido.")
    else:
        if rol == "usuario":
            print("Acceso básico: puedes ver el contenido.")
        else:
            print("Acceso denegado: no tienes permisos en este sistema.")

# usando elif podemos simplificar el código anterior y no necesitar tantos niveles de indentación.

rol = "moderador"
if rol == "administrador":
    print("Acceso completo: puedes modificar usuarios y configuraciones.")
elif rol == "moderador":
    print("Acceso limitado: puedes gestionar el contenido.")
elif rol == "usuario":
    print("Acceso básico: puedes ver el contenido.")
else:
    print("Acceso denegado: no tienes permisos en este sistema.")
