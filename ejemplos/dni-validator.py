def validar_dni(dni):
    # Letras válidas según el resto de la división por 23
    letras = "TRWAGMYFPDXBNJZSQVHLCKE"

    # Comprobar formato: 8 dígitos y 1 letra al final
    if len(dni) != 9 or not dni[:8].isdigit() or not dni[8].isalpha():
        return False

    # Extraer el número y la letra del DNI
    numero = int(dni[:8])
    letra = dni[8].upper()  # Convertimos la letra a mayúscula por si acaso

    # Comprobar si la letra es correcta
    letra_correcta = letras[numero % 23]
    return letra == letra_correcta

# Ejemplo de uso
dni = "12345678Z"
if validar_dni(dni):
    print(f"El DNI {dni} es válido.")
else:
    print(f"El DNI {dni} no es válido.")
