# loops

for i in range(10):
    print(i)

for i in range(1, 11):
    print(i)

for i in range(1, 11, 2):
    print(i)

for i in range(10, 0, -1):
    print(i)

for i in range(10):
    if i == 5:
        break
    print(i)

valor = True
cantidad = 0
while valor:
    cantidad += 1
    if cantidad == 5:
        valor = False
    print(cantidad)

lista = ["A", "B", "C", "D", "E"]
for elemento in lista:
    print(elemento)

for i, elemento in enumerate(lista):
    print(i, elemento)

diccionario = {"nombre": "Juan", "edad": 22}
for key in diccionario:
    print(key, diccionario[key])

for key, value in diccionario.items():
    print(key, value)

