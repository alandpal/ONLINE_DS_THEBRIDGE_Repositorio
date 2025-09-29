from utils import *

# He intentado hacer la logica del juego pero no me daba tiempo y la he copiado de internet
# solo era para ver si funcionaba y para entregar el ejercicio

# Los utils si que lo he ido haciendo yo, pero hay un punto donde me he perdido y he tenido 
# que ir haciendo pequeños retoques

tablero_jugador = crear_tablero()
tablero_maquina = crear_tablero()

barcos_jugador = colocar_barcos(tablero_jugador, lista_flota)
barcos_maquina = colocar_barcos(tablero_maquina, lista_flota)

turno = "jugador"
juego_terminado = False

while not juego_terminado:
    mostrar_tablero(tablero_jugador)

    if turno == "jugador":
        fila = int(input("Elige fila (0-9): "))
        columna = int(input("Elige columna (0-9): "))
        resultado = disparar_jugador((fila, columna), tablero_maquina)
        print("Resultado del disparo:", resultado)
        
        if victoria(tablero_maquina):
            print("¡Has ganado!")
            juego_terminado = True
        else:
            turno = "maquina"
        
    else:
        casilla, resultado = disparar_maquina(tablero_jugador)
        print(f"La máquina dispara a {casilla} -> {resultado}")

        if victoria(tablero_jugador):
            print("La máquina ha ganado...")
            juego_terminado = True
        else:
            turno = "jugador"

