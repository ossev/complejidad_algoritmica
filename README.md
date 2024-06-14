# COMPLEJIDAD ALGORITMICA

## Introducción

### ¿Por qué comparamos la eficiencia de un algoritmo?

  Dependiendo del algoritmo, este se puede tardar un poco o se puede tardar demasiado. Esto puede ser costoso.

### Complejidad algoritmica vs complejidad espacial?

  Cuanto tiempo nos vamos a tardar ejecutando un algoritmo vs cuando tiempo en memoria va a ocupar la ejecución del algoritmo

### Podemos definirla como T(n)

  Una función T que recibe un input n

## Aproximaciones

### ¿Cómo podemos implementar esta función de tiempo?

Esto depende de varias factores cuando probamos en local

- La capacidad de nuestra laptop
- Los programas que se estén ejecutando en nuestra laptop

Tambien podemos contar los pasos que ejecuta nuestro algoritmo
Este enfoque es un poquito más preciso, pero la solución puede variar de algorimo a algoritmo y esto termina introduciendo muchos términos que pueden ser irrelevantes.

En cualquier caso una mejor solución seria contar los pasos del algoritmo, pero con una medida asintótica.

El concepto de medida asintotica se refiere al análisis del comportamiento de un algoritmo en función de su rendimiento y complejidad a medida que el tamaño de la entrada (n) crece haci el infinito. Es una forma de describir el rendimiento de una algoritmo de manera teórica y abstracta, sin necesidas de ejecutarlo realmente. La idea principal es centrarse en cómo la cantidad de pasos o el tiempo de ejecución del algoritmo crece a medida que aumenta el tamaño de la entrada.

En el análisis de algoritmos, hay varias notaciones asintóticas comunes que se utilizan para describir este crecimiento:

1. Notación O grande (Big O):Describe el peor caso o el límite superior del tiempo de ejecución de un algoritmo. Indica el crecimiento máximo de los recursos requeridos (tiempo, espacio) en función del tamaño de la entrada. Por ejemplo, O(n) significa que el tiempo de ejecución crece linealmente con el tamaño de la entrada.
2. Notación Omega (Ω): Indica el mejor caso o el límite inferior del tiempo de ejeución de un algoritmo. India el menor crecimiento de un de los recursos requeridos en el mejor escesario. Por ejemplo: Ω(n) significa que el tiempo de ejecución crece al menos linealmente con el tamaño de la entrada.
3. Notación Theta (Θ). Describe el caso promedio o el crecimiento exacto del tiempo de ejecuión de un algoritmo. Indica que el tiempo de eejcución crece de manera consistente con el tamaño de la entrada. Por ejemplo, Θ(n) significa que el tiempo de ejeución crece linealmente con el tamaño de la entrada en todos los casos.

### Ejemplo de medida asintótica

Considera dos funciones para calcular el factorial de un número, una iterativa y otra recursiva:

1. Función iterativa:

   ```python
    def factorial_iterative(n: int) -> int:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
   ```

   Complejidad: O(n), porque realiza un bucle desde 2 hasta n, ejecutándose n-1 veces.

2. Funcion recursiva:

   ```python
    def factorial_recursive(n: int) -> int:
        if n == 0 or n == 1:
            return 1
        return n * factorial_recursive(n - 1)

   ```

   Complejidad: O(n), porque cada llamada recursiva reduce el tamaña de la entrada en 1, resultando en n llamadas recursivas.

### Importancia del Análisis Asintótico

El análisis asintótico es importante porque permite comparar la eficiencia de diferentes algoritmos sin tener que implementarlos y ejecutarlos. Proporciona una forma de predecir cómo se comportarán los algoritmos con entradas de tamaño grande y ayuda a seleccionar el algoritmo más adecuado para un problema específico.

En resumen, el análisis asintótico es una herramienta teórica que permite describir y comparar la eficiencia de los algoritmos en función del tamaño de la entrada, proporcionando una forma abstracta de medir su rendimiento a gran escala.

## Abstracción

Tomememos en cuenta la siguiente función:

```python
def f(x):
  respuesta = 0
  for i in range(1000):
    respuesta += 1

  for i in range(x):
    respuesta += x

  for i in range(x):
    for j in range(x):
      respuesta += 1
      respuesta += 1
  
  return respuesta
```

1. Primer bucle:  
  Este primer bucle se ejecuta 1000 veces independiente del valor de x. Esto es una operación constante:  
  $\ O(1000)=O(1)$  

2. Segundo bucle:  
  Este bucle se ejecutad x veces y cada iteración tiene una opearción de suma que tambień depeden de x:  
  $\ x×1=O(x)$

3. Tercer bucle:  
  Este es un bucle anidado. El bucle exterior se ejecuta 𝑥 veces y el bucle interior también se ejecuta 𝑥 veces. Dentro del blucle interno, hay dos operaciones de suma, pero ambasa son constantes, por lo que cada iteraciń del bucle interno tiene un costo constante:  
  $\ x×x×2 = 2x = O(x^2)$

### Sumando las complejidades

Ahora sumamos todas las complejidades de cada parte de la función:  
La notación Big O considera la tasa de crecimiento más alta, ignorando los coeficientes y términos de menor orden. En este caso, el término dominante es $\ O(x^2)$.  

#### Notación Big O final  

$\ O(1) + O(x) + O(x^2) = O(x^2)$

Por lo tanto, la notación asintótica de la función $\ f(x)$ es:

$\ O(x^2)$
