import random

numero_secreto = random.randint(1, 100)

while True:
    numero = int(input("Adivina el número secreto: "))
    if numero == numero_secreto:
        print("¡Has adivinado el número secreto!")
        break
    elif numero < numero_secreto:
        print("El número secreto es mayor")
    else:
        print("El número secreto es menor")