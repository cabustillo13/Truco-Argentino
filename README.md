# Truco-Argentino
Saber cuántos puntos para el envido tengo en una mano, analizando una imagen.

![Programa principal](https://github.com/cabustillo13/Truco-Argentino/blob/master/Ejemplo/Screenshot0.png)

**INTRODUCCIÓN**

El truco se juega con una baraja española sin ochos, nueves, ni comodines, para jugar de a dos o cuatro se pueden retirar los dieces. 

Consiste en un "partido" en el cual los jugadores se enfrentan, y gana el primer jugador o equipo de jugadores que llega a un número determinado de puntos, que suele ser 15 o 30, según lo determinen los participantes previamente. 

Consta de 4 palos ( o pintas): Espada, basto, oro y copa.

**CONTEXTO**

Particularmente con este programa abordamos lo que es el **Envido**, que consiste en sumar las dos cartas de mayor valor del mismo palo más 20 a esa suma. En el envido las cartas 10, 11 y 12 tienen valor cero al momento de sumarlas. 

_Ejemplo: Sí se tiene las siguientes cartas: 11 de espada, 7 de espada y 3 de oro. El envido es: 0+7 + 20 = 27_

_Ejemplo: Sí se tiene las siguientes cartas: 6 de espada, 7 de espada y 3 de oro. El envido es: 6+7 + 20 = 33_

_Ejemplo: Sí se tiene las siguientes cartas: 10 de oro, 12 de oro y 4 de copa. El envido es: 0+0 + 20 = 20_

Cuando las 3 cartas sean de distinto palo, el valor del envido es el mayor valor entre las 3 cartas.

_Ejemplo: Sí se tiene las siguientes cartas: 10 de oro, 2 de espada y 4 de copa. El envido es: 4_

![Envido](https://github.com/cabustillo13/Truco-Argentino/blob/master/Ejemplo/Screenshot2.png)

Existe un caso particular llamado **Flor**, que resulta cuando se tienen las 3 cartas del mismo palo. Se suman los 3 valores de las cartas más 20.

_Ejemplo: Sí se tiene las siguientes cartas: 11 de espada, 7 de espada y 3 de espada. El envido es: 0+7+3 + 20 = 30_

El máximo valor que se puede obtener en el envido es 33. También con la flor. 

En caso de que se tenga flor y la suma de las 3 cartas supere 33. Solo se deben sumar las dos cartas con mayor valor más 20.

_Ejemplo: Sí se tiene las siguientes cartas: 5 de espada, 7 de espada y 3 de espada. El envido es: 5+7 + 20 = 32_
