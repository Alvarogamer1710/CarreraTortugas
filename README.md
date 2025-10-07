# Carrera de Tortugas

Código creado por el alumno Álvaro Hernández Villarreal de la Universidad Europea de Madrid (UEM).

Este repositorio contiene un script en Python (`CarreraTortugas.py`) que simula una carrera entre tres tortugas. En cada turno (sprint) cada tortuga avanza una distancia aleatoria entre 1 y 10 unidades hasta que alguna alcanza la meta.

## Contenido
- `CarreraTortugas.py`: script principal que ejecuta la simulación.
- `README.md`: este archivo con instrucciones.

## Requisitos
- Python 3.x instalado.

## Cómo ejecutar
1. Abre una terminal (por ejemplo PowerShell en Windows).
2. Ejecuta el script:

```powershell
python "c:\Users\Usuario\Desktop\Tortugas\CarreraTortugas.py"
```

## Descripción del comportamiento
- Inicializa las posiciones de tres tortugas en 0 y una meta a 100 unidades.
- En cada iteración, cada tortuga avanza una distancia aleatoria entre 1 y 10 unidades.
- Muestra en consola cuánto avanzó cada tortuga y su total acumulado.
- Cuando al menos una tortuga alcanza la meta, el script termina y muestra el/los ganador(es).

## Personalización rápida
- Cambiar la distancia de la meta: modifica la variable `meta` en `CarreraTortugas.py`.
- Cambiar el rango de avance por sprint: modifica la función `mover_tortuga()` (por ejemplo `random.randint(1, 5)`).
- Añadir un contador de sprints: puedes añadir un contador y mostrarlo por iteración. Si quieres, lo puedo añadir al script.
- Pausas entre sprints: evita usar bucles que consumen CPU (busy-wait). Usa `time.sleep(segundos)` para pausas sencillas. Si usas una GUI como `turtle`, usa `Screen().ontimer`.

## Notas
- El script original puede contener una espera activa (busy-wait) que consume mucha CPU. Es recomendable reemplazarla por `time.sleep()` para pausas.

## Autor y licencia
- Autor: Álvaro Hernández Villarreal
- Uso educativo.