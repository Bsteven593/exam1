#Haz una tabla de multiplicar utilizando el ciclo for
for m in range(1,11):
    print(f'9 x {m} = {9*m}')

#Crear un buble que cuente todos los numeros pares hasta el 100    

p = 1
while p <= 100:
    if p % 2 == 0:
     print("El numero", p , "es par")
    p = p + 1  
    
    
#Imprima el siguiente patron con el ciclo for
# *   
# **  
# ***
# ****
# *****
# ****
# ***
# **
# * 
 
n = 5

for i in range(1,n+1):
    for j in range(i):
        print("* ", end=" ") 
    print()
for i in range(n -1,0, -1):
    for j in range (i):
        print("* ", end=" ") 
    print() 


    
    
   