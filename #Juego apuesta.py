#Programa juego apuesta
import random
import time
cantDerrotasPlayer1 = 0
cantDerrotasPlayer2 = 0
cantDerrotasPlayer3 = 0
cantDerrotasPlayer4 = 0
cantVictoriasPlayer1 = 0
cantVictoriasPlayer2 = 0
cantVictoriasPlayer3 = 0
cantVictoriasPlayer4 = 0
dineroPlayer1 = 1000
dineroPlayer2 = 1000
dineroPlayer3 = 1000
dineroPlayer4 = 1000
rondas = 0
while True:
    print("Bienvenidos al juego de apuesta por la maquina, tendras $1000 y deberas apostar por el numero que piensas que la maquina piensa, despues de 10 rondas el que mas dinero tenga gana. Cada ronda el numero sera diferente.")
    while True:
        try:
            cantJugadores = int(input("Cantidad de Jugadores: "))
            break
        except:
            print("Debe escribir un numero entero del 1 al 4")
    if cantJugadores < 2:
        print("No se puede jugar con menos de 2 jugadores")
        print("Escriba numero de opcion: ")
        print("1. Volver")
        print("2. Salir")
        opciones = input()
        opciones = int(opciones)
        if opciones == 1:
            print("Volviendo")
            time.sleep(1)
        if opciones == 2:        
            break
    if cantJugadores > 4:
        print("No se puede jugar con mas de 4 jugadores")
        print("Escriba numero de opcion: ")
        print("1. Volver")
        print("2. Salir")
        opciones = input()
        opciones = int(opciones)
        if opciones == 1:
            print("Volviendo")
            time.sleep(1)
        if opciones == 2:        
            break
    if cantJugadores == 2:
        print("A jugar!! para ganar debes tener mas dinero que el otro jugador al terminar la ronda 10")
        #obtener nombre de player1
        print("Nombre del primer jugador")
        player1 = input()
        #obtener nombre de player2
        print("Nombre del segundo jugador")
        player2 = input()
        print(f"{player1} vs. {player2}")
        #iniciar rondas 
        time.sleep(1)
        while rondas < 10:
            if dineroPlayer1 <= 1:
                break
            if dineroPlayer2 <= 1:
                break
            maquina = random.randint(1, 10)
            rondas = rondas + 1   
            #obtener estimacion de player1            
            print(f"Estimacion de {player1}")
            estPlayer1 = input()
            estPlayer1 = int(estPlayer1)
            #obtener estimacion de player2
            print(f"Estimacion de {player2}")
            estPlayer2 = input()
            estPlayer2 = int(estPlayer2)
            time.sleep(1)
            #obtener apuesta de player1
            print(f"Cantidad de apuesta de {player1}")
            cantApuestaPlayer1 = input()
            #restar cantidad de apuesta de player1
            cantApuestaPlayer1 = int(cantApuestaPlayer1)
            dineroPlayer1 = dineroPlayer1 - cantApuestaPlayer1
            #obtener apuesta de player2
            print(f"Cantidad de apuesta de {player2}")
            cantApuestaPlayer2 = input()
            cantApuestaPlayer2 = int(cantApuestaPlayer2)
            #restar cantidad de apuesta de player2
            dineroPlayer2 = dineroPlayer2 - cantApuestaPlayer2
             #Sumar la cantidad total de la apuesta de ambos jugadores
            cantApuestaTotal = cantApuestaPlayer1 + cantApuestaPlayer2
            #verificar si algun jugador gano la ronda
            #ver si player1 gano la ronda actual o la perdio y si gano sumarle cantidad total de apuesta
            if estPlayer1 == maquina:
                print(f"{player1} gano la ronda {rondas}")
                #sumar cantidad total de apuesta
                dineroPlayer1 = dineroPlayer1 + cantApuestaTotal
            else:
                print(f"{player1} perdio la ronda {rondas}")
            #ver si player2 gano la ronda actual o la perdio y si gano sumarle la cantidad total de apuesta
            if estPlayer2 == maquina:
                print(f"{player2} gano la ronda")
                #sumar cantidad total de apuesta
                dineroPlayer2 = dineroPlayer2 + cantApuestaTotal
            else:
                print(f"{player2} perdio la ronda")
            print(f"{player1} su cantidad de dinero actual es de ${dineroPlayer1}")
            print(f"{player2} su cantidad de dinero actual es de ${dineroPlayer2}")
        #verificar quien gano
        #empate player1
        if dineroPlayer1 == dineroPlayer2:
            print(f"{player1} fue una empate!! ;D")
        #gana player1
        if dineroPlayer1 > dineroPlayer2:
            print(f"{player1} fue una victoria!! :)")
        #pierde player1
        if dineroPlayer1 < dineroPlayer2:
            print(f"{player1} fue una derrota!! :(")
        #empate player2
        if dineroPlayer2 == dineroPlayer1:
            print(f"{player2} fue una empate!! ;D")
        #gana player2
        if dineroPlayer2 > dineroPlayer1:
            print(f"{player2} fue una victoria!! :)")
        #pierde player2
        if dineroPlayer2 < dineroPlayer1:
            print(f"{player2} fue una derrota!! :(")
        time.sleep(3)
        print(f"{player1} su dinero total es de ${dineroPlayer1}")
        print(f"{player2} su dinero total es de ${dineroPlayer2}")
        print("Escriba numero de opcion")
        print("1. Volver")
        print("2. Salir")
        end = input()
        end = int(end)
        if end == 1:
            print("Volviendo...")
            time.sleep(1)
        if end == 2: 
            print("Saliendo...")
            time.sleep(1)

        
        