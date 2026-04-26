# TP1 - Teoría de Algoritmos

## Requisitos

- Python 3.10 o superior

Librerías utilizadas, todas estándar.
No se requieren instalaciones adicionales.

---

## Ejecución de los problemas

### Problema 1 - División y conquista

Implementación de búsqueda de moneda falsa.

```bash
python DyC.py
```

Versión alternativa:
```bash
python DyCAlternativa.py
```

### Problema 2 - Greedy

Cálculo de caminos mínimos en grafos (Dijkstra).

```bash
python Greedy.py
```
El programa permite:

- Ingreso manual del grafo
- Uso de datos de prueba predefinidos

### Problema 3 - Backtracking

Resolución de laberintos generados aleatoriamente.

- Ejecución con valores por defecto: 
```bash
python Backtracking.py
```
- Especificando tamaño del laberinto:
```bash
python Backtracking.py filas columnas
```

Ejemplo:
```bash
python Backtracking.py 20 20
```

- Especificando tamaño y densidad de paredes:
```bash
python Backtracking.py filas columnas densidad
```

Con densidad: valor entre 0 y 1 (prob) que indica la densidad de paredes

Ejemplo:
```bash
python Backtracking.py 20 20 0.3
```

### Problema 4 - Programación Dinámica

Descomposición de una cadena en el menor número de palíndromos.
```bash
python Dinamico.py
```