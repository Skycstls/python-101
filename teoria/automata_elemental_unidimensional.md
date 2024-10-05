# Automata Celular Elemental Unidimensional

https://atlas.wolfram.com/01/01/0/

Sistema para simular vida y evolución de celulas en una sola dimension, donde representamos el estado actual de una celula mediante X o ., donde X es una celula viva y . es una celula muerta.:

X => Viva
. => Muerta

Ejemplo de un sistema en su primera generación:
........X........

Cada celda evoluciona basandose en su estado actual y el estado de sus vecinos a la derecha e izquierda, en caso de no tener un vecino, cuenta como 0.

```plaintext
.X. <- Generación 0
 ↓  Dependiendo de los vecinos, la celda evoluciona a X o .
 ?  <- Generación 1
```

Hay 8 combinaciones posibles que podemos crear a partir de los trios de celda + vecinos.

Cada uno de estos casos se usa para determinar el estado de la celda en la siguiente generación.


Regla 0
XXX => .
XX. => .
X.X => .
X.. => .
.XX => .
.X. => .
..X => .
... => .
││└─ vecino
│└── celula actual
└─── vecino

Regla 1
XXX => .
XX. => .
X.X => .
X.. => .
.XX => .
.X. => .
..X => .
... => X

Regla 2
XXX => .
XX. => .
X.X => .
X.. => .
.XX => .
.X. => .
..X => X
... => .

Regla 3
XXX => .
XX. => .
X.X => .
X.. => .
.XX => .
.X. => .
..X => X
... => X


