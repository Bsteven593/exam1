from jugadores import Jugador
from equipos import Equipo
from directorT import Director
from asignacion import Asignacion

print("Jugadores")

jugador1 = Jugador(10,"Alex","delantero")
print(vars(jugador1))

jugador2 = Jugador(20,"Marioi","centro")
print(vars(jugador2))

jugador3 = Jugador(2,"Luis","Arquero")
print(vars(jugador3))


print("EQUIPOS")

equipo1 = Equipo("BSC","A")
print(vars(equipo1))

equipo2 = Equipo("Emelec","D")
print(vars(equipo2))

equipo3 = Equipo("Liga De Quito","B")
print(vars(equipo3))


print("DIRECTOR TECNICO")

dt1 = Director(57,"A")
print(vars(dt1))

dt2 = Director(50,"A")
print(vars(dt2))

dt3 = Director(55,"C")
print(vars(dt3))


ag= Asignacion(11, Director("33","q"))
print(vars(ag))
print(vars(ag.rango))

         


    