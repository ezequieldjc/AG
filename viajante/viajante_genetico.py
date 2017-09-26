from nombres_capitales_viajante import capitales
from tabla_distancias_viajante import distancias
import operator
import math
import random

#obtengo las distancias a la capital indicada
def getMatrizDistancias(indiceCiudad):
	global distancias
	if(indiceCiudad >= 2):
		matrizDistancias = distancias[str(indiceCiudad)]
	for i in range(indiceCiudad + 1, 24):
		matrizDistancias[str(i)] = distancias[str(i)][str(indiceCiudad)]
	#devuelve una matriz de tuplas ordenadas por distancia de menor a mayor
	return sorted(matrizDistancias.items(), key=operator.itemgetter(1))
		
#funcion objetivo
def f_obj(ciudad):
	trayectoria = 0
	for i in range(23):
		rec = ciudad[i]
		trayectoria = trayectoria + rec[1]
	return 1/float(trayectoria)
	
	
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
print

for q in range(200):
	#Formo el recorrido y al final evaluo con la funcion objetivo
	recorridos = []
	evaluaciones = []
	trayectos = []
	for k in range(50):
		cromosoma = cromosomas[k]
		recorrido = []
		#armo los recorridos (sin volver a la ciudad de origen)
		for i in range(22):
			if((cromosoma[i]) < (cromosoma[i+1])):
				recorrido.append((str(cromosoma[i]), distancias[str(cromosoma[i+1])][str(cromosoma[i])]))
			else:
				recorrido.append((str(cromosoma[i]), distancias[str(cromosoma[i])][str(cromosoma[i+1])]))
		# Vuelvo a la capital de origen
		if((cromosoma[0]) < (cromosoma[22])):
			recorrido.append( (str(cromosoma[0]), distancias[str(cromosoma[22])][str(cromosoma[0])]) )
		else:
			recorrido.append( (str(cromosoma[0]), distancias[str(cromosoma[0])][str(cromosoma[22])]) )
		recorridos.append(recorrido)	
		# obtener las evaluaciones de la funcion objetivo con cada cromosoma
		evaluacion = f_obj(recorrido)
		trayecto = int(math.pow(evaluacion, -1))
		evaluaciones.append( evaluacion )
		trayectos.append(trayecto)
		
		
	
	#print evaluaciones
	if ((q == 0) or (q == 49) or (q == 99) or (q == 149) or (q == 199)):
		print
		print "----------------------"
		print "Longitudes de trayectos en la iteracion " + str(q + 1) + ":"
		print
		print trayectos
		print "Menor trayecto: " + str(min(trayectos)) 
		menor = trayectos.index(min(trayectos))
		print 
		print "Recorrido: "
		rec = recorridos[menor]
		print rec
		print "----------------------"

	# ortener la suma de todas las evaluaciones 
	totalEvaluaciones = sum(evaluaciones)

	# obtener los fitness de cada cromosoma
	losFitness = []
	for i in range(50):
		losFitness.append((evaluaciones[i]) / float(totalEvaluaciones))
	#print losFitness

	#hacemos la ruleta
	arcosRuleta = []
	for i in range(50):
		arcosRuleta.append( int( round(losFitness[i] * 10000) ) )
	#print arcosRuleta

	ruleta = []
	for i in range(len(arcosRuleta)):
		for j in range(arcosRuleta[i]):
			ruleta.append(i)
	#print len(arcosRuleta)
	#print len(ruleta)

	#giramos la ruleta y obtenemos los pares de cromosomas
	pares = []
	for i in range(50):
		pares.append(ruleta[int(random.randint(0,len(ruleta) - 1))])
	#print pares

	#crossover - probabilidad 0.75
	poblacionNueva = []
	j = 0
	for i in range(25):
		#se calcula la probabilidad de crossover
		if(random.random() <= 0.95):
			lugarDeCorte = random.randint(0,21)
			hijo1 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
			hijo2 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
			padre1 = cromosomas[pares[j]]
			padre2 = cromosomas[pares[j+1]]
			#crossover ciclico
			primerNum = padre1[0] 
			hijo1[0] = primerNum 
			segundoNum = padre2[0] 
			hijo2[0] = segundoNum
			while (segundoNum != primerNum):
				indice = padre1.index(segundoNum)
				hijo1[indice] = segundoNum
				hijo2[indice] = padre2[indice]
				segundoNum = padre2[indice]
			for m in range(23):
				if (hijo1[m] == 0):
					hijo1[m] = padre2[m]
					hijo2[m] = padre1[m]

			poblacionNueva.append(hijo1)
			poblacionNueva.append(hijo2)
			j = j + 2
		else:
			padre1 = cromosomas[pares[j]]
			padre2 = cromosomas[pares[j+1]]
			poblacionNueva.append(padre1)
			poblacionNueva.append(padre2)
			j = j + 2
	# for r in range(50):
		# print poblacionNueva[r]
	#print len(poblacionNueva)
		
	#mutacion - 0.05
	#se calcula la probabilidad de mutacion
	for i in range(50):
		if(random.random() <= 0.05):
			genAleatorio1 = random.randint(0,22)
			genAleatorio2 = random.randint(0,22)
			
			num = poblacionNueva[i][genAleatorio1]
			poblacionNueva[i][genAleatorio1] = poblacionNueva[i][genAleatorio2]
			poblacionNueva[i][genAleatorio2] = num

	cromosomas = []
	for i in range(50):
		cromosomas.append(poblacionNueva[i])






















	
	
	
	
	
	