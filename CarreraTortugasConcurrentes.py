## Autor: Álvaro Hernández Villarreal

import threading
import random
import time

meta = 100
carrera_ha_terminado = False
mutex1 = threading.Lock()
mutex2 = threading.Lock()

def mover_tortuga():
    return random.randint(0, 10)

def correr_tortuga(nombre_tortuga):
    global carrera_ha_terminado
    distancia_recorrida = 0
    
    while not carrera_ha_terminado:
        
        avance = mover_tortuga()
        distancia_recorrida += avance
        
        with mutex1:
            if not carrera_ha_terminado:
                print(f"{nombre_tortuga}: Avanzó {avance} m. Total: {distancia_recorrida} m")

        if distancia_recorrida >= meta:
            with mutex2:
                if not carrera_ha_terminado:
                    carrera_ha_terminado = True
                    with mutex1:
                        print(f"\n¡¡¡ {nombre_tortuga} ha ganado la carrera !!!\n")
        
        time.sleep(random.uniform(0.1, 0.4))

def main():
    print("¡Bienvenido a la carrera de tortugas!")
    print(f"La meta está a {meta} metros de distancia.\n")

    listaH = []
    nombres_tortugas = ["Tortuga 1", "Tortuga 2", "Tortuga 3"]

    for nombre in nombres_tortugas:
        hilo = threading.Thread(target=correr_tortuga, args=(nombre,))
        listaH.append(hilo)

    for hilo in listaH:
        hilo.start()

    for hilo in listaH:
        hilo.join()

    print("\nLa carrera ha finalizado.")

main()