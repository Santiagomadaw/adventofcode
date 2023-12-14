# --- Day 8: Haunted Wasteland ---

## Parte 1

Parece que debes utilizar las instrucciones izquierda/derecha para navegar por la red. Tal vez, si haces que el camello siga las mismas instrucciones, puedas escapar del páramo embrujado.

Después de examinar los mapas por un rato, destacan dos nodos: AAA y ZZZ. Tienes la sensación de que AAA es donde te encuentras ahora, y debes seguir las instrucciones izquierda/derecha hasta llegar a ZZZ.

Este formato define cada nodo de la red individualmente. Por ejemplo:

```
RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)
```

Comenzando con AAA, debes buscar el próximo elemento según la siguiente instrucción izquierda/derecha en tu entrada. En este ejemplo, comienza con AAA y ve a la derecha (R) eligiendo el elemento derecho de AAA, CCC. Luego, L significa elegir el elemento izquierdo de CCC, ZZZ. Siguiendo las instrucciones izquierda/derecha, llegas a ZZZ en 2 pasos.

Por supuesto, es posible que no encuentres ZZZ de inmediato. Si te quedas sin instrucciones izquierda/derecha, repite toda la secuencia de instrucciones según sea necesario: RL realmente significa RLRLRLRLRLRLRLRL... y así sucesivamente. Por ejemplo, aquí hay una situación que toma 6 pasos para llegar a ZZZ:

```
LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
```

Comenzando en AAA, sigue las instrucciones izquierda/derecha. ¿Cuántos pasos se requieren para llegar a ZZZ?

Tu respuesta al acertijo fue *****.


**<span style="color: yellow;">¡La primera mitad de este acertijo está completa! Te otorga una estrella dorada: **⭐**.</span>**
## Parte 2

La tormenta de arena está sobre ti y no estás más cerca de escapar del páramo. Hiciste que el camello siguiera las instrucciones, pero apenas has salido de tu posición inicial. ¡Va a tomar significativamente más pasos escapar!

¿Y si el mapa no es para personas? ¿Y si el mapa es para fantasmas? ¿Están los fantasmas incluso sujetos a las leyes del espacio-tiempo? Solo hay una manera de averiguarlo.

Después de examinar los mapas un poco más, tu atención se centra en un hecho curioso: ¡el número de nodos con nombres que terminan en A es igual al número que termina en Z! Si fueras un fantasma, probablemente comenzarías en cada nodo que termine con A y seguirías todos los caminos al mismo tiempo hasta que todos terminen simultáneamente en nodos que terminen con Z.

Por ejemplo:

```
LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)
```

Aquí, hay dos nodos de inicio, 11A y 22A (porque ambos terminan con A). A medida que sigues cada instrucción izquierda/derecha, utiliza esa instrucción para navegar simultáneamente lejos de ambos nodos en los que te encuentras actualmente. Repite este proceso hasta que todos los nodos en los que te encuentras actualmente terminen con Z. (Si solo algunos de los nodos en los que te encuentras terminan con Z, actúan como cualquier otro nodo y continúas normalmente). En este ejemplo, procederías de la siguiente manera:

Paso 0: Estás en 11A y 22A.
Paso 1: Eliges todos los caminos a la izquierda, llevándote a 11B y 22B.
Paso 2: Eliges todos los caminos a la derecha, llevándote a 11Z y 22C.
Paso 3: Eliges todos los caminos a la izquierda, llevándote a 11B y 22Z.
Paso 4: Eliges todos los caminos a la derecha, llevándote a 11Z y 22B.
Paso 5: Eliges todos los caminos a la izquierda, llevándote a 11B y 22C.
Paso 6: Eliges todos los caminos a la derecha, llevándote a 11Z y 22Z.

Entonces, en este ejemplo, terminas completamente en nodos que terminan en Z después de 6 pasos.

Comienza simultáneamente en cada nodo que termine con A. ¿Cuántos pasos toma antes de que solo estés en nodos que terminan con Z?

Tu respuesta al acertijo fue *************.

**<span style="color: yellow;">¡Ambas partes de este rompecabezas están completas! Proporcionan dos estrellas doradas: **⭐⭐**.</span>**
