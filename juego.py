# #hijo prodigo
# nombre = input("Ingrese su nombre: ") #guardar lo que se escribe
# #variables
# dinero = 100
# dignidad = 50
# hambre = 0

# print(f"{nombre} ha recibido su herencia") #100
# print ("Que desea hacer con su herencia?")
# print ("1. Gastarlo todo en fiestas")
# print ("2. Invertir")
# print ("3. Ahorrar")

# opcion = int(input("Elige una opcion: "))
# if opcion == 1:
#     dinero = 0
#     dignidad -=20
#     hambre += 50
# elif opcion == 2:
#     dinero +=20
# elif opcion == 3:
#     print("Muy bien usted esta ahorrando") 
# else:
#     print("Esta opcion es invalida")      
    
# # gastar(dinero, dignidad)
# # trabajar(dinero, hambre)
# def gastar(dinero, dignidad):
#     dinero -= 30
#     dignidad -=10
#     return dinero, hambre

# def trabajar(dinero, hambre):
#     dinero += 15
#     hambre += 5
#     return dinero, hambre
    
# #bucle
# while dinero > 0:
#     print("“Sigues viviendo lejos de casa…”")
#     dinero -= 10
# -------------OBJETOS
# HijoProdigo
# Debe incluir:
# Atributos:
# nombre
# dinero
# dignidad
# hambre
# arrepentimiento
class HijoProdigo : 
    def __init__(self, nombre_apellido):
        self.nombre_apellido = nombre_apellido
        self.dinero = 100
        self.dignidad = 50
        self.hambre = 0
        self.arrepentimiento =0 
# gastar_todo()
# invertir()
# ahorrar()
# trabajar()
# reflexionar()2
    def gastar_todo(self):

        dinero_antes = self.dinero
        dignidad_antes = self.dignidad
        hambre_antes = self.hambre

        self.dinero = 0
        self.dignidad -= 20
        self.hambre += 50

        print("\nGastaste todo tu dinero...")
        print(f"Dinero perdido: -{dinero_antes}")
        print(f"Dignidad perdida: {self.dignidad - dignidad_antes}")
        print(f"Hambre aumentó: +{self.hambre - hambre_antes}")

    def invertir(self):

        dinero_antes = self.dinero
        
        self.dinero += 20
        print(f"Has invertido sabiamente tu dinero: {self.dinero}")
        print(f"Dinero ganado: +{self.dinero - dinero_antes}")

    def ahorrar(self):
        print(f"Decidiste ahorrar tu dinero: {self.dinero}")
        print("Tu dinero no cambió.")
        print("Fue una decisión responsable.")

    def trabajar(self):

        dinero_antes = self.dinero
        hambre_antes = self.hambre

        self.dinero += 15
        self.hambre += 5
        print("Trabajaste y ganaste dinero.")
        print(f"Dinero ganado: +{self.dinero - dinero_antes}")
        print(f"Hambre aumentó: +{self.hambre - hambre_antes}")

    def reflexionar(self):
        if self.hambre > 40:
            self.arrepentimiento += 10
# crear jugador
jugador = HijoProdigo(input("Ingrese su nombre y apellido: "))

print(f"\n{jugador.nombre_apellido} ha recibido su herencia")
print(f"Dispone de este monto: {jugador.dinero}")
print(f"Inicia con una dignidad de: {jugador.dignidad}")
print(f"Inicia con un hambre de: {jugador.hambre}")

# Bucle principal
while jugador.dinero > 0:
    print("\n MENU ")
    print("1. Gastar todo en fiestas")
    print("2. Invertir")
    print("3. Ahorrar")
    print("4. Trabajar")

    opcion = int(input("Elige una opcion: "))

    if opcion == 1:
        jugador.gastar_todo()
    elif opcion == 2:
        jugador.invertir()
    elif opcion == 3:
        jugador.ahorrar()
    elif opcion == 4:
        jugador.trabajar()
    else:
        print("Opcion invalida")

    jugador.reflexionar()

    print("\n--- ESTADO ACTUAL ---")
    print(f"Dinero: {jugador.dinero}")
    print(f"Hambre: {jugador.hambre}")
    print(f"Dignidad: {jugador.dignidad}")
    print(f"Arrepentimiento: {jugador.arrepentimiento}")

    if jugador.dinero <= 0:
        break

print("\n El dinero se acabó.")
print("Nivel final de arrepentimiento:", jugador.arrepentimiento)