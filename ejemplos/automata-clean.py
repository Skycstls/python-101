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

n = 31
generaciones = 15

fila = [0] * n
fila[n // 2] = 1 

def imprimir_fila(fila):
    output = ""
    for celda in fila:
        if celda == 1:
            output += "■"
        else:
            output += " "
    print(output)

imprimir_fila(fila)

for _ in range(generaciones):
    nueva_generacion = [0] * n 
    for i in range(1, n - 1):
        vecino_izq = fila[i - 1]
        vecino_der = fila[i + 1]
        celula_activa = fila[i]
        trio = (vecino_izq, celula_activa, vecino_der)
        nueva_generacion[i] = regla30_tabla[trio] 
    fila = nueva_generacion 
    imprimir_fila(fila)

