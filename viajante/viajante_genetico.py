from nombres_capitales_viajante import capitales
from tabla_distancias_viajante import distancias
import operator
import math
import random

#obtengo las distancias a la capital indicada
def getMatrizDistancias(indiceCiudad):
	global distancias
	if(indiceCiudad >= 2):
		matrizDistancias = distancias[indiceCiudad]
	for i in range((indiceCiudad) + 1, 24):
		matrizDistancias[str(i)] = distancias[str(i)][indiceCiudad]
	#devuelve una matriz de tuplas ordenadas por distancia de menor a mayor
	return sorted(matrizDistancias.items(), key=operator.itemgetter(1))
		
#funcion objetivo
def f_obj(ciudad):
	total = 0
	for i in range(23):
		rec = ciudad[i]
		total = total + rec[1]
	return total
	
	
#constantes
numero_de_pruebas = 3


#primer poblacion
cromosomas = []
for i in range(50):
	ciudades = "00000000000000000000000"
	cromosoma = []
	for j in range(23):
		num = random.randint(1,23)
		#esto es para que no se repitan dos numeros de ciudades
		while (ciudades[num-1] == '1' ):
			num = random.randint(1,23)
		list1 = list(ciudades)
		list1[num-1] = '1'
		ciudades = ''.join(list1)
		cromosoma.append(num)
	cromosomas.append(cromosoma)
#print cromosomas
#print ciudades


#Formo el recorrido y al final evaluo con la funcion objetivo
recorridos = []
evaluaciones = []
for k in range(50):
	cromosoma = cromosomas[k]
	numero_capital_actual = cromosoma[0]
	recorrido = []
	for i in range(22):
		dists = getMatrizDistancias(numero_capital_actual)
		proximaCiudad = dists[cromosoma[i+1]]
		numero_capital_actual = proximaCiudad[0]
		recorrido.append(proximaCiudad)
	#Vuelvo a la capital de origen
	if(int(cromosoma[i+1]) < int(cromosoma[22])):
		recorrido.append( (numero_capital_partida, distancias[numero_capital_actual][numero_capital_partida]) )
	else:
		recorrido.append( (numero_capital_partida, distancias[numero_capital_partida][numero_capital_actual]) )
	recorridos.append(recorrido)	
	#obtener las evaluaciones de la funcion objetivo con cada cromosoma
	evaluacion = f_obj(recorrido)
	evaluaciones.append( evaluacion )

print evaluaciones















