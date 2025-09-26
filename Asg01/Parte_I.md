# Asignación 01 - Parte I: Ejercicios de Programación Fundamental

## 1. Encontrar Máximo Sin Funciones Integradas

**Enunciado del Problema:**
Escriba un programa que encuentre el valor máximo en una lista de números sin usar la función integrada `max()`. El programa también debe reportar la posición (índice) donde ocurre el máximo. La lista de números será ingresada como valores separados por comas.

**Sugerencia:** Similar a encontrar el mínimo, pero también mantener un registro del índice donde ocurre el máximo.

**Entrada:** Una cadena con números separados por comas
**Salida:** El valor máximo y su posición en la lista

**Ejemplos:**

**Ejemplo 1:**
```
Numeros: 5,2,8,1,9,3
Maximo: 9, Posicion: 4
```

**Ejemplo 2:**
```
Numeros: -3,-1,-5,-2
Maximo: -1, Posicion: 1
```

**Ejemplo 3:**
```
Numeros: 7,7,3,7,2
Maximo: 7, Posicion: 0
```

---

## 2. Calcular Promedio Sin Funciones Integradas

**Enunciado del Problema:**
Escriba un programa que calcule el promedio aritmético (media) de una lista de números sin usar funciones integradas como `sum()`. El resultado debe mostrarse con 2 decimales de precisión.

**Sugerencia:** Use un acumulador para sumar valores, luego divida por la longitud de la lista. Use formateo de cadenas para la precisión decimal.

**Entrada:** Una cadena con números separados por comas
**Salida:** El promedio de los números con 2 decimales

**Ejemplos:**

**Ejemplo 1:**
```
Numeros: 10,20,30,40,50
Promedio: 30.00
```

**Ejemplo 2:**
```
Numeros: 85,90,78,92,88
Promedio: 86.60
```

**Ejemplo 3:**
```
Numeros: 5,7,3,9,1,4,6
Promedio: 5.00
```

---

## 3. Patrón de Triángulo

**Enunciado del Problema:**
Escriba un programa que imprima un patrón de triángulo rectángulo usando asteriscos (*). El usuario especifica la altura del triángulo. Cada fila debe tener tantos asteriscos como su número de fila.

**Sugerencia:** Use bucles anidados - el externo para las filas, el interno para las columnas. Use multiplicación de cadenas para caracteres repetidos.

**Entrada:** Un número entero positivo (altura del triángulo)
**Salida:** Patrón de triángulo con asteriscos

**Ejemplos:**

**Ejemplo 1:**
```
Altura: 4
*
**
***
****
```

**Ejemplo 2:**
```
Altura: 3
*
**
***
```

**Ejemplo 3:**
```
Altura: 6
*
**
***
****
*****
******
```

---

## 4. Patrón de Tablero de Ajedrez

**Enunciado del Problema:**
Escriba un programa que cree un patrón de tablero de ajedrez usando dos caracteres diferentes ('X' y 'O'). El usuario especifica el tamaño (n x n cuadrículas). Las posiciones alternas deben usar caracteres diferentes.

**Sugerencia:** Use aritmética modular para determinar qué carácter usar basado en las coordenadas de posición.

**Entrada:** Un número entero positivo (tamaño del tablero)
**Salida:** Patrón de tablero de ajedrez

**Ejemplos:**

**Ejemplo 1:**
```
Tamano: 4
XOXO
OXOX
XOXO
OXOX
```

**Ejemplo 2:**
```
Tamano: 3
XOX
OXO
XOX
```

**Ejemplo 3:**
```
Tamano: 5
XOXOX
OXOXO
XOXOX
OXOXO
XOXOX
```

---

## 5. Invertir Palabras

**Enunciado del Problema:**
Escriba un programa que tome una oración y invierta cada palabra individualmente manteniendo el mismo orden de las palabras. Por ejemplo, "Hola Mundo" se convierte en "aloH odnuM".

**Sugerencia:** Divida la oración en palabras, invierta cada palabra usando slicing, luego únalas de nuevo.

**Entrada:** Una oración (cadena de texto)
**Salida:** La misma oración con cada palabra invertida

**Ejemplos:**

**Ejemplo 1:**
```
Oracion: Hola Mundo
Resultado: aloH odnuM
```

**Ejemplo 2:**
```
Oracion: Python es genial
Resultado: nohtyP se laineg
```

**Ejemplo 3:**
```
Oracion: Programar divierte mucho
Resultado: ramargorP etreivid ohcum
```

---

## 6. Verificador de Anagramas

**Enunciado del Problema:**
Escriba un programa que determine si dos palabras son anagramas (contienen las mismas letras con la misma frecuencia). El programa debe ignorar las diferencias entre mayúsculas y minúsculas.

**Sugerencia:** Cuente las frecuencias de caracteres en ambas palabras, compare los resultados. Alternativa: ordene los caracteres y compare.

**Entrada:** Dos palabras separadas por una coma
**Salida:** "Son anagramas" o "No son anagramas"

**Ejemplos:**

**Ejemplo 1:**
```
Palabras: amor,roma
Resultado: Son anagramas
```

**Ejemplo 2:**
```
Palabras: casa,saca
Resultado: Son anagramas
```

**Ejemplo 3:**
```
Palabras: perro,gato
Resultado: No son anagramas
```

---

## 7. Intersección de Listas

**Enunciado del Problema:**
Escriba un programa que encuentre los elementos comunes entre dos listas (intersección). El resultado no debe contener duplicados y debe estar ordenado de menor a mayor.

**Sugerencia:** Use bucles anidados para comparar elementos, o use un diccionario para rastrear ocurrencias en ambas listas.

**Entrada:** Dos listas de números separados por comas, cada lista en una línea diferente
**Salida:** Lista con los elementos comunes ordenados

**Ejemplos:**

**Ejemplo 1:**
```
Lista 1: 1,2,3,4,5
Lista 2: 3,4,5,6,7
Interseccion: [3, 4, 5]
```

**Ejemplo 2:**
```
Lista 1: 10,20,30,40
Lista 2: 15,20,25,30
Interseccion: [20, 30]
```

**Ejemplo 3:**
```
Lista 1: 1,1,2,3,3
Lista 2: 2,2,3,4,4
Interseccion: [2, 3]
```

---

## 8. Particionador de Listas

**Enunciado del Problema:**
Escriba un programa que particione una lista en dos listas: una con números pares y otra con números impares. Debe mantener el orden original dentro de cada partición.

**Sugerencia:** Cree dos listas vacías, itere a través de la lista original, agregue a la lista apropiada basado en la prueba par/impar.

**Entrada:** Una lista de números enteros separados por comas
**Salida:** Dos listas separadas (pares e impares)

**Ejemplos:**

**Ejemplo 1:**
```
Numeros: 1,2,3,4,5,6,7,8
Pares: [2, 4, 6, 8]
Impares: [1, 3, 5, 7]
```

**Ejemplo 2:**
```
Numeros: 10,15,20,25,30
Pares: [10, 20, 30]
Impares: [15, 25]
```

**Ejemplo 3:**
```
Numeros: 3,7,9,11
Pares: []
Impares: [3, 7, 9, 11]
```