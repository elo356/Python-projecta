# juegos numeros
import random
import time
intentosRealizados = 0
turnos = 1
print("Bienvenidos a Adivina un juego de adivinar el numero que piensa la maquina. Maximo de 2 a 4 jugadores")

while True:
    while True:
        try:
            canJugadores = int(input("Cantidad Jugadores: "))
            break
        except:
            print("Debe escribir un numero del 2 al 4")
    if canJugadores == 2:
        print("Nombre del primer jugador")
        player1 = input()
        time.sleep(1)
        print("Nombre segundo jugador")
        player2 = input()
        time.sleep(1)
        print(f"{player1} vs. {player2}")
        time.sleep(1)
        print("Dificultad facil o dificil.(Debe escribir numero de opcion)")
        print("1. Facil")
        print("2. Dificil")
        dificultad = int(input())
        if dificultad == 1:
            print("Facil, su estimacion debe ser del 1 al 10")
            maquina = random.randint(1, 10)
            while intentosRealizados < 6:
                print(f"turno {turnos}")
                print(f"Estimacion de {player1}")
                estPlayer1 = input()
                estPlayer1 = int(estPlayer1)
                print(f"Estimacion de {player2}")
                estPlayer2 = input()
                estPlayer2 = int(estPlayer2)

                intentosRealizados = intentosRealizados + 1
                turnos = turnos + 1
                time.sleep(1)
                if estPlayer1 < maquina:
                    print(f"La estimacion de {player1} es baja")
                if estPlayer1 > maquina:
                   print(f"La estimacion de {player1} es alta")
                if estPlayer1 == maquina:
                    if maquina <= 1:
                        print(f"Genial {player1}, ganaste en {intentosRealizados} intento")
                    if maquina > 1:
                        print(f"Genial {player1}, ganaste en {intentosRealizados} intentos")
                    break
                if estPlayer2 < maquina:
                    print(f"La estimacion de {player2} es baja")
                if estPlayer2 > maquina:
                    print(f"La estimacion de {player2} es alta")
                if estPlayer2 == maquina:
                    if maquina <= 1:
                        print(f"Genial {player2}, ganaste en {intentosRealizados} intento")
                    if maquina > 1:
                        print(f"Genial {player2}, ganaste en {intentosRealizados} intentos")
                    break
            if estPlayer1 != maquina:
                print(f"Lo siento {player1} perdiste, la respuesta era {maquina}")
            if estPlayer2 != maquina:
                print(f"Lo siento {player2} perdiste, la respuesta era {maquina}")

        if dificultad == 2:
            print("Dificil, su estimacion deber ser del 1 al 20")
            maquina = random.randint(1, 20)
            while intentosRealizados < 10:
                print(f"turno {turnos}")
                print(f"Estimacion de {player1}")
                estPlayer1 = input()
                estPlayer1 = int(estPlayer1)
                print(f"Estimacion de {player2}")
                estPlayer2 = input()
                estPlayer2 = int(estPlayer2)
                intentosRealizados = intentosRealizados + 1
                turnos = turnos + 1
                time.sleep(1)
                if estPlayer1 < maquina:
                    print(f"La estimacion de {player1} es baja")
                if estPlayer1 > maquina:
                    print(f"La estimacion de {player1} es alta")
                if estPlayer1 == maquina:
                    if maquina <= 1:
                        print(f"Genial {player1}, ganaste en {intentosRealizados} intento")
                    if maquina > 1:
                        print(f"Genial {player1}, ganaste en {intentosRealizados} intentos")
                    break
                if estPlayer2 < maquina:
                    print(f"La estimacion de {player2} es baja")
                if estPlayer2 > maquina:
                    print(f"La estimacion de {player2} es alta")
                if estPlayer2 == maquina:
                    if maquina <= 1:
                        print(f"Genial {player2}, ganaste en {intentosRealizados} intento")
                    if maquina > 1:
                        print(f"Genial {player2}, ganaste en {intentosRealizados} intentos")
                    break
            if estPlayer1 != maquina:
                print(f"Lo siento {player1} perdiste, la respuesta era {maquina}")
            if estPlayer2 != maquina:
                print(f"Lo siento {player2} perdiste, la respuesta era {maquina}")

    if canJugadores == 3:
        print("Nombre del primer jugador")
        player1 = input()
        time.sleep(1)
        print("Nombre segundo jugador")
        player2 = input()
        time.sleep(1)
        print("Nombre tercer jugador")
        player3 = input()
        print(f"{player1} vs. {player2} vs. {player3}")
        time.sleep(1)
        print("Dificultad facil o dificil.(Debe escribir numero de opcion)")
        print("1. Facil")
        print("2. Dificil")
        dificultad = int(input())
        if dificultad == 1:
            print("Facil, su estimacion debe ser del 1 al 10")
            maquina = random.randint(1, 10)
            while intentosRealizados < 6:
                print(f"turno {turnos}")
                print(f"Estimacion de {player1}")
                estPlayer1 = input()
                estPlayer1 = int(estPlayer1)
                print(f"Estimacion de {player2}")
                estPlayer2 = input()
                estPlayer2 = int(estPlayer2)
                print(f"Estimacion de {player3}")
                estPlayer3 = input()
                estPlayer3 = int(estPlayer3)
                time.sleep(1)
                intentosRealizados = intentosRealizados + 1
                turnos = turnos + 1
                time.sleep(1)
                if estPlayer1 < maquina:
                    print(f"La estimacion de {player1} es baja")
                if estPlayer1 > maquina:
                    print(f"La estimacion de {player1} es alta")
                if estPlayer1 == maquina:
                    if maquina <= 1:
                        print(f"Genial {player1}, ganaste en {intentosRealizados} intento")
                    if maquina > 1:
                        print(f"Genial {player1}, ganaste en {intentosRealizados} intentos")
                    break
                if estPlayer2 < maquina:
                    print(f"La estimacion de {player2} es baja")
                if estPlayer2 > maquina:
                    print(f"La estimacion de {player2} es alta")
                if estPlayer2 == maquina:
                    if maquina <= 1:
                        print(f"Genial {player2}, ganaste en {intentosRealizados} intento")
                    if maquina > 1:
                        print(f"Genial {player2}, ganaste en {intentosRealizados} intentos")
                    break
                if estPlayer3 < maquina:
                    print(f"La estimacion de {player3} es baja")
                if estPlayer3 > maquina:
                    print(f"La estimacion de {player3} es alta")
                if estPlayer3 == maquina:
                    if maquina <= 1:
                        print(f"Genial {player3}, ganaste en {intentosRealizados} intento")
                if maquina > 1:
                    print(f"Genial {player3}, ganaste en {intentosRealizados} intentos")
                    break
            if estPlayer1 != maquina:
                 print(f"Lo siento {player1} perdiste, la respuesta era {maquina}")
            if estPlayer2 != maquina:
                print(f"Lo siento {player2} perdiste, la respuesta era {maquina}")
            if estPlayer3 != maquina:
                print(f"Lo siento {player3} perdiste, la respuesta era {maquina}")

        if dificultad == 2:
            print("Dificil, su estimacion deber ser del 1 al 20")
            maquina = random.randint(1, 20)
            while intentosRealizados < 6:
                print(f"turno {turnos}")
                print(f"Estimacion de {player1}")
                estPlayer1 = input()
                estPlayer1 = int(estPlayer1)
                print(f"Estimacion de {player2}")
                estPlayer2 = input()
                estPlayer2 = int(estPlayer2)
                print(f"Estimacion de {player3}")
                estPlayer3 = input()
                estPlayer3 = int(estPlayer3)
                time.sleep(1)
                intentosRealizados = intentosRealizados + 1
                turnos = turnos + 1
                time.sleep(1)
                if estPlayer1 < maquina:
                    print(f"La estimacion de {player1} es baja")
                if estPlayer1 > maquina:
                    print(f"La estimacion de {player1} es alta")
                if estPlayer1 == maquina:
                    if maquina <= 1:
                        print(f"Genial {player1}, ganaste en {intentosRealizados} intento")
                    if maquina > 1:
                        print(f"Genial {player1}, ganaste en {intentosRealizados} intentos")
                    break
                if estPlayer2 < maquina:
                    print(f"La estimacion de {player2} es baja")
                if estPlayer2 > maquina:
                    print(f"La estimacion de {player2} es alta")
                if estPlayer2 == maquina:
                    if maquina <= 1:
                        print(f"Genial {player2}, ganaste en {intentosRealizados} intento")
                    if maquina > 1:
                        print(f"Genial {player2}, ganaste en {intentosRealizados} intentos")
                    break
                if estPlayer3 < maquina:
                    print(f"La estimacion de {player3} es baja")
                if estPlayer3 > maquina:
                    print(f"La estimacion de {player3} es alta")
                if estPlayer3 == maquina:
                    if maquina <= 1:
                        print(f"Genial {player3}, ganaste en {intentosRealizados} intento")
                    if maquina > 1:
                        print(f"Genial {player3}, ganaste en {intentosRealizados} intentos")
                    break
            if estPlayer1 != maquina:
                print(f"Lo siento {player1} perdiste, la respuesta era {maquina}")
            if estPlayer2 != maquina:
                print(f"Lo siento {player2} perdiste, la respuesta era {maquina}")
            if estPlayer3 != maquina:
                print(f"Lo siento {player3} perdiste, la respuesta era {maquina}")

    if canJugadores == 4:
        print("Nombre del primer jugador")
        player1 = input()
        time.sleep(1)
        print("Nombre segundo jugador")
        player2 = input()
        time.sleep(1)
        print("Nombre tercer jugador")
        player3 = input()
        print("Nombre cuarto jugador")
        player4 = input()
        print(f"{player1} vs. {player2} vs. {player3} vs. {player4}")
        time.sleep(1)
        print("Dificultad facil o dificil.(Debe escribir numero de opcion)")
        print("1. Facil")
        print("2. Dificil")
        dificultad = int(input())
        if dificultad == 1:
            print("Facil, su estimacion debe ser del 1 al 10")
            maquina = random.randint(1, 10)
            while intentosRealizados < 10:
                print(f"turno {turnos}")
                print(f"Estimacion de {player1}")
                estPlayer1 = input()
                estPlayer1 = int(estPlayer1)
                print(f"Estimacion de {player2}")
                estPlayer2 = input()
                estPlayer2 = int(estPlayer2)
                print(f"Estimacion de {player3}")
                estPlayer3 = input()
                estPlayer3 = int(estPlayer3)
                print(f"Estimacion de {player4}")
                estPlayer4 = input()
                estPlayer4 = int(estPlayer4)
                time.sleep(1)
                intentosRealizados = intentosRealizados + 1
                turnos = turnos + 1
                time.sleep(1)
                if estPlayer1 < maquina:
                    print(f"La estimacion de {player1} es baja")
                if estPlayer1 > maquina:
                    print(f"La estimacion de {player1} es alta")
                if estPlayer1 == maquina:
                    if maquina <= 1:
                        print(f"Genial {player1}, ganaste en {intentosRealizados} intento")
                    if maquina > 1:
                        print(f"Genial {player1}, ganaste en {intentosRealizados} intentos")
                    break
                if estPlayer2 < maquina:
                    print(f"La estimacion de {player2} es baja")
                if estPlayer2 > maquina:
                    print(f"La estimacion de {player2} es alta")
                if estPlayer2 == maquina:
                    if maquina <= 1:
                        print(f"Genial {player2}, ganaste en {intentosRealizados} intento")
                    if maquina > 1:
                        print(f"Genial {player2}, ganaste en {intentosRealizados} intentos")
                    break
                if estPlayer3 < maquina:
                    print(f"La estimacion de {player3} es baja")
                if estPlayer3 > maquina:
                    print(f"La estimacion de {player3} es alta")
                if estPlayer3 == maquina:
                    if maquina <= 1:
                        print(f"Genial {player3}, ganaste en {intentosRealizados} intento")
                    if maquina > 1:
                        print(f"Genial {player3}, ganaste en {intentosRealizados} intentos")
                    break
                if estPlayer4 < maquina:
                    print(f"La estimacion de {player4} es baja")
                if estPlayer4 > maquina:
                    print(f"La estimacion de {player4} es alta")
                if estPlayer4 == maquina:
                    if maquina <= 1:
                        print(f"Genial {player4}, ganaste en {intentosRealizados} intento")
                    if maquina > 1:
                        print(f"Genial {player4}, ganaste en {intentosRealizados} intentos")
                    break
            if estPlayer1 != maquina:
                print(f"Lo siento {player1} perdiste, la respuesta era {maquina}")
            if estPlayer2 != maquina:
                print(f"Lo siento {player2} perdiste, la respuesta era {maquina}")
            if estPlayer3 != maquina:
                print(f"Lo siento {player3} perdiste, la respuesta era {maquina}")
            if estPlayer4 != maquina:
                print(f"Lo siento {player4} perdiste, la respuesta era {maquina}")

        if dificultad == 2:
            print("Dificil, su estimacion deber ser del 1 al 20")
            maquina = random.randint(1, 20)
            while intentosRealizados < 6:
                print(f"turno {turnos}")
                print(f"Estimacion de {player1}")
                estPlayer1 = input()
                estPlayer1 = int(estPlayer1)
                print(f"Estimacion de {player2}")
                estPlayer2 = input()
                estPlayer2 = int(estPlayer2)
                print(f"Estimacion de {player3}")
                estPlayer3 = input()
                estPlayer3 = int(estPlayer3)
                print(f"Estimacion de {player4}")
                estPlayer4 = input()
                estPlayer4 = int(estPlayer4)
                time.sleep(1)
                intentosRealizados = intentosRealizados + 1
                turnos = turnos + 1
                time.sleep(1)
                if estPlayer1 < maquina:
                    print(f"La estimacion de {player1} es baja")
                if estPlayer1 > maquina:
                    print(f"La estimacion de {player1} es alta")
                if estPlayer1 == maquina:
                    if maquina <= 1:
                        print(f"Genial {player1}, ganaste en {intentosRealizados} intento")
                    if maquina > 1:
                        print(f"Genial {player1}, ganaste en {intentosRealizados} intentos")
                    break
                if estPlayer2 < maquina:
                    print(f"La estimacion de {player2} es baja")
                if estPlayer2 > maquina:
                    print(f"La estimacion de {player2} es alta")
                if estPlayer2 == maquina:
                    if maquina <= 1:
                        print(f"Genial {player2}, ganaste en {intentosRealizados} intento")
                    if maquina > 1:
                        print(f"Genial {player2}, ganaste en {intentosRealizados} intentos")
                    break
                if estPlayer3 < maquina:
                    print(f"La estimacion de {player3} es baja")
                if estPlayer3 > maquina:
                    print(f"La estimacion de {player3} es alta")
                if estPlayer3 == maquina:
                    if maquina <= 1:
                        print(f"Genial {player3}, ganaste en {intentosRealizados} intento")
                    if maquina > 1:
                        print(f"Genial {player3}, ganaste en {intentosRealizados} intentos")
                    break
                if estPlayer4 < maquina:
                    print(f"La estimacion de {player4} es baja")
                if estPlayer4 > maquina:
                    print(f"La estimacion de {player4} es alta")
                if estPlayer4 == maquina:
                    if maquina <= 1:
                        print(f"Genial {player4}, ganaste en {intentosRealizados} intento")
                    if maquina > 1:
                        print(f"Genial {player4}, ganaste en {intentosRealizados} intentos")
                    break
            if estPlayer1 != maquina:
                print(f"Lo siento {player1} perdiste, la respuesta era {maquina}")
            if estPlayer2 != maquina:
                print(f"Lo siento {player2} perdiste, la respuesta era {maquina}")
            if estPlayer3 != maquina:
                print(f"Lo siento {player3} perdiste, la respuesta era {maquina}")
            if estPlayer4 != maquina:
                print(f"Lo siento {player4} perdiste, la respuesta era {maquina}")

    if canJugadores > 4:
        print("Lo siento solo pueden jugar un maximo de 4 jugadores")
    if canJugadores <= 1:
        print("Los siento solo se puede jugar de  2 a 4 jugadores")
    print("Escriba numero de opcion")
    print("1. Volver a jugar")
    print("2. Salir")
    volver = input()
    volver = int(volver)
    time.sleep(1)
    if volver == 1:
        print("Reiniciando...")
        time.sleep(1)
        print("Reiniciando.")
        time.sleep(1)
        time.sleep(1)
        print("Reiniciado...")
        time.sleep(1)
    if volver == 2:
        print("Saliendo")
        break
