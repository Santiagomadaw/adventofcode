# --- Day 1: Trebuchet?! ---

Algo está mal con la producción global de nieve, y te han seleccionado para echar un vistazo. Los Elfos incluso te han dado un mapa; en él, han utilizado estrellas para marcar las cincuenta ubicaciones principales que probablemente estén teniendo problemas.

Has estado haciendo esto lo suficiente como para saber que para restaurar las operaciones de nieve, debes verificar todas las cincuenta estrellas antes del 25 de diciembre.

Recoge estrellas resolviendo rompecabezas. Dos rompecabezas estarán disponibles cada día en el calendario de Adviento; el segundo rompecabezas se desbloquea cuando completas el primero. Cada rompecabezas otorga una estrella. ¡Buena suerte!

Intentas preguntar por qué no pueden simplemente usar una máquina del tiempo ("no lo suficientemente potente") y a dónde te están enviando incluso ("al cielo") y por qué tu mapa parece en su mayoría en blanco ("seguro que haces muchas preguntas") y espera, ¿acabas de decir el cielo? ("por supuesto, ¿de dónde crees que viene la nieve?") cuando te das cuenta de que los Elfos ya te están cargando en una catapulta ("por favor, quédate quieto, necesitamos sujetarte").

Mientras están haciendo los ajustes finales, descubren que su documento de calibración (tu entrada de rompecabezas) ha sido modificado por un Elf muy joven que aparentemente estaba emocionado por mostrar sus habilidades artísticas. En consecuencia, los Elfos tienen problemas para leer los valores en el documento.

## Parte 1

El documento de calibración recién mejorado consiste en líneas de texto; cada línea originalmente contenía un valor de calibración específico que los Elfos ahora necesitan recuperar. En cada línea, el valor de calibración se puede encontrar combinando el primer dígito y el último dígito (en ese orden) para formar un solo número de dos dígitos.

Por ejemplo:

1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
En este ejemplo, los valores de calibración de estas cuatro líneas son 12, 38, 15 y 77. Sumar estos valores produce 142.

Considera todo tu documento de calibración. ¿Cuál es la suma de todos los valores de calibración?

## --- Part Two ---
Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

Equipped with this new information, you now need to find the real first and last digit on each line. For example:

two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.

What is the sum of all of the calibration values