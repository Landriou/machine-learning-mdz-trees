# Resultados de evaluacion de arboles de decision.

![WhatsApp Image 2021-10-31 at 23 52 12](https://user-images.githubusercontent.com/39389586/139701612-52960d39-65ea-4787-8c72-3889a1541076.jpeg)


# Investigar sobre las estrategias de los árboles de decisión para datos de tipo real y elaborar un breve resumen.

## Se puede dar el caso de que tengamos datos de entrada de tipo entero o reales, para eso


• Atributos de entrada continuos de valor entero: los atributos continuos de valor entero, tienen un número infinito de valores posibles. Más que generar infinitas ramas, los algoritmos de aprendizaje del árbol de decisión típicamente
encuentran el punto de ruptura (split point) que proporciona la máxima ganancia de
información. Por ejemplo, en un nodo del árbol se puede dar el caso de que el test sobre Altura>160 proporcione la mayor información.


## Tambien se puede dar tener una salida de valor continuo, para eso: 

• Atributos de salida de valor continuo: si intentamos predecir un valor numérico, como el precio de una obra de arte, más que una clasificación discreta necesitamos un árbol de regresión. Este tipo de árbol tiene en cada hoja una función
lineal de algún subconjunto de atributos numéricos, en vez de un valor simple. Por
ejemplo, la rama para grabados pintados a mano puede terminar con una función
lineal del área, edad y número de colores. El algoritmo de aprendizaje debe decidir cuándo dejar de dividir para comenzar a aplicar regresión lineal utilizando los
atributos restantes.
