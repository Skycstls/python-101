---
marp: true
theme: default
class: invert
size: 16:9
style: |
  img {background-color: transparent!important;}
  a:hover, a:active, a:focus {text-decoration: none;}
  header a {color: #ffffff !important; font-size: 30px;}
  footer {color: #148ec8;}
header: '[&#9671;](#1 " ")'
footer: 'Guia básica de sintaxis y conceptos de Python'
---

# Python

Guia básica de sintaxis y conceptos de Python

---

## ¿Qué es Python?

Es un lenguaje multiparadigma, interpretado, de tipado dinámico y fuertemente tipado.

`Multiparadigma` porque soporta programación orientada a objetos, programación imperativa y programación funcional.

`Interpretado` porque no necesita ser compilado, se ejecuta directamente en un interprete.

`Tipado dinámico` porque no es necesario declarar el tipo de dato de una variable.

`Fuertemente tipado` porque no se pueden realizar operaciones entre tipos de datos distintos.

---

## Variables

Las variables son espacios de memoria que se utilizan para almacenar valores. 

En Python, las variables no necesitan ser declaradas, simplemente se asigna un valor y Python se encarga de asignar el tipo de dato, esto se conoce como lenguaje dinámico.

```python
una_variable = "hola mundo"
otra_variable = 42
otra_variable_mas = 3.14
```

![bg right:30%](https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Collection_storage-Clearwater_County_History_Center_Shevlin%2C_MN-02.jpg/640px-Collection_storage-Clearwater_County_History_Center_Shevlin%2C_MN-02.jpg)

---

## Datos primitivos

Estos son los tipos de datos más básicos, no podemos descomponer estos tipos de datos en otros más simples.

- `int`: Números enteros como: 1, 312, -3, 0
- `float`: Números decimales, como: 3.14, -0.5, 1.0
- `str`: Cadenas de texto, como: "Hola mundo".
- `bool`: Booleanos, como: True, False
- `NoneType`: Valores nulos, en Python se representa con `None`

![bg left:30%](https://upload.wikimedia.org/wikipedia/commons/thumb/3/32/Lego_Color_Bricks.jpg/640px-Lego_Color_Bricks.jpg)

---

## Datos compuestos

Estos datos se forman a partir de otros datos primitivos.

- `lista`: colecciones ordenadas de elementos.
- `tupla`: colecciones ordenadas de elementos inmutables.
- `diccionario`: colecciones no ordenadas de elementos.
- `conjunto`: colecciones no ordenadas de elementos únicos.

![bg right:40%](https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Cro_protein_complex_with_DNA.png/640px-Cro_protein_complex_with_DNA.png)

---

## Enteros (int)

Los números enteros son aquellos que no tienen parte decimal.

```python
entero0 = 42
entero1 = 120
entero2 = -3
```

---

## Decimales (float)

Los números decimales son aquellos que tienen parte decimal.

```python
decimal0 = 3.14
decimal1 = -0.5
decimal2 = 1.0
```

---

## Cadenas de texto (str)

Las cadenas de texto son secuencias de caracteres.

```python
cadena0 = "Hola mundo"
cadena1 = "Python"
cadena2 = 'También se pueden usar comillas simples'
```

---

## Booleanos (bool)

Los booleanos son valores que pueden ser `True` o `False`.

```python
verdadero = True
falso = False
```

---

## Nulos (NoneType)

En Python, `None` es un valor especial que representa la ausencia de un valor.

```python
nulo = None
```

Esto es útil para inicializar variables que no tienen un valor definido. Más adelante en el código, podemos asignar un valor a la variable y comprobar si es `None` para saber si ha sido inicializada.

---

### Conversión de tipos

Python es un lenguaje de tipado dinámico, lo que significa que no es necesario declarar el tipo de una variable.

Sin embargo, también es de tipado fuerte, lo que significa que no se pueden realizar operaciones entre tipos de datos distintos.

Para convertir un tipo de dato a otro, podemos usar las funciones `int()`, `float()`, `str()`, `bool()`, etc.

![bg right:40%](https://upload.wikimedia.org/wikipedia/commons/thumb/a/ae/Metal_movable_type.jpg/640px-Metal_movable_type.jpg)

---

### Conversión de tipos

#### Conversión a entero

```python
entero_de_cadena1 = int("30")
entero_de_cadena2 = int("Hola")
entero_de_decimal = int("3.14")
entero_de_booleano = int("True")
```

---

### Conversión de tipos

#### Conversión a decimal

```python
decimal_de_entero = float(42) # 42.0
decimal_de_cadena1 = float("3.14") # 3.14
decimal_de_cadena2 = float("Hola") # ValueError: could not convert string to float: 'Hola'
decimal_de_booleano = float(True) # ValueError: could not convert string to float: 'True'
```

---

### Conversión de tipos

#### Conversión a cadena

```python
cadena_de_entero = str(42) # "42"
cadena_de_decimal = str(3.14) # "3.14"
cadena_de_booleano = str(True) # "True"
```

---

### Conversión de tipos

#### Conversión a booleano

```python
booleano_de_entero = bool(1) # True
booleano_de_entero = bool(-1) # True
booleano_de_entero = bool(0) # False
booleano_de_decimal = bool(3.14) # True
booleano_de_decimal2 = bool(0.000001)
booleano_de_cadena1 = bool("3.14") # True
booleano_de_cadena2 = bool(cadena2) # True
booleano_de_booleano = bool(booleano) # True
```

---

## Operadores

Los operadores son símbolos que se utilizan para realizar operaciones entre valores.

- Aritméticos: `+`, `-`, `*`, `/`, `%`, `//`
- Lógicos: `and`, `or`, `not`, `xor`, `nand`, `nor`, `xnor`
- Relacionales: `==`, `!=`, `<`, `>`, `<=`, `>=`
- Asignación: `=`, `+=`, `-=`, `*=`, `/=`, `%=`
- Bitwise: `&`, `|`, `^`, `~`, `<<`, `>>`

![bg left:40%](https://upload.wikimedia.org/wikipedia/commons/thumb/1/16/Telephone_operators_at_Weiss_Collection.jpg/640px-Telephone_operators_at_Weiss_Collection.jpg)

---

### Operadores aritméticos

Nos permiten realizar `operaciones matemáticas` sobre `cualquier dato`.

![bg right:40%](https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/PissarraMatem%C3%A0tiques1.jpg/640px-PissarraMatem%C3%A0tiques1.jpg)

---

### Operadores aritméticos 

#### Enteros y decimales

```python
1 + 1 # 2
3.1 * 0.04 # 0.124
5 / 2 # 2.5
5 // 2 # 2
5 % 2 # 1
```

---

### Operadores aritméticos 

#### Cadenas de texto

```python
"h" + "o" + "l" + "a" + "!" * 3
"hola" / 2 # error
"hola" * 2.5 # error
```

---

### Operadores aritméticos 

#### Sobre listas

```python
lista = [1, 2, 3, 4, 5]
lista + [6, 7, 8] # [1, 2, 3, 4, 5, 6, 7, 8]
lista * 2 # [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
```

---

### Operadores aritméticos 

#### Sobre diccionarios

```python
diccionario = {"a": 1, "b": 2, "c": 3}
diccionario + {"d": 4} # error
diccionario * 2 # error
```

---

### Operadores aritméticos 

#### Sobre tuplas

```python
tupla = (1, 2, 3, 4, 5)
tupla + (6, 7, 8) # (1, 2, 3, 4, 5, 6, 7, 8)
tupla * 2 # (1, 2, 3, 4, 5, 1, 2, 3, 4, 5)
```

---

### Operadores lógicos

Nos permiten realizar `operaciones lógicas` sobre `valores booleanos`.

Son abstracciones directas de las operaciones lógicas que se realizan en circuitos electrónicos.

```python
True and False # False
True or False # True
not True # False
True xor False # True
True nand False # True
True nor False # False
True xnor False # False
```

![bg right:40% width:400px](https://upload.wikimedia.org/wikipedia/commons/thumb/9/93/Logic_circuit_example.png/640px-Logic_circuit_example.png)

---

### Operadores lógicos

#### Enteros y decimales

```python
1 and 5 # 5
5 and 1 # 1
5 and 0 # 0
0 and 5 # 0

1 or 5 # 1
5 or 1 # 5
5 or 0 # 5
0 or 5 # 5
```

---

### Operadores lógicos

#### Cadenas de texto

```python
"hola" and "mundo" # "mundo"
"" and "mundo" # ""
"mundo"  and "" # ""
"hola" or "mundo" # "hola"
"" or "mundo" # "mundo"
"mundo" or "" # "mundo"
```

---

### Operadores de asignación

Nos permiten `asignar valores` a `variables`, también realizar operaciones y asignarlas.

```python
variable = 42
variable += 1 # 43
variable -= 1 # 42
variable *= 2 # 84
variable /= 2 # 42.0
```

![bg right:50% width:500px](https://upload.wikimedia.org/wikipedia/commons/thumb/1/1e/Finger_Pointing-Left-1574437693.svg/640px-Finger_Pointing-Left-1574437693.svg.png)

---

### Operadores relacionales

Nos permiten `comparar valores` y `obtener valores booleanos` como resultado.

![bg left:50%](https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Star-sizes-tr.jpg/640px-Star-sizes-tr.jpg)

---

### Operadores relacionales

#### Enteros y decimales

```python
1 == 1 # True
1 != 1 # False
1 < 1 # False
1 > 1 # False
1 <= 1 # True
1 >= 1 # True
```

---

### Operadores relacionales

#### Cadenas de texto

```python
"hola" == "hola" # True
"hola" != "hola" # False
```

---

### Operadores relacionales

#### Listas

```python
[1, 2, 3] == [1, 2, 3] # True
[1, 2, 3] != [1, 2, 3] # False
[1, 2, 3] < [1, 2, 3] # False
[1, 2, 3] > [1, 2, 3] # False
[1, 2, 3] <= [1, 2, 3] # True
[1, 2, 3] >= [1, 2, 3] # True
```

---

### Operadores relacionales

#### Diccionarios

```python
{"a": 1, "b": 2} == {"a": 1, "b": 2} # True
{"a": 1, "b": 2} != {"a": 1, "b": 2} # False
{"a": 1, "b": 2} < {"a": 1, "b": 2} # False
{"a": 1, "b": 2} > {"a": 1, "b": 2} # False
{"a": 1, "b": 2} <= {"a": 1, "b": 2} # True
{"a": 1, "b": 2} >= {"a": 1, "b": 2} # True
```

---

### Operadores relacionales

#### Tuplas

```python
(1, 2, 3) == (1, 2, 3) # True
(1, 2, 3) != (1, 2, 3) # False
(1, 2, 3) < (1, 2, 3) # False
(1, 2, 3) > (1, 2, 3) # False
(1, 2, 3) <= (1, 2, 3) # True
(1, 2, 3) >= (1, 2, 3) # True
```

---

## Control de flujo

El control de flujo nos permite `tomar decisiones` y `repetir acciones` en función de ciertas condiciones.

- `if`: Si se cumple una condición, se ejecuta un bloque de código.
- `else`: Si no se cumple la condición del `if`, se ejecuta un bloque de código.
- `elif`: Si no se cumple la condición del `if`, pero se cumple una condición adicional, se ejecuta un bloque de código.
- `for`: Se repite un bloque de código un número determinado de veces.
- `while`: Se repite un bloque de código mientras se cumpla una condición.
- `break`: Sal de un bucle `for` o `while`.

---

### if

Nos permite que un bloque de código se ejecute si se cumple una condición.

```python
edad = 18
if edad >= 18:
    print("Eres mayor de edad")
```

---

### else

Nos permite que un bloque de código se ejecute si no se cumple una condición.

```python
edad = 17

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
```

---

### elif

Nos deja añadir más condiciones a un bloque de código.

```python
euros = 10
pan_existencias = 2
cansado = False

if euros < 2:
    print("No tienes suficiente dinero")
elif pan_existencias <= 0:
    print("No hay pan")
elif cansado:
    print("Descansar")
else:
    print("Comprar pan")
```

---

El uso de `elif` evita la anidación excesiva de `if` y `else`:

```python
euros = 10
pan_existencias = 2
cansado = False

if euros >= 2:
    if pan_existencias > 0:
        if not cansado:
            print("Comprar pan")
        else:
            print("Descansar")
    else:
        print("No hay pan")
else:
    print("No tienes suficiente dinero")
```

---

### for

Nos permite repetir un bloque de código un número determinado de veces.

Una forma común de usar `for` es con la función `range()` para definir un rango de valores.

```python
for i in range(5):
    print(i)
```

---

### for

También podemos recorrer elementos de una lista, tupla, diccionario, conjunto o string.

```python
cadena = "Hola mundo"
for caracter in cadena:
    print(caracter)

lista = [1, 2, 3, 4, 5]
for elemento in lista:
    print(elemento)

diccionario = {"a": 1, "b": 2, "c": 3}
for clave, valor in diccionario.items():
    print(clave, valor)

conjunto = {1, 2, 3, 4, 5}
for elemento in conjunto:
    print(elemento)
```

---

### while

Nos permite repetir un bloque de código mientras se cumpla una condición.

```python
contador = 0
while contador < 5:
    print(contador)
    contador += 1
```

---

### while

#### Recorrer una lista

```python
nombres = ["juan", "pedro", "maría", "ana"]
indice = 0
nombres_cap = [] 
while indice < len(nombres) - 1:
    nombres_cap.append(nombres[indice].capitalize())
    indice += 1
```

---

While es útil cuando tenemos condiciones que no sabemos cuántas veces se van a repetir.

```python
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
```

---


