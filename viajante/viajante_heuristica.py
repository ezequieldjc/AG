from nombres_capitales_viajante import capitales
from tabla_distancias_viajante import distancias

print "elija el numero de la capital de partida :>)"
# print capitales

#leo la entrada de consola
numero_capital_partida = raw_input()
#obtengo el nombre de la capital e indice
capital_partida = capitales[int(numero_capital_partida, 10) - 1]
print capital_partida

#obtengo las distancias a cada capital
if(int(numero_capital_partida, 10) > 1):
    matriz_distancias = distancias[numero_capital_partida]

for i in range(int(numero_capital_partida) + 1, 24):
    matriz_distancias[str(i)] = distancias[str(i)][numero_capital_partida]

print matriz_distancias
