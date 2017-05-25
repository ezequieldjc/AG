import math
import random


#constantes
numero_de_pruebas = 20
poblaciones_evaluaciones = []
con_elitismo = True


#funcion objetivo
def f_obj(num):
	return num/(math.pow(2,30) - 1)

def mostrar_evaluaciones(evaluaciones):
	print str(max(evaluaciones)) + "  " + str(min(evaluaciones)) + "  " + str(sum(evaluaciones) / 10) + "  " + str(sum(evaluaciones))


#Primera poblacion
cromosomas = []
for i in range(10):
	cromosoma = ""
	for j in range(30):
		cromosoma = cromosoma + str(random.randint(0,1))
	cromosomas.append(cromosoma)

print "n mayor eval    menor eval      promedio        suma"

#inicio de iteraciones de prueba
for r in range(numero_de_pruebas):

	cromosomas.sort()



	#obtener las evaluaciones de la funcion objetivo con cada cromosoma y la sumatoria
	evaluaciones = []
	for i in range(10):
		evaluacion = f_obj( int( cromosomas[i], 2) )
		evaluaciones.append( evaluacion )

	totalEvaluaciones = sum(evaluaciones)
	print str(r + 1) + " " + str(max(evaluaciones)) + "  " + str(min(evaluaciones)) + "  " + str(sum(evaluaciones) / 10) + "  " + str(sum(evaluaciones))


	#se guarda en el arreglo de poblaciones los valores de las evaluaciones
	# poblaciones_evaluaciones.append({'maximo': max(evaluaciones), 'minimo': min(evaluaciones), 'promedio': sum(evaluaciones)/10 })

	poblacionNueva = []


	#obtener los fitness de cada cromosoma
	losFitness = []
	for i in range(len(cromosomas)):
		losFitness.append( (evaluaciones[i]) / totalEvaluaciones )
	#print losFitness

	#---Elitismo---#
	if(con_elitismo):
		poblacionNueva[:] = cromosomas[8:]
		del cromosomas[8:]
	#se borran los elegidos de la poblacion inicial



	#--metodo de ruleta--#

	#asignamos arcos de la ruleta a los cromosomas en base a los pesos de cada uno
	arcosRuleta = []
	for i in range(len(cromosomas)):
		arcosRuleta.append(int(round(losFitness[i] * 100)))

	ruleta = []
	for i in range(len(arcosRuleta)):
		for j in range(arcosRuleta[i]):
			ruleta.append(i)
	#print len(arcosRuleta)
	#print len(ruleta)

	#giramos la ruleta y obtenemos los pares de cromosomas
	pares = []
	for i in range(len(cromosomas)):
		pares.append(ruleta[int(random.randint(0,len(ruleta) - 1))])
	#print pares

	#--crossover--#
	j = 0
	for i in range(len(cromosomas) / 2):
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


	#--mutacion--#

	#se calcula la probabilidad de mutacion
	for i in range(len(poblacionNueva)):
		if(random.random() <= 0.05):
			genAleatorio = random.randint(0,29)
			s = list(poblacionNueva[i])
			if(poblacionNueva[i][genAleatorio] == '1'):
				s[genAleatorio] = '0'
			else:
				s[genAleatorio] = '1'
			poblacionNueva[i] = "".join(s)


	cromosomas = []
	for i in range(10):
		cromosomas.append(poblacionNueva[i])
	# print "----------------------"
#fin de iteraciones de prueba
# print poblaciones_evaluaciones
print "mayor cromosoma " + max(cromosomas)