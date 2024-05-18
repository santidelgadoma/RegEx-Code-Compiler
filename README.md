# Proyecto2
## Descripción del problema
El proyecto tiene como objetivo construir un reconocedor sencillo de enunciados while bien formados de un lenguaje de programación. El programa debe leer los datos de entrada, que consisten en un conjunto de bloques while sintácticamente correctos, y debe determinar si el conjunto de bloques es aceptado o rechazado como correcto. Además, el programa debe generar una serie de estadísticas relacionadas con las condiciones de prueba de cada while.
## Objetivo del proyecto
El objetivo de este proyecto es construir un reconocedor sencillo de enunciados while bien formados de un lenguaje de programación específico. El programa debe ser capaz de:
- Leer datos de entrada: el programa debe leer datos de entrada que consisten en un conjunto de bloques while sintácticamente correctos. El formato específico de los datos de entrada debe definirse claramente.
-	Determinar la validez de los bloques while: el programa debe analizar cada bloque while y determinar si cumple con las reglas sintácticas definidas para las sentencias while en el lenguaje de programación elegido.
-	Generar estadísticas: el programa debe generar un conjunto de estadísticas relacionadas con las condiciones de prueba de cada sentencia while analizada. Estas estadísticas incluyen, por ejemplo, el número total de variables (diferentes) usadas en todos los while encontrados, el número total de operadores de comparación encontrados (con repeticiones) y el número total de while's que contienen los bloques parseados.
-	Nosotros consideramos que para que un enunciado while sea correcto, debe tener la siguiente estructura: la palabra while, seguido de un paréntesis que abre, dentro del cual se coloca una variable o constante, seguido de un signo de comparación, y luego otra variable o constante, cerrando con un paréntesis. A esto le sigue una llave que abre, dentro de la cual puede haber otra estructura while o simplemente una llave que cierra.
  ### Ejemplos aceptados:
  while(x < 9){  
     while(6 > y){}  
  }  
  ### Ejemplo no aceptado:
  while(8 < i)  
      while(j > l){  
      }  
-	En la siguiente imagen se puede ver el automata de pila que se usó. Se encarga de rechazar los errores de sintaxis o conteo de corchetes o parentesis.
![imagen1](https://github.com/179786-moises/p2/blob/main/p1.jpg)
## Forma de uso
### Prerrequisitos:
-	El usuario debe contar con Python para hacer uso del programa.
- El usuario debe almacenar el texto que desea analizar con el código en un archivo de texto.
-	El usuario debe guardar en la misma carpeta el archivo de código y el archivo de texto.
### Pasos:
-	En la terminal, el usuario debe pararse sobre la carpeta donde se encuentran los archivos antes mencionados, es decir, aplicar los comandos “cd C:/…”
-	En la terminal el usuario debe escribir el siguiente comando” py .\main.py .\prueba.txt”, donde prueba.txt es el archivo de texto creado por el usuario para revisar y main.py es el código proporcionado para obtener las respuestas.
### Restricciones:
-	Si no se detecta un archivo de texto se imprime "Ingresa un archivo de texto por favor", es decir, si al momento de ingresar el comando el archivo que se sube no es de texto se imprime eso.
-	Si no se detecta un parámetro se imprime "Ingresa un archivo de texto como parámetro por favor", es decir, si al momento de ingresar el comando” py .\main.py .\prueba.txt” no se pone .”\prueba.txt”.
-	Si la cadena contenida dentro del archivo de texto no cuenta con número correcto de llaves, el código te da de salida “cadena invalida”.
-	Si en la cadena hay errores de redacción entonces, la salida da “cadena invalida”.
###  Ejemplos:
-	En el primer ejemplo usaremos el que se nos proporcionó en canvas.
![imagen2](https://github.com/179786-moises/p2/blob/main/1.png)
-	En el segundo ejemplo usaremos el mismo pero quitaremos el último corchete.
![imagen3](https://github.com/179786-moises/p2/blob/main/2.png)
- En el tercer ejemplo usaremos el primero pero sin el primer corchete.
![imagen3](https://github.com/179786-moises/p2/blob/main/2.png)
-	En el cuarto ejemplo usaremos el segundo bloque proporcionado en canvas que tiene error.
![imagen4](https://github.com/179786-moises/p2/blob/main/3.png)
 	
