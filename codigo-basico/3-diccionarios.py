# diccionarios.py

user1 = {'nombre': 'Carlos', 'edad': 22, 'cursos': ['Cybsec', 'Automatización']}
user2 = {'nombre': 'Pepe', 'edad': 20, 'cursos': ['Cybsec', 'DAW']}
user3 = {'nombre': 'Maria', 'edad': 24, 'cursos': ['Cybsec', 'ASIR']}

print(user1)
print(user1['edad'])
print(user1['cursos'])
print(user1['cursos'][0])
print(user1['cursos'][1])

usuarios = []
usuarios.append(user1)
usuarios.append(user2)
usuarios.append(user3)

print(usuarios)

for usuario in usuarios:
    if usuario['edad'] > 21:
        print(usuario)

def mayor_de_edad(usuario):
    return usuario['edad'] > 21

usuarios_mayores = filter(mayor_de_edad, usuarios) # filter funciona con cualquier iterable
