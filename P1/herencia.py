class Persona():
    def __init__(self,apePat,apeMat,nom):
        self.apellidoPaterno = apePat
        self.apellidoMaterno = apeMat
        self.nombre         = nom
        
    def mostrasNombreCompleto(self):
        txt  = "{0} {1} , {2}"  
        return txt.format(self.apellidoPaterno, self.apellidoMaterno,self.nombre )

class Estudiante(Persona):
    
    def __init__(self,apePat, apeMat, nom, profecion):
        super().__init__(apePat, apeMat, nom)
        self.profecion = profecion
    
estu1 = Estudiante("torres","lopez","juan","ingles")
print(estu1.mostrasNombreCompleto())
print(estu1.profecion)
    