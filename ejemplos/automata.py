# Tabla que define la Regla 30
# El índice es la tripleta (vecinos izquierda, centro, derecha) en binario
# El valor es el nuevo estado de la célula central
regla30_tabla = {
    (1, 1, 1): 0,
    (1, 1, 0): 0,
    (1, 0, 1): 0,
    (1, 0, 0): 1,
    (0, 1, 1): 1,
    (0, 1, 0): 1,
    (0, 0, 1): 1,
    (0, 0, 0): 0
}

# Tamaño del autómata (número de celdas en la fila)
n = 31  # Número impar para empezar desde el centro
# Número de generaciones
generaciones = 90

# Fila inicial con un solo bloque activo en el centro
fila = [0] * n
fila[n // 2] = 1  # La celda central es 1

# Función para imprimir la fila actual
def imprimir_fila(fila):
    output = ""
    for celda in fila:
        if celda == 1:
            output += "■"
        else:
            output += " "
    print(output)

# Imprimimos la fila inicial
imprimir_fila(fila)

# Evolucionamos el autómata
for _ in range(generaciones):
    nueva_fila = [0] * n  # Creamos una nueva fila vacía
    # Aplicamos la regla a cada tripleta de celdas
    for i in range(1, n - 1):  # Evitamos los extremos
        tripleta = (fila[i - 1], fila[i], fila[i + 1])  # Vecinos (izq, centro, der)
        nueva_fila[i] = regla30_tabla[tripleta]  # Usamos la tabla para encontrar el nuevo valor
    fila = nueva_fila  # Actualizamos la fila actual
    imprimir_fila(fila)

