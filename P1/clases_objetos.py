class Humano:
    def __init__(self,edad):
        self.edad = edad
        print ("soy un nuevo objetos")
        
    def hablar(self, mensaje):
        print (mensaje)   

pedro = Humano(22)

raul = Humano(11)

laura = Humano(44)

print(vars(pedro))    
print("soy pedro y tengo",pedro.edad) 
print("soy raul y tengo",raul.edad)

print(vars(laura))



pedro.hablar("hola")
raul.hablar("hola pedro ")   