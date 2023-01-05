from auto  import Auto
from auto  import Repuestos
from motos import Moto
from tapis import Tapis
from promo import Promo


if __name__ == "__main__":
    moto1     = Moto("Suzuki","abc","zzz",1575,100,True,140,False,5)
    repuesto1 = Repuestos("Dess","RJO"," 1616",2234,1,True,"China","metal",True)
    tapis1    = Tapis("Cuero",20,50,230)
    
    moto2     = Moto("Yamaha","bb14","cc",1009,200,True,150,False,5)
    repuesto2 = Repuestos("Fruzz","CCO","1313",1023,2,True,"Usa","carbonato",True)
    tapis2    = Tapis("Ceda",9,65,240)
    
    promo1    = Promo(2100,"31/12/2022",repuesto1,tapis1,moto1)
    promo2    = Promo(1900,"30/12/2022",repuesto2,tapis2,moto2)
    
  
    print(moto1.mejor(repuesto1))
    
   
    print(repuesto1)
    
    
    print(vars(moto1))
    print(vars(repuesto1))
    print(vars(tapis1))
    
    print(vars(moto2))
    print(vars(repuesto2))
    print(vars(tapis2))
    
   
    print(vars(promo1))
    print(vars(promo2))
    
    
    
    