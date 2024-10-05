# if siempre necesita un valor booleano para evaluar, si le pasamos un valor que no sea booleano, python lo convertirá a booleano.

if 1:
    print("1 es True")

if 0:
    print("Nunca verás este mensaje")

if "Hola":
    print("Hola es True")

if "":
    print("Nunca verás este mensaje")

if [1, 2, 3]:
    print("La lista [1, 2, 3] es True")

if []:
    print("Nunca verás este mensaje")

diccionario = {"nombre": "Juan", "edad": 22}

if "nombre" in diccionario:
    print("nombre está en el diccionario")

if "Juan" in diccionario.values():
    print("Juan es un valor del diccionario")

if "apellido" not in diccionario:
    print("apellido no está en el diccionario")

if "apellido" not in diccionario.keys():
    print("apellido no está en el diccionario")

if "apellido" not in diccionario.items():
    print("apellido no está en el diccionario")

# Los valores que son considerados False en python son:
# 0
# ""
# []
# {}
# None
# False
#
# Todos los demás valores son considerados True.

#