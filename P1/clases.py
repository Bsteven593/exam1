
class transporte:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.arrancado = False

    def arrancar(self):
        self.arrancado = True
        print("el", self.marca, self.modelo, "se ha arrancado")

    def parar(self):
        self.parar = False
        print("el", self.marca, self.modelo, "se ha parado")


carro = transporte("bmw", "abc")
tesla = transporte("tesla", "cba")

print(type(carro))
print(type(tesla))

print(carro.marca, carro.modelo)
print(tesla.marca, tesla.modelo)

carro.arrancar()
tesla.arrancar()

print(carro.arrancar)
print(tesla.arrancar)

carro.parar()
tesla.parar()

print(carro.parar)
print(tesla.parar)
