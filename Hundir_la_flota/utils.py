import numpy as np
import random

def crear_tablero(tamaño=(10,10)):
    return np.full(tamaño, "_")

tablero = crear_tablero()

def crear_barcos(eslora, tamaño_tablero = 10):
    orientacion = random.choice(["horizontal", "vertical"])
    if orientacion == "horizontal":
        fila = random.randint(0, tamaño_tablero -1)
        columna_inicial = random.randint(0, tamaño_tablero - eslora)
        barco = [(fila, columna_inicial + i)for i in range(eslora)]

    else:
        fila_inicial = random.randint(0, tamaño_tablero - eslora)
        columna = random.randint(0, tamaño_tablero - 1)
        barco = [(fila_inicial + i, columna)for i in range(eslora)]

    return barco

lista_flota = [4,3,3,2,2,2]

# La funcion colocar barcos, sirve para evitar que los barcos se solapen
# Primero se recorren las casillas para comprobar que no hay un barco
# Si no hay un barco, marca con O las casillas que estan ocupadas
# Ademas dvuelve una lista con todos los barcos colocados

def colocar_barcos(tablero, lista_flota):
    barcos = []
    for eslora in lista_flota:
        barco_colocado = False
        while not barco_colocado:
            barco = crear_barcos(eslora, len(tablero))
            casillas_libres = True
            for fila, columna in barco:
                if tablero[fila, columna] != "_":
                    casillas_libres = False
                    break
            if casillas_libres: 
                for fila, columna in barco:
                    tablero[fila, columna] = "O"
                barcos.append(barco)
                barco_colocado = True
    return barcos

# El jugador tiene una duncion de disparar introduciendo fila y columna
# Dependiendo de la casilla marca  la casilla como "X" o "A"
def disparar_jugador(casilla, tablero_maquina):
    fila, columna = casilla
    if tablero_maquina [fila, columna] == "O":
        tablero_maquina [fila, columna] = "X"
        return "Tocado" 
    else:
        tablero_maquina[fila, columna] = "A"
        return "Agua"

# La maquina dispara de forma aleatoria a una casilla del tablero del jugador
# Devuelve tocado o agua dependiendo de si habia un barco
def disparar_maquina(tablero_jugador):
    fila = random.randint(0, len(tablero_jugador) - 1)
    columna = random.randint(0, len(tablero_jugador[0]) - 1)
    if tablero_jugador [fila, columna] == "O":
        tablero_jugador [fila, columna] = "X"
        return (fila, columna), "Tocado"
    else:
        tablero_jugador[fila, columna] = "A"
        return (fila, columna), "Agua"

# Compureba si todas las casillas son "X", es decir si el barco esta hundido
def comprobar_barco_hundido(barco, tablero):
    for fila, columna in barco:
        if tablero[fila, columna] != "X":
            return False
    return True

# Comprueba que en un tablero no hayan "O" en ese caso de quien sea el tablero ha perdido

def victoria(tablero):
    return not np.any(tablero == "O")

#Muestra el tablero
def mostrar_tablero(tablero):
    for fila in tablero:
        print(" ".join(fila))
    print()

