from nombres_capitales_viajante import capitales
from tabla_distancias_viajante import distancias
import operator

visitadas = "00000000000000000000000"

#obtengo las distancias a la capital indicada
def getMatrizDistancias(indiceCiudad):
    global distancias
    if(int(indiceCiudad, 10) >= 1):
        matrizDistancias = distancias[indiceCiudad]
    for i in range(int(indiceCiudad) + 1, 24):
        matrizDistancias[str(i)] = distancias[str(i)][indiceCiudad]
    #devuelve una matriz de tuplas ordenadas por distancia de menor a mayor
    return sorted(matrizDistancias.items(), key=operator.itemgetter(1))
##

def cambiarVisitadas(indice, valor):
    global visitadas
    list1 = list(visitadas)
    list1[indice] = valor
    visitadas = ''.join(list1)


# def getRecorrido(indiceCap, distancias, visitadas):
#     indiceCapMasCercana = getCiudadMasCercana(indiceCap)
#     if(visitadas = 11111111111111111111111)
#     return getRecorrido(indiceCapMasCercana, distancias, visitadas)


print "elija el numero de la capital de partida"
# print capitales

#leo la entrada de consola
numero_capital_partida = raw_input()
numero_capital_actual = numero_capital_partida

#obtengo el nombre de la capital e indice
capital_partida = capitales[int(numero_capital_partida, 10) - 1]

print capital_partida

cambiarVisitadas(int(numero_capital_partida, 10) - 1, "*")

recorrido = []

for i in range(22):
    dists = getMatrizDistancias(numero_capital_actual)
    j = 0
    encontrado = False
    while(not encontrado):
        if((visitadas[int(dists[j][0]) - 1] != "1") and (visitadas[int(dists[j][0]) - 1] != "*")):
            encontrado = True
            proximaCiudad = dists[j]
            cambiarVisitadas(int(proximaCiudad[0]) - 1, "1")
            numero_capital_actual = proximaCiudad[0]
        else:
            j = j + 1
    recorrido.append(proximaCiudad)


print visitadas
print recorrido