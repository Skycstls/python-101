string = "HOLA MUNDO"

diccionario = {
    "O": "0",
    "I": "1",
    "E": "3",
    "A": "4",
    "S": "5",
    "T": "7",
    "B": "8",
    "G": "9"
}

for letra in string:
    if letra in diccionario:
        string = string.replace(letra, diccionario[letra])