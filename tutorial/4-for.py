# iterar sobre un rango de numeros con for
for valor in range(0,100):
    print(valor)

# iterar sobre un string
string = "cybsec zero"
for i in string:
    print(i)

# iterar sobre un string con un rango
for i in range(0,len(string)):
    print(string[i])

# iterar sobre una lista
lista = ["a","b","c","d","e"]
for i in lista:
    print(i)

# iterar sobre una lista con enumerate
for i, elemento in enumerate(lista):
    print(i,elemento)

# iterar sobre un diccionario
diccionario = {"nombre": "Juan", "edad": 22}
for key in diccionario:
    print(key, diccionario[key])

# crear un array aleatorio de una dimension

import random

array = []
for i in range(0,10):
    array.append(random.randint(0,100))
print(array)



