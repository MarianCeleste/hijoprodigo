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
    def __init__(self, nombre):
        self.nombre =  nombre
        self.dinero = 100
        self.dignidad = 50
        self.hambre = 0
        self.arrepentimiento =0 
# gastar_todo()
# invertir()
# ahorrar()
# trabajar()
# reflexionar()
    def gastar_todo(self):
        self.dinero = 0
        self.dignidad -=20
        self.hambre += 50
        
    def invertir(self):
        self.dinero += 20
        print(f"has invertido sabiamente tu dinero : {self.dinero}")      
        
    def ahorrar(self):
        self.dinero += 20
        
    def trabajar(self):
        self.dinero += 15
    
    def reflexionar(self):
        if self.hambre > 40:
            self.arrepentimiento += 10

jugador =  HijoProdigo(input("Ingrese su nombre: "))      #guardar lo que se escribe

print(f"{jugador.nombre} ha recibido su herencia") #100            
print(f"Dispone de este monto: {jugador.dinero}")
print(f"Incia con una dignidad de : {jugador.dignidad}")
print(f"Incia con un hambre de : {jugador.hambre}")                

while jugador.dinero > 0:
    print("“Sigues viviendo lejos de casa…”")
    # jugador.dinero -= 10  
    jugador.gastar_todo() 
    jugador.reflexionar()
    
print("El dinero se acabo")              
print("Su nivel de arrepentimiento esta en :" , jugador.arrepentimiento)      
                
            
# -----
opcion = int(input("Elige una opcion: "))
if opcion == 1:
    jugador.gastar_todo()
elif opcion == 2:
    jugador.invertir()
elif opcion == 3:
    jugador.ahorrar()
else:
    print("Esta opcion es invalida")   