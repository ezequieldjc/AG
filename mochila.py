import math

#Chemche was here

objetos = [
    {"volumen": 150, "valor": 20},
    {"volumen": 325, "valor": 40},
    {"volumen": 600, "valor": 50},
    {"volumen": 805, "valor": 36},
    {"volumen": 430, "valor": 25},
    {"volumen": 1200, "valor": 64},
    {"volumen": 770, "valor": 54},
    {"volumen": 60, "valor": 18},
    {"volumen": 930, "valor": 46},
    {"volumen": 353, "valor": 28}
]
mochila_volumen = 4200

num_elementos = len(objetos)

def int2bin(int, cant_digitos):
    return ('{0:0' + str(cant_digitos) +'b}').format(int)

def volumen_total(combinacion):
    volumenCombinacion = 0
    for i in range(len(combinacion)):
        if(combinacion[i] == '1'):
            volumenCombinacion += int(objetos[i]["volumen"])
    return volumenCombinacion

def valor_total(combinacion):
    valorCombinacion = 0
    for i in range(len(combinacion)):
        if (combinacion[i] == '1'):
            valorCombinacion += int(objetos[i]["valor"])
    return valorCombinacion

def funFitness (vol,val):
    return (float(vol)/float(val))


combinaciones = []

for i in range(int(math.pow(2, num_elementos))):
    combinacion = int2bin(i, num_elementos)
    combinaciones.append(combinacion)

# print combinaciones

pos_mayor = 0
valor_mayor = 0
for i in range(len(combinaciones)):
    if(volumen_total(combinaciones[i]) <= mochila_volumen):
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
        print "       Volumen:" + str(objetos[i]["volumen"]) + ".  Valor: " +  str(objetos[i]["valor"])
print "Volumen Exhaustivo: " + str(volumen_total(combinaciones[pos_mayor]))
print "Valor Exhaustivo: " + str(valor_mayor)
print "--------------------------------"

# arranca el chemche
#
# algoritmo greedy
# evaluo una funcion fitness para cada elemento y voy poniendo los elementos que tengan mayor fitness

fitness = []

for i in range (num_elementos):
    fitness.append(  {"fit":funFitness(objetos [i]["volumen"], objetos [i]["valor"]) ,  "pos": i} )

# Ordeno los elementos en forma decreciente
fitness.sort(reverse=True)


# Para simplificar creo un nuevo arreglo, que contenga solamente las posiciones de los mejores fitness, de mayor a menor
fitnessOnly = []
for i in range (num_elementos):
    fitnessOnly.append(fitness[i]["pos"])

# print fitnessOnly

combinacionesGreedy = []
# mejorar|
for i in (fitnessOnly):
    combinacionesGreedy.append(0)

volumenAcumuladoGreedy = 0
valorAcumuladoGreedy = 0
i=0

for i in fitnessOnly:
    if volumenAcumuladoGreedy + objetos[i]["volumen"] <= mochila_volumen:
        volumenAcumuladoGreedy += objetos[i] ["volumen"]
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
        print "       Volumen:" + str(objetos[i]["volumen"]) + ".  Valor: " +  str(objetos[i]["valor"])
print "Volumen Greedy: " + str(volumenAcumuladoGreedy)
print "Valor Greedy: " + str(valorAcumuladoGreedy)
print
