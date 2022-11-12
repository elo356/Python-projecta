#IA para buscar area y perimetro de figura
import time
#Area
baseTriangulo = None
baseCuadrado = None
baseTrapecio1 = None
baseTrapecio2 = None
alturaTriangulo = None
alturaTrapecio = None
alturaCuadrado = None
circurferenciaCirculo = None
#Perimetro
ladoCuadrado = None
ladoTriangulo1 = None
ladoTriangulo2 = None
ladoTriangulo3 = None
ladoTrapecio1 = None
baseMenorTrapecio = None
baseMsyorTrapecio = None
#figura1
def Circulo1():
    print(f"{name}, eliguiste Circulo")
        while True:
            try:
                Circurferencia = float(input("Circurferencia del circulo: "))
                break
            except:
                print("Debe escribir un numero")


      
     
        figura1 = (Circurferencia * Circurferencia) * 3.14

        print(f"Bueno {name} segun la informacion que me diste el area del Circulo es {figura1}")
        return
def Triangulo1():
     print(f"{name}, eliguiste Triangulo")
        while True:
            try:
                baseTriangulo = float(input("Base del Triangulo: "))
                break
            except:
                print("Debe escribir un numero")


        while True:
            try:
                alturaTriangulo = float(input("Altura del Triangulo: "))
                break
            except:
                print("Debe escribir un numero")
            
     
        figura1 = baseTriangulo * alturaTriangulo / 2

        print(f"Bueno {name} segun la informacion que me diste el area del Triangulo es {figua1}")
        return
def Trapecio1():
    print(f"{name}, eleguiste Trapecio")
        while True:
            try:
                baseTrapecio1 = float(input("Base mayor del Trapecio: "))
                break
            except:
                print("Debe escribir un numero")

        while True:
            try:
                baseTrapecio2 = float(input("Base menor del Trapecio: "))
                break
            except:
                print("Debe escribir un numero")


        while True:
            try:
                alturaTrapecio = float(input("Altura del Trapecio: "))
                break
            except:
                print("Debe escribir un numero")
            
     
        figura1 = (baseTrapecio1 + baseTrapecio2) * alturaTrapecio / 2

        print(f"Bueno {name} segun la informacion que me diste el area del Trapecio es {figura1}")
        return
def Cuadrado1():
    print(f"{name}, eleguiste Cuadrado")
        while True:
            try:
                baseCuadrado = float(input("Base del Cuadrado: "))
                break
            except:
                print("Debe escribir un numero")


        while True:
            try:
                alturaCuadrado = float(input("Altura del Cuadrado: "))
                break
            except:
                print("Debe escribir un numero")
            
     
        figura1 = baseCuadrado * alturaCuadrado

        print(f"Bueno {name} segun la informacion que me diste el area del Cuadrado es {figura1}")
        return
#figura 2
def Circulo2():
    print(f"{name}, eliguiste Circulo")
        while True:
            try:
                Circurferencia = float(input("Circurferencia del circulo: "))
                break
            except:
                print("Debe escribir un numero")


      
     
        figura2 = (Circurferencia * Circurferencia) * 3.14

        print(f"Bueno {name} segun la informacion que me diste el area del Circulo es {figura2}")
        return
def Triangulo2():
     print(f"{name}, eliguiste Triangulo")
        while True:
            try:
                baseTriangulo = float(input("Base del Triangulo: "))
                break
            except:
                print("Debe escribir un numero")


        while True:
            try:
                alturaTriangulo = float(input("Altura del Triangulo: "))
                break
            except:
                print("Debe escribir un numero")
            
     
        figura2 = baseTriangulo * alturaTriangulo / 2

        print(f"Bueno {name} segun la informacion que me diste el area del Triangulo es {figura2}")
        return
