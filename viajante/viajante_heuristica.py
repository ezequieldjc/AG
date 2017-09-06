from nombres_capitales_viajante import capitales
from tabla_distancias_viajante import distancias

visitadas = "00000000000000000000000"

#obtengo las distancias a la capital indicada
def getMatrizDistancias(indiceCiudad, tablaDistancias):
    if(int(indiceCiudad, 10) >= 1):
        matrizDistancias = distancias[indiceCiudad]
    for i in range(int(indiceCiudad) + 1, 24):
        matrizDistancias[str(i)] = distancias[str(i)][indiceCiudad]
    return matrizDistancias
##



# def getRecorrido(indiceCap, distancias, visitadas):
#     indiceCapMasCercana = getCiudadMasCercana(indiceCap)
#     if(visitadas = 11111111111111111111111)
#     return getRecorrido(indiceCapMasCercana, distancias, visitadas)


print "elija el numero de la capital de partida"
# print capitales

#leo la entrada de consola
numero_capital_partida = raw_input()

#obtengo el nombre de la capital e indice
capital_partida = capitales[int(numero_capital_partida, 10) - 1]

# print capital_partida

# #obtengo las distancias a cada capital
# if(int(numero_capital_partida, 10) >= 1):
#     matriz_distancias = distancias[numero_capital_partida]
# for i in range(int(numero_capital_partida) + 1, 24):
#     matriz_distancias[str(i)] = distancias[str(i)][numero_capital_partida]
##

# print getMatrizDistancias(numero_capital_partida, distancias)

recorrido = []
# iterintems() devuelve un objeto iterator que nos permite recorrer todos los items de
# matriz_distancias para poder acceder al indice de ciudad y distancia
# for i in matriz_distancias.iteritems():
    # print i[1]

