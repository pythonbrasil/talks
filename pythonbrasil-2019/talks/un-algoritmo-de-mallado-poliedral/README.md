<p align="center"><img src="../logo_python_brasil_2019-01.svg" width="200"></p>

# Palestra: Un algoritmo de Mallado Poliedral en 3 Dimensiones para Aproximar Soluciones a Problemas Físicos Singulares
Apresentada por: **Alexis Jawtuschenko**


A palestra **Un algoritmo de Mallado Poliedral en 3 Dimensiones para Aproximar Soluciones a Problemas Físicos Singulares** foi apresentada no dia 25/10/2019, durante a [Conferência Python Brasil 2019](http://2019.pythonbrasil.org.br).



### Slides

Sem slides disponíveis. Você pode ajudar a publicá-los aqui?



### Sobre Palestra
Muchos problemas de la geometría y de la física se modelizan en términos de ecuaciones diferenciales, que son ecuaciones que relacionan a una función desconocida con algunas de sus derivadas. En casi todos los casos, si bien está demostrada la existencia y unicidad de la solución de una de tales ecuaciones, es imposible computarla analíticamente de manera exacta, y entonces un abordaje posible es construir un método numérico para construir otra función que sea una aproximación (todo lo cercana que se quiera) de esta función desconocida. Estas aproximaciones se dan en forma de una función definida por\npartes, siguiendo una cierta subdivisión de la región del espacio en donde ocurre el fenómeno físico de interés. La definición y construcción de un método numérico propio comienza, entonces, con la explicitación del proceso de mallado, que consiste en una sucesión infinita de subdivisiones del dominio, con elementos de medida tan pequeña como se quiera. Después de esto, la definición de todos los objetos de cálculo concreto y de análisis teórico concernientes al método numérico depende de cuáles son precisamente los puntos, las aristas, las caras y los poliedros de las mallas. Un programa\nde mallado debe tomar como entrada alguna información geométrica sucinta de la región a subdividir y entregar como salida alguna tabulación concreta de los puntos, aristas, caras y poliedros de la malla. Por ejemplo una lista de archivos de texto. Presentamos en esta charla la implementación en Python/NumPy que implementa (y grafica) un algoritmo de mallado propuesto por el autor, junto su método numérico asociado, en su trabajo de tesis doctoral por la Universidad de Buenos Aires. Además mostraremos brevemente parte del segundo programa que ensambla el sistema lineal de ecuaciones, a partir de las mallas, cuya solución son las coordenadas que determinan a la solución aproximada de una ecuación diferencial modelo.



### Minibio
Doctor de la Universidad de Buenos Aires, Área Ciencias Matemáticas. \n\nProfesor Adjunto en el Departamento de Matemática y Ciencias de la Universidad \nde San Andrés.\n\nJefe de Trabajos Prácticos en la Facultad de Ciencias Exactas y Naturales\nde la Universidad de Buenos Aires.\n\nBecario Doctoral del CONICET entre 2012 y 2017.\nProgramador Python/GNU Octave/C++ orientado a matemática/ciencia.


