class obra:
    def __init__(self,obreros,material):
     self.obreros  = obreros
     self.material = material
     
     
     
trabajo1 = obra(10,"cementos")   
trabajo2 = obra(60,"arena") 

print(type(trabajo1))
print(trabajo1.obreros, trabajo1.material)

print(vars(trabajo2))
print(trabajo2.obreros, trabajo2.material)


    