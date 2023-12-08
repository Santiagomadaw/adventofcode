
# Día 5: Si Le Das Una Semilla A Un Fertilizante

Tomas el bote y encuentras al jardinero justo donde te dijeron que estaría: administrando un gigantesco "jardín" que más bien parece una granja.

"¿Una fuente de agua? ¡Isla Isla *es* la fuente de agua!" Señalas que la Isla de la Nieve no está recibiendo agua.

"Oh, tuvimos que detener el agua porque nos *quedamos sin arena* para [filtrarla](https://en.wikipedia.org/wiki/Sand_filter); no se puede hacer nieve con agua sucia. No te preocupes, estoy seguro de que obtendremos más arena pronto; solo apagamos el agua hace unos días... semanas... oh no." Su rostro cae en una expresión de horrorosa realización.

"He estado tan ocupado asegurándome de que todos aquí tengan comida que olvidé por completo revisar por qué dejamos de recibir más arena. Hay un ferry que sale pronto y se dirige en esa dirección, es mucho más rápido que tu bote. ¿Podrías por favor echarle un vistazo?"

Apenas tienes tiempo para aceptar esta solicitud cuando plantea otra. "Mientras esperas el ferry, tal vez puedas ayudarnos con nuestro *problema de producción de alimentos*. Acaba de llegar el último [Almanaque](https://en.wikipedia.org/wiki/Almanac) de la Isla, y estamos teniendo problemas para entenderlo".

El almanaque (tu entrada de rompecabezas) enumera todas las semillas que deben plantarse. También enumera qué tipo de suelo usar con cada tipo de semilla, qué tipo de fertilizante usar con cada tipo de suelo, qué tipo de agua usar con cada tipo de fertilizante, y así sucesivamente. Cada tipo de semilla, suelo, fertilizante, etc., se identifica con un número, pero los números se reutilizan en cada categoría, es decir, el suelo `123` y el fertilizante `123` no necesariamente están relacionados entre sí.

Por ejemplo:

```plaintext
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
```

El almanaque comienza enumerando qué semillas deben plantarse: semillas `79`, `14`, `55`, y `13`.

El resto del almanaque contiene una lista de *mapas* que describen cómo convertir números de una *categoría fuente* a números de una *categoría destino*. Es decir, la sección que comienza con `mapeo de semilla a suelo` describe cómo convertir un *número de semilla* (la fuente) en un *número de suelo* (el destino). Esto permite que el jardinero y su equipo sepan qué suelo usar con qué semillas, qué agua usar con qué fertilizante, y así sucesivamente.

En lugar de listar cada número fuente y su número destino correspondiente uno por uno, los mapas describen rangos completos de números que se pueden convertir. Cada línea dentro de un mapa contiene tres números: el *inicio del rango de destino*, el *inicio del rango fuente*, y la *longitud del rango*.

Considera nuevamente el ejemplo `mapeo de semilla a suelo`:

```plaintext
50 98 2
52 50 48
```

La primera línea tiene un *inicio de rango de destino* de `50`, un *inicio de rango fuente* de `98`, y una *longitud de rango* de `2`. Esta línea significa que el rango fuente comienza en `98` y contiene dos valores: `98` y `99`. El rango de destino es de la misma longitud, pero comienza en `50`, por lo que sus dos valores son `50` y `51`. Con esta información, sabes que el número de semilla `98` corresponde al número de suelo `50` y que el número de semilla `99` corresponde al número de suelo `51`.

La segunda línea significa que el rango fuente comienza en `50` y contiene `48` valores: `50`, `51`, ..., `96`, `97`. Esto corresponde a un rango de destino que comienza en `52` y también contiene `48` valores: `52`, `53`, ..., `98`, `99`. Entonces, el número de semilla `53` corresponde al número de suelo `55`.

Cualquier número fuente que *no esté mapeado* corresponde al *mismo* número de destino. Así que, el número de semilla `10` corresponde al número de suelo `10`.

Entonces, la lista completa de números de semilla y sus correspondientes números de suelo se vería así:

```plaintext
seed  soil
0      0
1      1
...    ...
48     48
49     49
50     52
51     53
...    ...
96     98
97     99
98     50
99     51
```

Con este mapa, puedes buscar el número de suelo requerido para cada número de semilla inicial:

- Seed number `79` corresponde al número de suelo `81`.
- Seed number `14` corresponde al número de suelo `14`.
- Seed number `55` corresponde al número de suelo `57`.
- Seed number `13` corresponde al número de suelo `13`.

El jardinero y su equipo quieren comenzar lo antes posible, así que les gustaría saber la ubicación más cercana que necesita una semilla. Utilizando estos mapas, encuentra *el número de ubicación más bajo que corresponde a alguna de las semillas iniciales*. Para hacer esto, deberás convertir cada número de semilla a través de otras categorías hasta que puedas encontrar su número de *ubicación correspondiente*. En este ejemplo, los tipos correspondientes son:

- Semilla `79`, suelo `81`, fertilizante `81`, agua `81`, luz `81`, temperatura `19`, humedad `69`, ubicación `37`.
- Semilla `14`, suelo `14`, fertilizante `0`, agua `11`, luz `25`, temperatura `19`, humedad `69`, ubicación `56`.
- Semilla `55`, suelo `57`, fertilizante `7`, agua `7`, luz `7`, temperatura `81`, humedad `0`, ubicación `93`.
- Semilla `13`, suelo `13`, fertilizante `69`, agua `1`, luz `7`, temperatura `68`, humedad `0`, ubicación `60`. 

Entonces, el número de ubicación más bajo en este ejemplo es 35.

**En resumen, ¿Cuál es el número de ubicación más bajo que corresponde a cualquiera de los números iniciales de semillas?**

---

**© 2023 Eric Wastl.** All rights reserved. Want to play along? [Advent of Code](https://adventofcode.com/) is designed for fun, education, and friendly competition.
```
