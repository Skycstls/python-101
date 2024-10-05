frutas=["manzana","pera","uva","sandia","melon", "manzana"]

'''
print(frutas)
print(frutas[0])
print(frutas[1])

frutas=["manzana","pera","uva","sandia","melon", "manzana"]
for fruta in frutas:
    print(fruta)

for i, fruta in enumerate(frutas):
    print(i, fruta)
'''

frutas=["manzana","pera","uva","sandia","melon", "manzana"]

print(len(frutas))

for i in range(0,4):
    print(frutas[i])

# En python podemos usar una lista como un stack (pila) y como un queue (cola), cada uno sigue un modelo LIFO (Last In First Out) y FIFO (First In First Out) respectivamente.

# Un stack es, basicamente, un bote de patatas pringles, el último elemento que se haya añadido a la lista es el que se irá el primero.

bote = []
bote.append("😀")
bote.append("😂")
bote.append("😍")
print(bote)
bote.pop()
print(bote)

# Un queue es una fila de personas para un concierto, el primero que llega es el primero que entra.

fila = []
fila.append("😀")
fila.append("😂")
fila.append("😍")
print(fila)
fila.pop(0)
print(fila)
fila.pop(0)

import random
emojis = ["🐍", "🐙", "🐇"]
emoji_aleatorio = random.choice(emojis)
print(emoji_aleatorio)
