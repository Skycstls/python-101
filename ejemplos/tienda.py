# los condicionales son una estructura de control que nos permiten tomar decisiones en nuestro código.

persona = {
    "nombre": "Carlos",
    "edad": 22,
    "euros": 10
}

lista_compra = ["patatas", "huevos", "agua"]

tienda = {
    "patatas_existencias": 500,
    "huevos_existencias": 0,
    "agua_existencias": 1,
    "patatas_precio": 2,
    "huevos_precio": 8,
    "leche_precio": 3
}

print(f"{persona['nombre']} tiene {persona['euros']} euros")

for producto in lista_compra:
    if producto == "patatas":
        if tienda["patatas_existencias"] > 0:
            if persona["euros"] >= tienda["patatas_precio"]:
                persona["euros"] -= tienda["patatas_precio"]
                tienda["patatas_existencias"] -= 1
                print(f"Compra de {producto} realizada")
            else:
                print(f"No tienes suficiente dinero para comprar {producto}")
        else:
            print(f"No hay existencias de {producto}")
    elif producto == "huevos":
        if tienda["huevos_existencias"] > 0:
            if persona["euros"] >= tienda["huevos_precio"]:
                persona["euros"] -= tienda["huevos_precio"]
                tienda["huevos_existencias"] -= 1
                print(f"Compra de {producto} realizada")
            else:
                print(f"No tienes suficiente dinero para comprar {producto}")
        else:
            print(f"No hay existencias de {producto}")
    elif producto == "agua":
        if tienda["agua_existencias"] > 0:
            if persona["euros"] >= tienda["leche_precio"]:
                persona["euros"] -= tienda["leche_precio"]
                tienda["agua_existencias"] -= 1
                print(f"Compra de {producto} realizada")
            else:
                print(f"No tienes suficiente dinero para comprar {producto}")
        else:
            print(f"No hay existencias de {producto}")
    else:
        print(f"El producto {producto} no está en la tienda")