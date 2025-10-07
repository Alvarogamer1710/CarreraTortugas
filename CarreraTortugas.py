## Autor: Álvaro Hernández Villarreal

import random

def mover_tortuga(): ## Genera un número aleatorio entre 1 y 10 para simular el movimiento de las tortugas
    return random.randint(1, 10)

def main():

    ##Cada tortuga empieza en 0 y la meta está a 100
    tortuga1 = 0
    tortuga2 = 0
    tortuga3 = 0
    meta = 100

    print("¡Bienvenido a la carrera de tortugas!")
    print("Tres tortugas competirán para ver quién llega primero a la meta.")
    print("La meta está a 100 unidades de distancia.")
    print("Cada tortuga avanzará una distancia aleatoria entre 1 y 10 unidades en cada turno.")
    print("¡Que comience la carrera!\n")

    while tortuga1 < meta and tortuga2 < meta and tortuga3 < meta: ## Mientras ninguna tortuga haya llegado a la meta, la carrera continúa
        avance1 = mover_tortuga()
        avance2 = mover_tortuga()
        avance3 = mover_tortuga()

        ## Actualiza la posición de cada tortuga
        tortuga1 += avance1
        tortuga2 += avance2
        tortuga3 += avance3

        print(f"Tortuga 1 avanzó {avance1} metros. Total: {tortuga1} metros")
        print(f"Tortuga 2 avanzó {avance2} metros. Total: {tortuga2} metros")
        print(f"Tortuga 3 avanzó {avance3} metros. Total: {tortuga3} metros\n")

        ## Pausa para simular el tiempo entre turnos
        x = 0
        while x<100000000:
            x+=1

    ## Determina el ganador o si hay empate
    if tortuga1 >= meta & tortuga2 >= meta & tortuga3 >= meta:
        print("¡Es un empate entre las tres tortugas!")
    elif tortuga1 >= meta & tortuga2 >= meta:
        print("¡Es un empate entre la Tortuga 1 y la Tortuga 2!")
    elif tortuga1 >= meta & tortuga3 >= meta:
        print("¡Es un empate entre la Tortuga 1 y la Tortuga 3!")
    elif tortuga2 >= meta & tortuga3 >= meta:
        print("¡Es un empate entre la Tortuga 2 y la Tortuga 3!")
    elif tortuga1 >= meta:
        print("¡La Tortuga 1 gana la carrera!")
    elif tortuga2 >= meta:
        print("¡La Tortuga 2 gana la carrera!")
    else:
        print("¡La Tortuga 3 gana la carrera!")

##Llamada a la función main para iniciar el programa
main()