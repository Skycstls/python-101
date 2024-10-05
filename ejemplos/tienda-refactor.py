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

def mostrar_dinero(persona):
    print(f"{persona['nombre']} tiene {persona['euros']} euros")

def comprar_producto(producto, persona, tienda):
    if producto in tienda and tienda[f"{producto}_existencias"] > 0:
        precio = tienda[f"{producto}_precio"]
        if persona["euros"] >= precio:
            persona["euros"] -= precio
            tienda[f"{producto}_existencias"] -= 1
            print(f"Compra de {producto} realizada")
        else:
            print(f"No tienes suficiente dinero para comprar {producto}")
    else:
        print(f"No hay existencias de {producto}")

def procesar_lista_compra(lista_compra, persona, tienda):
    for producto in lista_compra:
        comprar_producto(producto, persona, tienda)

mostrar_dinero(persona)
procesar_lista_compra(lista_compra, persona, tienda)