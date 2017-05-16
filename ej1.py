import math
import random

#prueba
#constantes
numero_de_pruebas = 19;

#funcion objetivo
def f_obj(num):
	return num/(math.pow(2,30) - 1)

#generar cromosomas aleatoriamente
cromosomas = []
for i in range(10):
	cromosoma = ""
	for j in range(30):
		if(random.random() > 0.5):
			cromosoma = cromosoma + '1'
		else:
			cromosoma = cromosoma + '0'
	cromosomas.append(cromosoma)
#print cromosomas

#inicio de iteraciones de prueba
cont1 = 0
cont2 = 0
maximo1 = 0
maximoprom1 = 0
for r in range(numero_de_pruebas):
	print
	print r + 1
	print
	#obtener las evaluaciones de la funcion objetivo con cada cromosoma y la sumatoria
	evaluaciones = []
	cromosomasBaseDiez = []
	for i in range(10):
		cromosomasBaseDiez.append(int( cromosomas[i], 2) )
		evaluaciones.append( f_obj( int( cromosomas[i], 2 ) ) )
	totalEvaluaciones = sum(evaluaciones)
	promedioEvaluaciones = sum(evaluaciones) / 10
	print "Mayor evaluacion: "
	print max(evaluaciones)
	print "Menor evaluacion: "
	print min(evaluaciones)
	print "Promedio: "
	print promedioEvaluaciones

	#cuenta la cantidad de veces que el numero maximo disminuyo de una poblacion a otra (DESPUES BORRAR)
	# if (max(cromosomas) < maximo1):
	# 	cont1 = cont1 + 1
	# maximo1 = max(cromosomas)

	#cuenta la cantidad de veces que el promedio disminuyo de una poblacion a otra (DESPUES BORRAR)
	# if (promedioEvaluaciones < maximoprom1):
	# 	cont2 = cont2 + 1
	# maximoprom1 = promedioEvaluaciones

	#obtener los fitness de cada cromosoma
	losFitness = []
	for i in range(10):
		losFitness.append((evaluaciones[i]) / totalEvaluaciones )
	#print losFitness
	print "maximo fitness"
	print max(losFitness)


	#metodo de ruleta

	#asignamos arcos de la ruleta a los cromosomas en base a los pesos de cada uno
	arcosRuleta = []
	for i in range(10):
		arcosRuleta.append(int(round(losFitness[i] * 100)))
	#hay veces que la suma de los arcos da diferente a 100, con esto se arregla
	m1 = 0
	m2 = 0
	if (sum(arcosRuleta) < 100):
		for ma in range(0,len(arcosRuleta)-1):
			if(arcosRuleta[ma] == max(arcosRuleta)):
				m1 = ma
				break
		resto = 100 - sum(arcosRuleta)
 		arcosRuleta[m1] = arcosRuleta[m1] + resto
	else:
		if (sum(arcosRuleta) > 100):
			for mi in range(0,len(arcosRuleta)-1):
				if(arcosRuleta[mi] == min(arcosRuleta)):
					m2 = mi
					break
			resto = (sum(arcosRuleta) - 100)
			arcosRuleta[m2] = arcosRuleta[m2] - resto

	ruleta = []
	for i in range(10):
		for j in range(arcosRuleta[i]):
			ruleta.append(i)
	#print arcosRuleta
	#print ruleta

	#giramos la ruleta y obtenemos los pares de cromosomas
	pares = []
	for i in range(10):
		pares.append(ruleta[int(random.randint(0,99))])
	#print pares

	j = 0
	poblacionNueva = []
	for i in range(5):
		#se calcula la probabilidad de crossover
		if(random.random() <= 0.75):
			lugarDeCorte = random.randint(0,28)
			hijo1 = ""
			hijo2 = ""
			padre1 = cromosomas[pares[j]]
			padre2 = cromosomas[pares[j+1]]
			for k in range(lugarDeCorte):
				hijo1 = hijo1 + padre1[k]
				hijo2 = hijo2 + padre2[k]
			for k in range(lugarDeCorte, 30):
				hijo1 = hijo1 + padre2[k]
				hijo2 = hijo2 + padre1[k]
			poblacionNueva.append(hijo1)
			poblacionNueva.append(hijo2)
			j = j + 2
		else:
			padre1 = cromosomas[pares[j]]
			padre2 = cromosomas[pares[j+1]]
			poblacionNueva.append(padre1)
			poblacionNueva.append(padre2)
			j = j + 2
	#print poblacionNueva

	#se calcula la probabilidad de mutacion
	for i in range(10):
		if(random.random() <= 0.05):
			genAleatorio = random.randint(0,29)
			s = list(poblacionNueva[i])
			if(poblacionNueva[i][genAleatorio] == '1'):
				s[genAleatorio] = '0'
			else:
				s[genAleatorio] = '1'
			poblacionNueva[i] = "".join(s)
	#print poblacionNueva

	#obtener el segundo mayor de la "vieja" poblacion (para usar despues)
	resto = 9999999999999
	m3 = 11
	for ma in range(0,len(cromosomas)-1):
		if(cromosomas[ma] == max(cromosomas)):
			for arr in range(0,len(cromosomas)-1):
				rest = (int( cromosomas[ma], 2) ) - (int( cromosomas[arr], 2) )
				if (rest > 0):
					if(rest < resto):
						resto = rest
						m3 = arr
			break
	#a los dos menores cromosomas de la nueva poblacion los reemplazamos por los dos mayores de la "vieja" poblacion
	for mi in range(0,len(poblacionNueva)-1):
		if(poblacionNueva[mi] == min(poblacionNueva)):
			if (poblacionNueva[mi] < max(cromosomas)):
				poblacionNueva[mi] = max(cromosomas)
				for mi2 in range(0,len(poblacionNueva)-1):
					if (m3 < 11):
						if(poblacionNueva[mi2] == min(poblacionNueva)):
							if (poblacionNueva[mi2] < cromosomas[m3]):
								poblacionNueva[mi2] = cromosomas[m3]
								break
				break

	#guardamos la poblacion nueva sobre la "vieja" en el arreglo cromosomas (para el bucle)
	cromosomas = []
	for i in range(10):
		cromosomas.append(poblacionNueva[i])
	print "----------------------"
#fin de iteraciones de prueba

#DESPUES BORRAR ESTO
# print
# print "cantidad de cagadas con maximo:"
# print cont1
# print "cantidad de cagadas con el promedio:"
# print cont2
