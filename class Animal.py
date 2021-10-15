class Animal:
    tam=0;
    color="";
    nombre="";

    def __init__(self,tam=5,color="azul"): #constructor de la clase
        self.tam=tam
        self.color=color
        print ("Nacio un Animal")

    def setNombre(self,nombre="pantera"):
        self.nombre=nombre

    def getTamano(self):
        return self.tam

    def getColor(self):
        return self.color

    def getNombre(self):
        return self.nombre

    def correr(self):
        print ("El animal corre")

class Gato(Animal):

    def __init__(self,tam,color):
        self.tam=tam;
        self.color=color;
        print ("Nacio un Gato\n")

    def maullar(self):
        print ("El gato maulla\n")

class Perro(Animal):
    def __init__(self,tam,color):
        self.tam=tam;
        self.color=color;
        print ("Nacio un Perro\n")

    def ladrar(self):
        print ("El perro ladra\n")

#Programa Principal
''' gato = Gato(10,"Negro");
gato.setNombre("Mustafar")
gato.maullar()
print ("Su nombre es "+gato.getNombre())
print (" mide "+str(gato.getTamano()))
print ("su color es "+gato.getColor()+"\n") '''

Animal = Animal(20,"Blanco")
Animal.setNombre("Lacie")

print ("Su nombre es "+Animal.getNombre())
print (" mide "+str(Animal.getTamano()))
print ("su color es "+Animal.getColor()+"\n")