def Trapecio2():
    print(f"{name}, eleguiste Trapecio")
        while True:
            try:
                baseTrapecio1 = float(input("Base mayor del Trapecio: "))
                break
            except:
                print("Debe escribir un numero")

        while True:
            try:
                baseTrapecio2 = float(input("Base menor del Trapecio: "))
                break
            except:
                print("Debe escribir un numero")


        while True:
            try:
                alturaTrapecio = float(input("Altura del Trapecio: "))
                break
            except:
                print("Debe escribir un numero")
            
     
        figura2 = (baseTrapecio1 + baseTrapecio2) * alturaTrapecio / 2

        print(f"Bueno {name} segun la informacion que me diste el area del Trapecio es {figura2}")
        return
def Cuadrado2():
    print(f"{name}, eleguiste Cuadrado")
        while True:
            try:
                baseCuadrado = float(input("Base del Cuadrado: "))
                break
            except:
                print("Debe escribir un numero")


        while True:
            try:
                alturaCuadrado = float(input("Altura del Cuadrado: "))
                break
            except:
                print("Debe escribir un numero")
            
     
        figura2 = baseCuadrado * alturaCuadrado

        print(f"Bueno {name} segun la informacion que me diste el area del Cuadrado es {figura2}")
        return
#Buscar Area
def Area():
    print(f"Perfecto {name} eligiste buscar area. Ecribe el numero de la figura que quiere resolver")
    print("1. Cuadrado")
    print("2. Triangulo")
    print("3. Trapecio")
    print("4. Circulo")
    while True:
        try:
            figura = int(input("Numero de opcion: "))
            break
        except:
            print("Debe escribir un numero de opcion")
    #Cuadrado
    if figura == 1:
        print(f"{name}, eleguiste Cuadrado")
        while True:
            try:
                baseCuadrado = float(input("Base del Cuadrado: "))
                break
            except:
                print("Debe escribir un numero")


        while True:
            try:
                alturaCuadrado = float(input("Altura del Cuadrado: "))
                break
            except:
                print("Debe escribir un numero")
            
     
        areaCuadrado = baseCuadrado * alturaCuadrado

        print(f"Bueno {name} segun la informacion que me diste el area del Cuadrado es {areaCuadrado}")
        return
        
    #Triangulo
    if figura == 2:
        print(f"{name}, eliguiste Triangulo")
        while True:
            try:
                baseTriangulo = float(input("Base del Triangulo: "))
                break
            except:
                print("Debe escribir un numero")


        while True:
            try:
                alturaTriangulo = float(input("Altura del Triangulo: "))
                break
            except:
                print("Debe escribir un numero")
            
     
        areaTriangulo = baseTriangulo * alturaTriangulo / 2

        print(f"Bueno {name} segun la informacion que me diste el area del Triangulo es {areaTriangulo}")
        return
    #Trapecio
    if figura == 3:
        print(f"{name}, eleguiste Trapecio")
        while True:
            try:
                baseTrapecio1 = float(input("Base mayor del Trapecio: "))
                break
            except:
                print("Debe escribir un numero")

        while True:
            try:
                baseTrapecio2 = float(input("Base menor del Trapecio: "))
                break
            except:
                print("Debe escribir un numero")


        while True:
            try:
                alturaTrapecio = float(input("Altura del Trapecio: "))
                break
            except:
                print("Debe escribir un numero")
            
     
        areaTrapecio = (baseTrapecio1 + baseTrapecio2) * alturaTrapecio / 2

        print(f"Bueno {name} segun la informacion que me diste el area del Trapecio es {areaTrapecio}")
        return
    #circulo
    if figura == 4:
        print(f"{name}, eliguiste Circulo")
        while True:
            try:
                Circurferencia = float(input("Circurferencia del circulo: "))
                break
            except:
                print("Debe escribir un numero")


      
     
        areaCirculo = (Circurferencia * Circurferencia) * 3.14

        print(f"Bueno {name} segun la informacion que me diste el area del Circulo es {areaCirculo}")
        return
