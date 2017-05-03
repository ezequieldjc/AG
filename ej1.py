import math
import random

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

for r in range(100):
	print
	print r
	print
	#print "repeticion numero:" + r
	#obtener las evaluaciones de la funcion objetivo con cada cromosoma y la sumatoria
	evaluaciones = []
	cromosomasBaseDiez = []
	for i in range(10):
		#print cromosomas[i]
		#print(int( cromosomas[i], 2) ) 
		cromosomasBaseDiez.append(int( cromosomas[i], 2) )
		#print ( f_obj( int( cromosomas[i], 2 ) ) )
		evaluaciones.append( f_obj( int( cromosomas[i], 2 ) ) )
	totalEvaluaciones = sum(evaluaciones)
	promedioEvaluaciones = sum(evaluaciones) / 10
	maxEvaluaciones = max(evaluaciones)
	print "Mayor: " 
	print max(cromosomasBaseDiez)
	print "Mayor en base 2: " 
	print max(cromosomas)
	print "Menor: " 
	print min(cromosomasBaseDiez)
	print "Promedio: " 
	print promedioEvaluaciones
	
	
	#obtener los fitness de cada cromosoma 
	losFitness = []
	for i in range(10):
		losFitness.append( f_obj( int( cromosomas[i], 2 ) ) / totalEvaluaciones )
	#print "los fitnesses"
	#print losFitness
	maxFitness = max(losFitness)
	
	
	#metodo de ruleta
	
	#asignamos arcos de la ruleta a los cromosomas en base a los pesos de cada uno
	arcosRuleta = []
	for i in range(10):
		arcosRuleta.append(int(round(losFitness[i] * 100)))
	ruleta = []
	for i in range(10):
		for j in range(arcosRuleta[i]):
			ruleta.append(i)		
	
	#print "ruleta"
	#print ruleta
	#print arcosRuleta
	#print sum(arcosRuleta)
	
	#giramos la ruleta y obtenemos los pares de cromos
	pares = []
	for i in range(10):
		pares.append(ruleta[int(random.randint(0,99))])
	#print pares
	
	j = 0
	poblacionNueva = []
	for i in range(5):
		#probabilidad de crossover
		if(random.random() <= 0.75):
			lugarDeCorte = random.randint(0,28)
			#print lugarDeCorte
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
	#print len(poblacionNueva)
	
	#se calcula la probabilidad de mutacion 
	for i in range(10):
		if(random.random() <= 0.05):
			#print (i + 1)
			genAleatorio = random.randint(0,29)
			#print (genAleatorio + 1)
			poblacionNueva[i][genAleatorio]
	
			s = list(poblacionNueva[i])
	
			if(poblacionNueva[i][genAleatorio] == '1'):
				s[genAleatorio] = '0'
			else:
				s[genAleatorio] = '1'
			poblacionNueva[i] = "".join(s)
	
	#print poblacionNueva
	
	cromosomas = []
	for i in range(10):
		cromosomas.append(poblacionNueva[i])
		