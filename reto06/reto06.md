
# Advent of Code


## Día 5: Si Le Das Una Semilla A Un Fertilizante

Coges el bote y encuentras al jardinero justo donde te dijeron que estaría: gestionando un gigantesco "jardín" que más bien parece una granja.

"¿Una fuente de agua? ¡La isla Island *es* la fuente de agua!" Señalas que Snow Island no está recibiendo agua.

"Oh, tuvimos que detener el agua porque nos *quedamos sin arena* para [filtrar](https://en.wikipedia.org/wiki/Sand_filter) con ella. No se puede hacer nieve con agua sucia. No te preocupes, seguro que conseguiremos más arena pronto; solo apagamos el agua hace unos días... semanas... oh no." Su rostro se hunde en una expresión de horror al darse cuenta.

"He estado tan ocupado asegurándome de que todos aquí tengan comida que olvidé por completo revisar por qué dejamos de recibir más arena. Hay un ferry que sale pronto en esa dirección; es mucho más rápido que tu bote. ¿Podrías ir a investigar, por favor?"

Apenas tienes tiempo de aceptar esta solicitud cuando plantea otra. "Mientras esperas al ferry, tal vez puedas ayudarnos con nuestro *problema de producción de alimentos*. Acaba de llegar el último [Almanaque](https://en.wikipedia.org/wiki/Almanac) de Island Island y tenemos problemas para entenderlo."

...

**¿Cuál es el número de ubicación más bajo que corresponde a cualquiera de los números de semilla iniciales?**
*Tu respuesta del rompecabezas fue* `**********`.

---

## Parte Dos

Todos morirán de hambre si solo plantas tan pocas semillas. Releyendo el almanaque, parece que la línea `seeds:` en realidad describe *rangos de números de semillas*.

Los valores en la línea inicial de `seeds:` vienen en pares. Dentro de cada par, el primer valor es el *inicio* del rango y el segundo valor es la *longitud* del rango. Así que, en la primera línea del ejemplo anterior:

```
seeds: 79 14 55 13
```

Esta línea describe dos rangos de números de semillas que se plantarán en el jardín. El primer rango comienza con el número de semilla `79` y contiene `14` valores: `79`, `80`, ..., `91`, `92`. El segundo rango comienza con el número de semilla `55` y contiene `13` valores: `55`, `56`, ..., `66`, `67`.

Ahora, en lugar de considerar cuatro números de semilla, necesitas considerar un total de *27* números de semilla.

En el ejemplo anterior, el número de ubicación más bajo se puede obtener a partir del número de semilla `82`, que corresponde a la tierra `84`, fertilizante `84`, agua `84`, luz `77`, temperatura `45`, humedad `46`, y *ubicación `46`*. Entonces, el número de ubicación más bajo es `46`.

**¿Cuál es el número de ubicación más bajo que corresponde a cualquiera de los números de semilla iniciales?**
*Tu respuesta del rompecabezas fue* `*********`.

**¡Ambas partes de este rompecabezas están completas! Proporcionan dos estrellas doradas: ⭐⭐**
