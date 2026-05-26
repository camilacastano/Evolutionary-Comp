import random


random.seed(42)  # reproducibility
# ------------------------------------------------------------
# 55 random players
# ------------------------------------------------------------

jugadores = []

for i in range(55):

    jugador = {
        "nombre": f"Jugador_{i+1}",

        # Evaluated characteristics
        "technique": random.randint(70, 100),
        "physical_condition": random.randint(50, 100),
        "speed": random.randint(70, 100),
        "discipline": random.randint(80, 100),
        "experience": random.randint(70, 100),
        "red_cards": random.randint(0, 7)
    }

    jugadores.append(jugador)

# ------------------------------------------------------------
# weights
# ------------------------------------------------------------

pesos = {
    "technique": 0.30,
    "physical_condition": 0.20,
    "speed": 0.20,
    "discipline": 0.10,
    "experience": 0.10,
    "red_cards": 0.10,
}

# ------------------------------------------------------------
# Individual fitness function, how good a player is
# ------------------------------------------------------------

def fitness_jugador(jugador):

    fitness = (
        jugador["technique"] * pesos["technique"] +
        jugador["physical_condition"] * pesos["physical_condition"] +
        jugador["speed"] * pesos["speed"] +
        jugador["discipline"] * pesos["discipline"] +
        jugador["experience"] * pesos["experience"] -
        jugador["red_cards"] * pesos["red_cards"]
    )

    return fitness

# ------------------------------------------------------------
# fitness function for the complete team
# ------------------------------------------------------------

def fitness_equipo(equipo):

    total = 0

    for jugador in equipo:
        total += fitness_jugador(jugador)

    return total

# ------------------------------------------------------------
# initial random team of 22 players
# ------------------------------------------------------------

def crear_equipo():

    return random.sample(jugadores, 22)

# ------------------------------------------------------------
# hill Climbing modification:
# replace one player with another available player
# ------------------------------------------------------------

def generar_vecino(equipo_actual):

    nuevo_equipo = equipo_actual.copy()

    # select player to remove
    indice = random.randint(0, 21)

    # available players not already in the team
    disponibles = [
        j for j in jugadores if j not in nuevo_equipo
    ]

    # select a new player
    nuevo_jugador = random.choice(disponibles)

    # replace player
    nuevo_equipo[indice] = nuevo_jugador

    return nuevo_equipo

# ------------------------------------------------------------
# HILL CLIMBING ALGORITHM
# ------------------------------------------------------------

def hill_climbing(iteraciones):

    # initial random solution
    equipo_actual = crear_equipo()

    fitness_actual = fitness_equipo(equipo_actual)

    # best solution found
    mejor_equipo = equipo_actual
    mejor_fitness = fitness_actual

    print("Initial fitness:",
          round(fitness_actual, 2))
    
    for iteracion in range(iteraciones):

        vecino = generar_vecino(equipo_actual)
        fitness_vecino = fitness_equipo(vecino)

        # Accept ONLY if better
        if fitness_vecino > fitness_actual:

            equipo_actual = vecino
            fitness_actual = fitness_vecino

            # Update best solution
            if fitness_actual > mejor_fitness:

                mejor_equipo = equipo_actual
                mejor_fitness = fitness_actual

            print(
                f"Iteration {iteracion+1} "
                f"| Improvement found "
                f"| Fitness: {round(fitness_actual,2)}"
            )

        else:

            print(
                f"Iteration {iteracion+1} "
                f"| No improvement "
                f"| Current fitness: {round(fitness_actual,2)}"
            )

    return mejor_equipo, mejor_fitness

# EXECUTION
iteraciones = 100

mejor_equipo, mejor_fitness = hill_climbing(iteraciones)

# BEST SOLUTION FOUND

print("\n====================================")
print("BEST TEAM FOUND")
print("====================================")

for jugador in mejor_equipo:

    print(
        jugador["nombre"],
        "| Fitness:",
        round(fitness_jugador(jugador), 2)
    )

print("\nTotal fitness:",
      round(mejor_fitness, 2))
    
