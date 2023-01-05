from auto  import Auto
from auto  import Repuestos
from motos import Moto
from tapis import Tapis

class Promo:
    precio       = int
    fecha_compra = str
    repuestoss   = Repuestos("","","","","","","","","")
    tapiss       = Tapis("","","","")
    motoss       = Moto("","","","","","","","","")
    
    def __init__(self,precio,fecha_compra,repuestoss,tapiss,motoss):
        self.precio       = precio
        self.fecha_compra = fecha_compra
        self.repuestoss   = repuestoss
        self.tapiss       = tapiss
        self.motoss       = motoss