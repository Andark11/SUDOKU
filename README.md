# 🧩 Solucionador de Sudoku

Un solucionador de Sudoku interactivo implementado en Python que utiliza algoritmos de búsqueda DFS (Depth-First Search) y BFS (Breadth-First Search) para resolver puzzles de diferentes niveles de dificultad.

## 📋 Características

- **Tres algoritmos de búsqueda**: DFS, BFS y Algoritmo Genético
- **Generación aleatoria de Sudokus** con 4 niveles de dificultad
- **Interfaz interactiva** en línea de comandos
- **Medición de tiempo de ejecución**
- **Visualización clara** del tablero con separadores
- **Modo continuo** para resolver múltiples Sudokus sin cerrar el programa

## 🎮 Niveles de Dificultad

1. **Fácil**: 30 celdas vacías
2. **Medio**: 40 celdas vacías
3. **Difícil**: 50 celdas vacías
4. **Extremo**: 60 celdas vacías

## 🚀 Uso

### Ejecutar el programa

Se sugiere ampliamente se compiele en VSC
Una vez parado en la ruta de intalación de la carpera

```bash
python3 main.py
```

### Flujo de uso

1. Selecciona el algoritmo (DFS, BFS o GA)
2. Selecciona el nivel de dificultad (1-4)
3. El programa genera un Sudoku aleatorio
4. El algoritmo resuelve el puzzle
5. Se muestra el tiempo de ejecución
6. Decide si quieres resolver otro Sudoku o salir

## 📁 Estructura del Proyecto

```
SUDOKU/
├── main.py                      # Interfaz principal y generación de Sudokus
├── dfs.py                       # Implementación del algoritmo DFS
├── bfs.py                       # Implementación del algoritmo BFS
├── genetic_algorithm.py         # Implementación del Algoritmo Genético
├── posibles_movimientos.py      # Funciones para calcular movimientos válidos
├── populated_move.py            # Estrategia básica de llenado
├── populated_move_smart.py      # Estrategia inteligente de llenado
├── is_complete_board.py         # Verificación de tablero completo
├── dead_end.py                  # Validación de estado del tablero
└── README.md                    # Este archivo
```

## 🧠 Algoritmos

### DFS (Depth-First Search)
- Explora en profundidad cada rama de posibilidades
- Usa backtracking cuando encuentra un camino sin salida
- Generalmente más rápido para la mayoría de Sudokus
### BFS (Breadth-First Search)
- Explora todas las posibilidades nivel por nivel
- Usa una cola para gestionar los estados
- Garantiza encontrar la solución más "corta" en términos de decisiones

### GA (Genetic Algorithm - Algoritmo Genético)
- Inspirado en la evolución biológica y selección natural
- Mantiene una población de soluciones candidatas
- Usa operadores genéticos: selección por torneo, cruce y mutación
- Optimiza minimizando conflictos en filas, columnas y cajas
- Converge hacia la solución a través de generaciones
- Elitismo para preservar las mejores soluciones
- Garantiza encontrar la solución más "corta" en términos de decisiones

## 🔍 Estrategias de Resolución

El programa utiliza múltiples estrategias:

1. **Movimiento único**: Coloca números cuando solo hay una opción válida en una celda
2. **Estrategia inteligente**: Encuentra números que solo pueden ir en una posición específica dentro de filas, columnas o cajas
3. **Búsqueda con backtracking**: Prueba posibilidades cuando las estrategias básicas no son suficientes

## 📊 Ejemplo de Salida

```
==================================================
=== SOLUCIONADOR DE SUDOKU ===
==================================================

Tablero inicial:
5 3 . | . 7 . | . . . 
6 . . | 1 9 5 | . . . 
. 9 8 | . . . | . 6 . 
---------------------
8 . . | . 6 . | . . 3 
4 . . | 8 . 3 | . . 1 
7 . . | . 2 . | . . 6 
---------------------
. 6 . | . . . | 2 8 . 
. . . | 4 1 9 | . . 5 
. . . | . 8 . | . 7 9 

Resolviendo con DFS...

¡Sudoku resuelto!
5 3 4 | 6 7 8 | 9 1 2 
6 7 2 | 1 9 5 | 3 4 8 
1 9 8 | 3 4 2 | 5 6 7 
---------------------
8 5 9 | 7 6 1 | 4 2 3 
4 2 6 | 8 5 3 | 7 9 1 
7 1 3 | 9 2 4 | 8 5 6 
---------------------
9 6 1 | 5 3 7 | 2 8 4 
2 8 7 | 4 1 9 | 6 3 5 
3 4 5 | 2 8 6 | 1 7 9 

Tiempo de ejecución: 0.0149 segundos
```

## 🛠️ Requisitos

- Python 3.x
- No requiere librerías externas

## 📝 Notas

- El generador crea Sudokus aleatorios que siempre tienen solución
- Los tiempos de ejecución varían según la complejidad del puzzle
- El programa valida que el tablero sea resoluble en cada paso

## 👨‍💻 Autor

Proyecto creado como demostración de algoritmos de búsqueda aplicados a la resolución de Sudoku.
