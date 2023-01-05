class Auto:
    marca     = str
    modelo    = str
    placa     = str
    matricula = int
    potencia  = int
    airbag    = bool
    
    def __init__(self,marca,modelo,placa,matricula,potencia,airbag):
      self.marca     = marca
      self.modelo    = modelo
      self.placa     = placa
      self.matricula = matricula
      self.potencia  = potencia
      self.airbag    = airbag  
      
class Repuestos(Auto):
    made    = str
    materal = str
    nuevo   = bool   
    
    def __init__(self, marca, modelo, placa, matricula, potencia, airbag,made,material,nuevo):
       super().__init__(marca, modelo, placa, matricula, potencia, airbag)
       self.made = made
       self.material = material
       self.nuevo = nuevo
       
    def __str__(self):
        return f'El {self.modelo} de la marca {self.marca} esta hecha en {self.made} con un material {self.material} su resgistron es {self.placa} para la potencia de {self.potencia} con la serie {self.matricula} , tiene airbag {self.airbag} y es nuevo {self.nuevo}'      
     