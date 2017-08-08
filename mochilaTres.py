import math
from time import time

objetos =  [
    {"peso": 1800, "valor": 72},
    {"peso": 600, "valor": 36},
    {"peso": 1200, "valor": 60},
]

def int2bin(int, cant_digitos):
    return ('{0:0' + str(cant_digitos) +'b}').format(int)

def peso_total(combinacion):
    pesoCombinacion = 0
    for i in range(len(combinacion)):
        if(combinacion[i] == '1'):
            pesoCombinacion += int(objetos[i]["peso"])
    return pesoCombinacion

def valor_total(combinacion):
    valorCombinacion = 0
    for i in range(len(combinacion)):
        if (combinacion[i] == '1'):
            valorCombinacion += int(objetos[i]["valor"])
    return valorCombinacion

def funFitness (pes,val):
    return (float(val)/float(pes))

pesoMochila = 3000;

numElementos = len(objetos)


time_ex = time()

combinaciones = []


for i in range(int(math.pow(2, numElementos))):
    combinaciones.append(int2bin(i,numElementos))


pos_mayor = 0
valor_mayor = 0
for i in range(len(combinaciones)):
    if(peso_total(combinaciones[i]) <= pesoMochila):
        if(valor_total(combinaciones[i]) > valor_mayor):
            pos_mayor = i
            valor_mayor = valor_total(combinaciones[i])

print
print "EXHAUSTIVA: "
print
# print "Combinacion Exhaustiva: " + str (combinaciones[pos_mayor])
print "Los elementos que entran en la mochila son: "
for i in range (len(combinaciones[pos_mayor])):
    if str(combinaciones[pos_mayor])[i] == '1':
        print "    El elemento " + str(i+1) + " esta dentro."
        print "       Peso:" + str(objetos[i]["peso"]) + ".  Valor: " +  str(objetos[i]["valor"])
print "Peso Exhaustivo: " + str(peso_total(combinaciones[pos_mayor]))
print "Valor Exhaustivo: " + str(valor_mayor)

print "--------------------------------"


print "tiempo de proceso de algoritmo exhaustivo: " + str(time() - time_ex)
# greedy


time_greedy = time()

fitness = []

for i in range (numElementos):
    fitness.append(  {"fit":funFitness(objetos [i]["peso"], objetos [i]["valor"]) ,  "pos": i} )

# Ordeno los elementos en forma decreciente
fitness.sort(reverse=True)


# Para simplificar creo un nuevo arreglo, que contenga solamente las posiciones de los mejores fitness, de mayor a menor
fitnessOnly = []
for i in range (numElementos):
    fitnessOnly.append(fitness[i]["pos"])

# print fitnessOnly


combinacionesGreedy = []
# mejorar|
for i in (fitnessOnly):
    combinacionesGreedy.append(0)

pesoAcumuladoGreedy = 0
valorAcumuladoGreedy = 0
i=0

for i in fitnessOnly:
    if pesoAcumuladoGreedy + objetos[i]["peso"] <= pesoMochila:
        pesoAcumuladoGreedy += objetos[i] ["peso"]
        combinacionesGreedy = combinacionesGreedy[:i] + [1] + combinacionesGreedy[i+1:]
        valorAcumuladoGreedy += objetos[i]["valor"]

print
print "GREEDY"
print
# print "Combinacion de elementos Greedy: " + str(combinacionesGreedy)
print "Los elementos que entran en la mochila son: "
for i in range (len(combinacionesGreedy)):
    if combinacionesGreedy[i] == 1:
        print "    El elemento " + str(i+1) + " esta dentro."
        print "       Peso:" + str(objetos[i]["peso"]) + ".  Valor: " +  str(objetos[i]["valor"])
print "Peso Greedy: " + str(pesoAcumuladoGreedy)
print "Valor Greedy: " + str(valorAcumuladoGreedy)
print

print "tiempo de proceso de greedy: " +  str(time() - time_greedy)
