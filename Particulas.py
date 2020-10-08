from particula import Particula

class Particulas:
    def __init__(self):
        self.__particulas = []
    
    def agregar_final(self, particula:Particula):
        self.__particulas.append(particula)
    
    def agregar_inicio(self, particula:Particula):
        self.__particulas.insert(0, particula)

    def mostrar(self):
        for particulas in self.__particulas:
            print(particulas)

Part = Particulas()

p01 = Particula(1,20,30,40,50,60,50,40,30,100)
p02 = Particula(2,30,50,23,43,12,53,12,53,200)
Part.agregar_inicio(p01)
Part.agregar_final(p02)
Part.mostrar()
