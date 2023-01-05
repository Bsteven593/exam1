class Humano:
    def __init__(self, edad):
        self.edad = edad
       

    def hablar(self, mensaje):
        print(mensaje)


class Ingsistemas(Humano):
    
    def __init__(self):
        print("hola")
        super().__init__("80")

    def programar(self, lenguaje):
        print("voy a programar en", lenguaje)


class licDerecho(Humano):
    def estudiarCaso(self, de):
        print("voy a estudiar en", de)


pedro = Ingsistemas()
raul = licDerecho(54)
laura = Humano(44)


print(vars(pedro))
print(vars(laura))

pedro.programar("pyton")
raul.estudiarCaso("oedro")

pedro.hablar("hola")
raul.hablar("hola pedro ")
