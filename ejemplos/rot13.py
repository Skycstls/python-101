mensaje="Rotar cada caracter 13 posiciones en el abecedario"

def rot(c, n):
    if c.isalpha():
        abc = "abcdefghijklmnopqrstuvwxyz"
        i = abc.index(c.lower())
        return abc[(i+n)%26]
    else:
        return c

def rot13(mensaje):
    return "".join(rot(c, 13) for c in mensaje)

print(rot13(mensaje))
