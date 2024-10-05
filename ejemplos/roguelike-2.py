from random import choice

elementos_mapa = {
    0: ".",
    1: "@",
    2: "#",
    3: "h",
    4: "x"
}

mapa = []
for i in range(5):
    fila = []
    for j in range(5):
        fila.append(choice([0, 0, 0, 0, 0, 0, 0, 0, 0, 1]))
    mapa.append(fila)

for fila in mapa:
    for elemento in fila:
        print(elementos_mapa[elemento], end=" ")
    print()
