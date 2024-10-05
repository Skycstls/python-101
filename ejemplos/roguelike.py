mapa = [
    [0, 0, 3, 0, 0],
    [0, 2, 2, 2, 0],
    [3, 2, 4, 2, 0],
    [0, 2, 0, 2, 0],
    [0, 0, 1, 0, 0]
]

elementos_mapa = {
    0: ".",
    1: "@",
    2: "#",
    3: "h",
    4: "x"
}

for fila in mapa:
    for elemento in fila:
        print(elementos_mapa[elemento], end=" ")
    print()
