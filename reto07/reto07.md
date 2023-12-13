# --- Day 7: Camel Cards ---

## Parte 1

En Camel Cards, se te proporciona una lista de manos, y tu objetivo es ordenarlas según la fuerza de cada mano. Una mano consta de cinco cartas etiquetadas con A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3 o 2. La fuerza relativa de cada carta sigue este orden, donde A es la más alta y 2 es la más baja.

Cada mano es exactamente de un tipo. De más fuerte a más débil, son:

- **Five of a kind:** cinco cartas con la misma etiqueta: AAAAA
- **Four of a kind:** cuatro cartas con la misma etiqueta y una carta con una etiqueta diferente: AA8AA
- **Full house:** tres cartas con la misma etiqueta y las dos cartas restantes comparten una etiqueta diferente: 23332
- **Three of a kind:** tres cartas con la misma etiqueta, y las dos cartas restantes son diferentes entre sí y de cualquier otra carta en la mano: TTT98
- **Two pair:** dos cartas comparten una etiqueta, otras dos comparten una segunda etiqueta, y la carta restante tiene una tercera etiqueta: 23432
- **One pair:** dos cartas comparten una etiqueta, y las otras tres cartas tienen una etiqueta diferente de la pareja y entre sí: A23A4
- **High card:** todas las etiquetas de las cartas son distintas: 23456

Las manos se ordenan principalmente según el tipo; por ejemplo, cada full house es más fuerte que cualquier three of a kind.

Si dos manos tienen el mismo tipo, se aplica una segunda regla de ordenación. Comienza comparando la primera carta de cada mano. Si estas cartas son diferentes, la mano con la primera carta más fuerte se considera más fuerte. Si la primera carta en cada mano tiene la misma etiqueta, entonces pasa a considerar la segunda carta en cada mano. Si son diferentes, la mano con la segunda carta más alta gana; de lo contrario, continúa con la tercera carta en cada mano, luego la cuarta, luego la quinta.

Entonces, 33332 y 2AAAA son ambas manos de four of a kind, pero 33332 es más fuerte porque su primera carta es más fuerte. Del mismo modo, 77888 y 77788 son ambas full house, pero 77888 es más fuerte porque su tercera carta es más fuerte (y ambas manos tienen la misma primera y segunda carta).

Para jugar a Camel Cards, se te proporciona una lista de manos y sus ofertas correspondientes (tu entrada de rompecabezas). Por ejemplo:

```
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
```

Este ejemplo muestra cinco manos; cada mano está seguida de su cantidad de oferta. Cada mano gana una cantidad igual a su oferta multiplicada por su rango, donde la mano más débil obtiene el rango 1, la segunda mano más débil obtiene el rango 2, y así sucesivamente hasta la mano más fuerte. Debido a que hay cinco manos en este ejemplo, la mano más fuerte tendrá el rango 5 y su oferta se multiplicará por 5.

Entonces, el primer paso es ordenar las manos por fuerza:

- 32T3K es la única one pair y las otras manos son de un tipo más fuerte, así que obtiene el rango 1.
- KK677 y KTJJT son ambas two pair. Sus primeras cartas tienen la misma etiqueta, pero la segunda carta de KK677 es más fuerte (K vs. T), por lo que KTJJT obtiene el rango 2 y KK677 obtiene el rango 3.
- T55J5 y QQQJA son ambas three of a kind. QQQJA tiene una primera carta más fuerte, así que obtiene el rango 5 y T55J5 obtiene el rango 4.

Ahora, puedes determinar las ganancias totales de este conjunto de manos sumando el resultado de multiplicar la oferta de cada mano por su rango (765 *1 + 220* 2 + 28 *3 + 684* 4 + 483 * 5). Entonces, las ganancias totales en este ejemplo son 6440.

Encuentra el rango de cada mano en tu conjunto. ¿Cuáles son las ganancias totales?

Tu respuesta al rompecabezas fue: [la respuesta al rompecabezas].

## Parte 2

 Para hacer las cosas un poco más interesantes, el Elfo introduce una regla adicional. Ahora, las cartas J son comodines (jokers) que pueden actuar como cualquier carta que haga que la mano sea del tipo más fuerte posible.

Para equilibrar esto, las cartas J son ahora las cartas individuales más débiles, incluso más débiles que el 2. Las otras cartas permanecen en el mismo orden: A, K, Q, T, 9, 8, 7, 6, 5, 4, 3, 2, J.

Las cartas J pueden fingir ser cualquier carta que sea mejor para determinar el tipo de mano; por ejemplo, QJJQ2 ahora se considera four of a kind. Sin embargo, con el propósito de romper empates entre dos manos del mismo tipo, J siempre se trata como J, no como la carta que está simulando ser: JKKK2 es más débil que QQQQ2 porque J es más débil que Q.

Ahora, el ejemplo anterior se desarrolla de manera muy diferente:

```
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
```

- 32T3K sigue siendo el único one pair; no contiene ningún comodín, así que su fuerza no aumenta.
- KK677 es ahora el único two pair, convirtiéndolo en la segunda mano más débil.
- T55J5, KTJJT y QQQJA son ahora todas four of a kind. T55J5 obtiene el rango 3, QQQJA obtiene el rango 4 y KTJJT obtiene el rango 5.

Con la nueva regla de comodines, las ganancias totales en este ejemplo son 5905.

Usando la nueva regla de comodines, encuentra el rango de cada mano en tu conjunto. ¿Cuáles son las nuevas ganancias totales?

Tu respuesta al rompecabezas fue: **243101568**.

**<span style="color: yellow;">¡Ambas partes de este rompecabezas están completas! Proporcionan dos estrellas doradas: **⭐⭐**.</span>**
