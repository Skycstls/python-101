# Datatypes

entero = 5
flotante = 5.5
cadena = "Hola"
booleano = True
lista = [1, 2, 3, 4, 5]
tupla = (1, 2, 3, 4, 5)
diccionario = {"nombre": "Juan", "edad": 22}
nulo = None

# Propiedades de los datos

print(type(entero))
print(type(flotante))
print(type(cadena))

# Operaciones con datos

print(entero + flotante)
print(cadena + " Mundo")
print(entero * 5)

# Conversión de datos

print(str(entero)) 
print(int(flotante))
print(float(entero))
print(bool(0.1))
print(bool(0))

# Listas

print(lista[0])
print(lista[1:3])
print(lista[-1])
print(lista[1:])
print(lista[:3])

for elemento in lista:
    print(elemento)

# Tuplas

print(tupla[0])
print(tupla[1:3])
print(tupla[-1])
print(tupla[1:])
print(tupla[:3])

# Diccionarios u objetos

print(diccionario["nombre"])
print(diccionario["edad"])

