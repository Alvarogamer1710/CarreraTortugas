## Autor: Álvaro Hernández Villarreal

import random
import time
import threading

tablero = []
contador_caca = []

ancho = 0
alto = 0

juego_terminado = False

mutex_global = threading.Lock()

def imprimir_tablero():
    print("---Vacas y Cacas---")
    
    mutex_global.acquire()
    
    i = 0
    while i < len(tablero):
        print(' '.join(tablero[i]))
        i = i + 1
        
    mutex_global.release()
    print("----------------------------")

def vivir_vaca(vaca_id):
    global tablero, contador_caca, juego_terminado
    
    char_vaca = 'V'
    
    y = random.randint(0, alto - 1)
    x = random.randint(0, ancho - 1)
    
    mutex_global.acquire()
    tablero[y][x] = char_vaca
    mutex_global.release()
    
    movimientos_desde_caca = 0
    
    esta_vivo = True
    while esta_vivo:
        
        time.sleep(random.uniform(0.5, 1.0))
        
        direccion = random.randint(1, 4)
        y_nueva = y
        x_nueva = x
        
        if direccion == 1: 
            y_nueva = y - 1
        elif direccion == 2: 
            x_nueva = x + 1
        elif direccion == 3: 
            y_nueva = y + 1
        elif direccion == 4: 
            x_nueva = x - 1
            
        mutex_global.acquire()
        
        if not juego_terminado:
            
            if (0 <= y_nueva < alto) and (0 <= x_nueva < ancho):
                
                movimientos_desde_caca = movimientos_desde_caca + 1
                
                dejar_atras = ' ' 
                
                if movimientos_desde_caca == 5:
                    movimientos_desde_caca = 0
                    dejar_atras = 'C' 
                    contador_caca[y][x] = 7
                
                tablero[y][x] = dejar_atras
                
                y = y_nueva
                x = x_nueva
                
                tablero[y][x] = char_vaca
        
        if juego_terminado:
            esta_vivo = False
            
        mutex_global.release()


def main():
    global tablero, contador_caca, ancho, alto, juego_terminado
    
    ancho = int(input("Introduce el ancho del terreno: "))
    alto = int(input("Introduce el alto del terreno: "))
    num_vacas = int(input("Introduce el numero de vacas: "))

    y = 0
    while y < alto:
        fila_tablero = []
        fila_caca = []
        x = 0
        while x < ancho:
            fila_tablero.append('"')
            fila_caca.append(0)
            x = x + 1
        tablero.append(fila_tablero)
        contador_caca.append(fila_caca)
        y = y + 1

    lista_hilos = []
    i = 0
    while i < num_vacas:
        hilo = threading.Thread(target=vivir_vaca, args=(i,))
        lista_hilos.append(hilo)
        hilo.start()
        i = i + 1

    while not juego_terminado:
        
        imprimir_tablero()
        
        mutex_global.acquire()
        
        hay_hierba = False
        y = 0
        while y < alto:
            x = 0
            while x < ancho:
                
                if contador_caca[y][x] > 0:
                    contador_caca[y][x] = contador_caca[y][x] - 1
                    
                    if contador_caca[y][x] == 0:
                        if tablero[y][x] == 'C':
                            tablero[y][x] = '"'
                
                if tablero[y][x] == '"':
                    hay_hierba = True
                    
                x = x + 1
            y = y + 1
        
        if not hay_hierba:
            juego_terminado = True
        
        mutex_global.release()
        
        time.sleep(random.randint(1, 3))

    imprimir_tablero()
    print("\n¡JUEGO TERMINADO! La vaca se comio toda la hierba.")

    i = 0
    while i < len(lista_hilos):
        lista_hilos[i].join()
        i = i + 1

    print("Todas las vacas han terminado.")

main()