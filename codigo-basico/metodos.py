# metodos de strings

cadena = "Hola mundo"

print(cadena.upper()) # HOLA MUNDO
print(cadena.lower()) # hola mundo
print(cadena.capitalize()) # Hola mundo
print(cadena.title()) # Hola Mundo
print(cadena.replace("Mundo", "Python")) # Hola Python
print(cadena.split(" ")) # ["Hola", "Mundo"]
print(cadena.find("M")) # 5
print(cadena.startswith("H")) # True
print(cadena.endswith("o")) # True
print(cadena.isnumeric()) # False
print(cadena.isalpha()) # False
print(cadena.isalnum()) # False

# metodos de listas

lista = ["A", "B", "C", "D", "E"]

print(lista.append("F"))
print(lista.remove("F"))
print(lista.pop(0))
print(lista.insert(0, "A"))
print(lista.count("A"))
print(lista.reverse())
print(lista.sort())
print(lista)

# metodos de tuplas

tupla = (1, 2, 3, 4, 5, 1)
print(tupla.count(1))
print(tupla.index(1))

# metodos de diccionarios

diccionario = {"nombre": "Juan", "edad": 22}

print(diccionario.keys())
print(diccionario.values())
print(diccionario.items())
print(diccionario.get("nombre"))
print(diccionario.get("apellido"))
print(diccionario.pop("nombre"))
print(diccionario)

# metodos de conjuntos

conjunto = {1, 2, 3, 4, 5}

conjunto.add(6)
conjunto.remove(6)
conjunto.discard(5)
