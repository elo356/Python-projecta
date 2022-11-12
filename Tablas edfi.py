from tabulate import tabulate
import time
while True:
    #Ejercicios
    print("Escriba nombre de los 8 ejercicios")
    ejercicio_1 = input("1. ")
    ejercicio_2 = input("2. ")
    ejercicio_3 = input("3. ")
    ejercicio_4 = input("4. ")
    ejercicio_5 = input("5. ")
    ejercicio_6 = input("6. ")
    ejercicio_7 = input("7. ")
    ejercicio_8 = input("8. ")
    #Prueba1minuto
    print("Escriba lo que hiso en las pruebas de 1 minuto en orden de como escribio los ejercicios")
    prueba_1 = input("1. ")
    prueba_2 = input("2. ")
    prueba_3 = input("3. ")
    prueba_4 = input("4. ")
    prueba_5 = input("5. ")
    prueba_6 = input("6. ")
    prueba_7 = input("7. ")
    prueba_8 = input("8. ")
    #porcientoATrabajar
    print("Escriba el porciento a trabajar sin el simbolo de %.Debe escribir un decimal por ejemplo 0.40")
    porciento_1 = input("1. ")
    porciento_2 = input("2. ")
    porciento_3 = input("3. ")
    porciento_4 = input("4. ")
    porciento_5 = input("5. ")
    porciento_6 = input("6. ")
    porciento_7 = input("7. ")
    porciento_8 = input("8. ")
    #pruebaAentero
    prueba_1 = int(prueba_1)
    prueba_2 = int(prueba_2)
    prueba_3 = int(prueba_3)
    prueba_4 = int(prueba_4)
    prueba_5 = int(prueba_5)
    prueba_6 = int(prueba_6)
    prueba_7 = int(prueba_7)
    prueba_8 = int(prueba_8)
    #porcientoAflotante
    porciento_1 = float(porciento_1)
    porciento_2 = float(porciento_2)
    porciento_3 = float(porciento_3)
    porciento_4 = float(porciento_4)
    porciento_5 = float (porciento_5)
    porciento_6 = float(porciento_6)
    porciento_7 = float(porciento_7)
    porciento_8 = float(porciento_8)
    #calculoSets
    sets_1 = prueba_1 * porciento_1
    sets_2 = prueba_2 * porciento_2
    sets_3 = prueba_3 * porciento_3
    sets_4 = prueba_4 * porciento_4
    sets_5 = prueba_5 * porciento_5
    sets_6 = prueba_6 * porciento_6
    sets_7 = prueba_7 * porciento_7
    sets_8 = prueba_8 * porciento_8
    #setsAentero
    set_1 = round(sets_1)
    set_2 = round(sets_2)
    set_3 = round(sets_3)
    set_4 = round(sets_4)
    set_5 = round(sets_5)
    set_6 = round(sets_6)
    set_7 = round(sets_7)
    set_8 = round(sets_8)
    #totalsets
    total_1 = set_1 * 3
    total_2 = set_2 * 3
    total_3 = set_3 * 3
    total_4 = set_4 * 3
    total_5 = set_5 * 3
    total_6 = set_6 * 3
    total_7 = set_7 * 3
    total_8 = set_8 * 3
    



    Tabla = [[f"Ejercicios","Prueba 1 minuto","Porciento A trabajar", "Sets 1","Sets 2","Sets 3", "Total"],
            [ejercicio_1, prueba_1, porciento_1, set_1, set_1, set_1, total_1],
            [ejercicio_2, prueba_2, porciento_2, set_2, set_2, set_2, total_2],
            [ejercicio_3, prueba_3, porciento_3, set_3, set_3, set_3, total_3],
            [ejercicio_4, prueba_4, porciento_4, set_4, set_4, set_4, total_4],
            [ejercicio_5, prueba_5, porciento_5, set_5, set_5, set_5, total_5],
            [ejercicio_6, prueba_6, porciento_6, set_6, set_6, set_6, total_6],
            [ejercicio_7, prueba_7, porciento_7, set_7, set_7, set_7, total_7],
            [ejercicio_8, prueba_8, porciento_8, set_8, set_8, set_8, total_8]]
    
    print(tabulate(Tabla, headers = "firstrow"))
    print("Escriba numero de opcion")
    print("1. Volver")
    print("2. Salir")
    vs = input()
    vs = int(vs)
    if vs == 1:
            print("Volviendo...")
            time.sleep(2)
    if vs == 2:
            print("Saliendo...")
            time.sleep(2)
            break
