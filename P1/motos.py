from auto import Auto

class Moto(Auto):
    tamaño = float
    retro  = bool
    marcha = int
    
    def __init__(self, marca, modelo, placa, matricula, potencia, airbag,tamaño,retro,marcha):
        super().__init__(marca, modelo, placa, matricula, potencia, airbag)
        self.tamaño = tamaño
        self.retro  = retro
        self.marcha = marcha
        
    def mejor(self,transporte):
        return f'Este {self.modelo} de la marca {self.marca} es mejor que {transporte.modelo} dde la marca {transporte.marca} ya que tiene {self.marcha} marchas'    