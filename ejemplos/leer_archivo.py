texto = open("ejemplo.txt", "r")
print(type(texto))
a = texto.read()
print(a)
texto.close()

b = a.replace("One", "Zero")

print(b)