# Ordenamiento de Burbuja: Latencias de Red

Programa interactivo en Python que permite registrar los tiempos de respuesta (latencia en milisegundos) de distintos servidores y los ordena de menor a mayor para identificar los más rápidos.

## ¿Cómo funciona?
El programa compara los tiempos en parejas de elementos que están uno al lado del otro. Si el valor de la izquierda es mayor que el de la derecha, los cambia de lugar. Repite este recorrido en varias vueltas hasta que todos los datos quedan ordenados, deteniéndose automáticamente si detecta que la lista ya está en orden antes de terminar.

## Requisitos
* Tener instalado **Python 3**.

## Cómo ejecutarlo
1. Abre una terminal en la carpeta donde guardaste el archivo.
2. Ejecuta el comando:
   ```bash
   python ordenamiento_burbuja.py
3. Ingresa la cantidad de servidores que deseas registrar (mínimo 2) y escribe la latencia de cada uno cuando el programa lo solicite.