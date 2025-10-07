## Autor: Álvaro Hernández Villarreal

import random

def main():
    tortuga1 = 0
    tortuga2 = 0
    tortuga3 = 0
    meta = 100

    print("¡Bienvenido a la carrera de tortugas!")
    print("Tres tortugas competirán para ver quién llega primero a la meta.")
    print("La meta está a 100 unidades de distancia.")
    print("Cada tortuga avanzará una distancia aleatoria entre 1 y 10 unidades en cada turno.")
    print("¡Que comience la carrera!\n")

    while tortuga1 < meta and tortuga2 < meta and tortuga3 < meta:
        avance1 = random.randint(1, 10)
        avance2 = random.randint(1, 10)
        avance3 = random.randint(1, 10)

        tortuga1 += avance1
        tortuga2 += avance2
        tortuga3 += avance3

        print(f"Tortuga 1 avanzó {avance1} unidades. Total: {tortuga1}")
        print(f"Tortuga 2 avanzó {avance2} unidades. Total: {tortuga2}")
        print(f"Tortuga 3 avanzó {avance3} unidades. Total: {tortuga3}\n")

    if tortuga1 >= meta & tortuga2 >= meta & tortuga3 >= meta:
        print("¡Es un empate entre las tres tortugas!")