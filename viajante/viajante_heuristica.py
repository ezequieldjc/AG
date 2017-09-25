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


#funcion para modificar el array "visitadas", poniendo un * en la capital de inicio y un 1 en la capital que ya fue visitada
def cambiarVisitadas(indice, valor):
    global visitadas
    list1 = list(visitadas)
    list1[indice] = valor
    visitadas = ''.join(list1)

#muestro las capitales a elegir
print "Capitales: "
for i in range(23):
	cap = capitales[i]
	print str(i+1) + ": " + str(cap[str(i+1)])
print
print "Elija el numero de la capital de partida: "

#leo la entrada de consola
numero_capital_partida = raw_input()
numero_capital_actual = numero_capital_partida

#obtengo el nombre de la capital e indice
capital_partida = capitales[int(numero_capital_partida, 10) - 1]

cambiarVisitadas(int(numero_capital_partida, 10) - 1, "*")

#Formo el recorrido a la capital mas cercana
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

#Vuelvo a la capital de origen
if(int(numero_capital_partida) < int(numero_capital_actual)):
    recorrido.append( (numero_capital_partida, distancias[numero_capital_actual][numero_capital_partida]) )
else:
    recorrido.append( (numero_capital_partida, distancias[numero_capital_partida][numero_capital_actual]) )

#Muestro los mensajes correspondientes
print
cap = capitales[int(numero_capital_partida, 10) - 1]
print "La capital de partida es: " + cap[numero_capital_partida]
print
total = 0
print "Recorrido completo:"
for i in range(23):
	rec = recorrido[i]
	cap = capitales[int(rec[0], 10) - 1]
	total = total + rec[1]
	print "                   " + str(cap[rec[0]]) + ": " + str(rec[1])
print
print "Longitud del trayecto: " + str(total)















