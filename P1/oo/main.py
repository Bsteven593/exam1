class persona:
    nombre   = str
    apellido = str
    edad     = int
    
    def __init__(self,nombre,apellido,edad):
        self.nombre    = nombre
        self. apellido = apellido
        self.edad      = edad
        
if __name__ == "__main__":
     Alisson = persona ("Alisson", "Cumbajin",21  )  
     Lenin   = persona ("Lenin", "Montalvo",19) 
     print(vars (Alisson))
     print(Lenin.apellido)
     
class Persona2:
      nombre   = str
      apellido = str
      edad     = int
      correo   = str
      def __init__(self,nombre,apellido,edad,correo):
        self.nombre    = nombre
        self. apellido = apellido
        self.edad      = edad
        self.correo   = correo   
      def __srt__(self):
        return  f"hola me llamo {self.nombre} {self.apellido} Soy "   
Ejemplo1 = Persona2('Diego, yanes'+29+'desarrollo')




class Persona3:
     nombre   = str
     apellido = str
     edad     = int
     carrera  = str
     semestre = str
      
     def bienvenida(self):
          print("hola"+ self.nombre+ "Bienvenido a la carrera de")

Ejemplo4 = Persona3("Diego, yanes"+29+"desarrollo") 
Ejemplo5 = Persona3("Diego, yanes"+29+"mate") 
Ejemplo6 = Persona3("Diego, yanes"+29+"ingles") 

Ejemplo4.bienvenida()



class persona:
    nombre   = str
    apellido = str
    edad     = int
    
    def __init__(self,nombre,apellido,edad):
        self.nombre = nombre
        self.edad = edad
        self.apellido = apellido
        
    def conversar(self,otra_persona):
        return f'hola {otra_persona.nombre}, me llamo {self.nombre}' 
    
    persona1 = persona("Diego, yanes"+29+"ingles") 
    persona2 =persona ("Juan, Alver"+29+"mate")  