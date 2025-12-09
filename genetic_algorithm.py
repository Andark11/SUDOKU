from typing import List, Tuple
import random
from copy import deepcopy

def count_conflicts(board: List[List[int]], original_board: List[List[int]]) -> int:
    """Cuenta el número de conflictos en el tablero (menor es mejor)"""
    conflicts = 0
    
    # Verificar que los números fijos no hayan cambiado (penalización muy alta)
    for i in range(9):
        for j in range(9):
            if original_board[i][j] != 0 and board[i][j] != original_board[i][j]:
                conflicts += 1000  # Penalización masiva por cambiar números fijos
    
    # Verificar filas
    for row in board:
        conflicts += 9 - len(set(row))
    
    # Verificar columnas
    for col in range(9):
        column = [board[row][col] for row in range(9)]
        conflicts += 9 - len(set(column))
    
    # Verificar cajas 3x3
    for box_row in range(3):
        for box_col in range(3):
            box = []
            for i in range(box_row * 3, box_row * 3 + 3):
                for j in range(box_col * 3, box_col * 3 + 3):
                    box.append(board[i][j])
            conflicts += 9 - len(set(box))
    
    return conflicts

def create_individual(original_board: List[List[int]]) -> List[List[int]]:
    """Crea un individuo llenando las celdas vacías con números aleatorios válidos por fila"""
    individual = deepcopy(original_board)
    
    for row_idx in range(9):
        # Obtener números que faltan en la fila
        existing = [num for num in individual[row_idx] if num != 0]
        missing = [num for num in range(1, 10) if num not in existing]
        random.shuffle(missing)
        
        # Llenar las celdas vacías
        missing_idx = 0
        for col_idx in range(9):
            if individual[row_idx][col_idx] == 0:
                individual[row_idx][col_idx] = missing[missing_idx]
                missing_idx += 1
    
    return individual

def crossover(parent1: List[List[int]], parent2: List[List[int]], 
              original_board: List[List[int]]) -> List[List[int]]:
    """Realiza cruce de dos padres intercambiando filas completas manteniendo invariantes"""
    child = deepcopy(parent1)
    
    # Intercambiar filas completas del padre 2 (esto mantiene la propiedad de números únicos por fila)
    for row_idx in range(9):
        if random.random() < 0.5:
            # Verificar que la fila del padre2 respeta los números fijos
            row_valid = True
            for col_idx in range(9):
                if original_board[row_idx][col_idx] != 0:
                    if parent2[row_idx][col_idx] != original_board[row_idx][col_idx]:
                        row_valid = False
                        break
            
            # Solo copiar la fila si respeta los números fijos
            if row_valid:
                child[row_idx] = deepcopy(parent2[row_idx])
    
    return child

def mutate(individual: List[List[int]], original_board: List[List[int]], 
           mutation_rate: float) -> List[List[int]]:
    """Aplica mutación intercambiando dos celdas no fijas en una fila"""
    mutated = deepcopy(individual)
    
    for row_idx in range(9):
        if random.random() < mutation_rate:
            # Encontrar columnas que no están fijas
            mutable_cols = [col for col in range(9) if original_board[row_idx][col] == 0]
            
            if len(mutable_cols) >= 2:
                col1, col2 = random.sample(mutable_cols, 2)
                mutated[row_idx][col1], mutated[row_idx][col2] = \
                    mutated[row_idx][col2], mutated[row_idx][col1]
    
    return mutated

def tournament_selection(population: List[Tuple[List[List[int]], int]], 
                        tournament_size: int = 5) -> List[List[int]]:
    """Selecciona un individuo mediante torneo"""
    tournament = random.sample(population, tournament_size)
    winner = min(tournament, key=lambda x: x[1])
    return winner[0]

def genetic_algorithm(board: List[List[int]], 
                     population_size: int = 200,
                     generations: int = 5000,
                     mutation_rate: float = 0.4,
                     elitism_count: int = 5) -> Tuple[List[List[int]], bool]:
    """Resuelve el Sudoku usando algoritmo genético"""
    
    original_board = deepcopy(board)
    
    # Crear población inicial
    population = []
    for _ in range(population_size):
        individual = create_individual(original_board)
        fitness = count_conflicts(individual, original_board)
        population.append((individual, fitness))
    
    best_ever_fitness = float('inf')
    generations_without_improvement = 0
    max_generations_without_improvement = 500
    
    for generation in range(generations):
        # Ordenar por fitness
        population.sort(key=lambda x: x[1])
        
        # Verificar si encontramos la solución
        if population[0][1] == 0:
            return population[0][0], True
        
        # Tracking del mejor fitness
        if population[0][1] < best_ever_fitness:
            best_ever_fitness = population[0][1]
            generations_without_improvement = 0
        else:
            generations_without_improvement += 1
        
        # Detener si no hay mejora
        if generations_without_improvement >= max_generations_without_improvement:
            break
        
        # Nueva generación
        new_population = []
        
        # Elitismo: mantener los mejores
        for i in range(elitism_count):
            new_population.append(population[i])
        
        # Generar el resto de la población
        while len(new_population) < population_size:
            parent1 = tournament_selection(population)
            parent2 = tournament_selection(population)
            
            child = crossover(parent1, parent2, original_board)
            child = mutate(child, original_board, mutation_rate)
            
            fitness = count_conflicts(child, original_board)
            new_population.append((child, fitness))
        
        population = new_population
    
    # Retornar el mejor individuo encontrado
    population.sort(key=lambda x: x[1])
    return population[0][0], population[0][1] == 0