#Termian area
#Buscar perimetro
def Permimetro():
    print(f"Perfecto {name} eligiste buscar perimetro. Ecribe el numero de la figura que quiere resolver")
    print("1. Cuadrado")
    print("2. Triangulo")
    print("3. Trapecio")
    while True:
        try:
            figura = int(input("Numero de opcion: "))
            break
        except:
            print("Debe escribir un numero de opcion")
    if figura == 1:
        print(f"{name}, eleguiste Cuadrado")
        while True:
            try:
                ladoCuadrado = float(input("lado del Cuadrado: "))
                break
            except:
                print("Debe escribir un numero")

            
     
        perimetroCuadrado = ladoCuadrado * 4

        print(f"Bueno {name} segun la informacion que me diste el perimetro del Cuadrado es {perimetroCuadrado}")
        return

    if figura == 2:
        print(f"{name}, eleguiste Triangulo")
        while True:
            try:
                ladoTriangulo1 = float(input("lado izquierdo del Triangulo: "))
                break
            except:
                print("Debe escribir un numero")
                
        while True:
            try:
                ladoTriangulo2 = float(input("lado derecho del Triangulo: "))
                break
            except:
                print("Debe escribir un numero")

        while True:
            try:
                ladoTriangulo3 = float(input("lado bajo del Triangulo: "))
                break
            except:
                print("Debe escribir un numero")

            
     
        perimetroTriangulo = ladoTriangulo1 + ladoTriangulo2 + ladoTriangulo3

        print(f"Bueno {name} segun la informacion que me diste el perimetro del Triangulo es {perimetroTriangulo}")
        return

    if figura == 3:
        print(f"{name}, eleguiste Trapecio")
        while True:
            try:
                ladoMayorTrapecio = float(input("Lado mayor del Trapecio: "))
                break
            except:
                print("Debe escribir un numero")
                
        while True:
            try:
                ladoMenorTrapecio = float(input("Lado menor del Trapecio: "))
                break
            except:
                print("Debe escribir un numero")

        while True:
            try:
                ladoTrapecio1 = float(input("Lado del Trapecio: "))
                break
            except:
                print("Debe escribir un numero")

        perimetroTrapecio = ladoMenorTrapecio + ladoMayorTrapecio + ladoTrapecio1 + ladoTrapecio1

        print(f"Bueno {name} segun la informacion que me diste el perimetro del Trapecio es {perimetroTrapecio}")
        return
        

#Termina perimetro
#Inicio del programa
print("Bienvenidos a Ari una ia que resuelve ejercicios de area y perimetro por ti")
name = input("Como se llama: ")
print("Escribe numero de opcion de lo que desea buscar")
print("1. Area")
print("2. Perimetro")
print("3. Varias Figuras en una")
while True:
    try:
        QueBuscar = int(input("Numero de opcion: "))
        break
    except:
        print("Debe escribir un numero de opcion")

if  QueBuscar == 1:
    Area()
if QueBuscar == 2:
    Permimetro()
       
if QueBuscar == 3:
    print("1. Cuadrado")
    print("2. Circulo")
    print("3. Trapecio")
    print("4. Triangulo")
    print("Escriba numero de opcion de la primera figura")
    primeraFigura = input()
    primeraFigura = int(primeraFigura)
    print("Escriba numero de opcion de la segunda figura")
    segundaFigura = input()
    segundaFigura = int(segundaFigura)
    
    if primeraFigura == 1 and segundaFigura == 1:
        Cuadrado1()
        time.sleep(2)
        Cuadrado2()
        resultado = figua1 + figura2
        print(f"{name}, segun la informacion que me diste de ambas figuras, el area total es de {resultado}")
    

    if segundaFigura == 1:
        Cuadrado()
    if segundaFigura == 2:
        Circulo()
    if segundaFigura == 3:
        Trapecio()
    if segundaFigura == 4:
        Triangulo()

    


    


