import math
from time import time

#agregamos mas objetos para realizar pruebas con cantidades distintas.
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
    {"volumen": 353, "valor": 28},
    {"volumen": 432, "valor": 33},
    {"volumen": 567, "valor": 22},
    {"volumen": 486, "valor": 74},
    {"volumen": 133, "valor": 58},
    {"volumen": 36, "valor": 33},
    {"volumen": 540, "valor": 65},
    {"volumen": 638, "valor": 31}
]
mochila_volumen = 4200

num_elementos = 10

# devuelve la expresion binaria del entero ingresado, con la cantidad de digitos ingresado
def int2bin(int, cant_digitos):
    return ('{0:0' + str(cant_digitos) +'b}').format(int)

#devuelve el volumen total de una combinacion de objetos ingresado como expresion binaria
def volumen_total(combinacion):
    volumenCombinacion = 0
    for i in range(len(combinacion)):
        if(combinacion[i] == '1'):
            volumenCombinacion += int(objetos[i]["volumen"])
    return volumenCombinacion

#devuelve el valor total de una combinacion de objetos ingresado como expresion binaria
def valor_total(combinacion):
    valorCombinacion = 0
    for i in range(len(combinacion)):
        if (combinacion[i] == '1'):
            valorCombinacion += int(objetos[i]["valor"])
    return valorCombinacion

#funcion fitness utilizada para la busqueda heuristica
def funFitness (vol,val):
    return (float(val)/float(vol))


time_ex = time()

#genera todas las combinaciones posibles de objetos, y las guarda en el array combinaciones
combinaciones = []

for i in range(int(math.pow(2, num_elementos))):
    combinacion = int2bin(i, num_elementos)
    combinaciones.append(combinacion)

# print combinaciones

#se recorren todas las combinaciones y se determina exhaustivamente cual es la mejor combinacion
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

# se muestran cuales son los objetos elegidos por el algoritmo, el volumen total ocupado y el valor total alcanzado.
print "Los elementos que entran en la mochila son: "
for i in range (len(combinaciones[pos_mayor])):
    if str(combinaciones[pos_mayor])[i] == '1':
        print "    El elemento " + str(i+1) + " esta dentro."
        print "       Volumen:" + str(objetos[i]["volumen"]) + ".  Valor: " +  str(objetos[i]["valor"])
print "Volumen Exhaustivo: " + str(volumen_total(combinaciones[pos_mayor]))
print "Valor Exhaustivo: " + str(valor_mayor)
print "--------------------------------"


print "tiempo de proceso de algoritmo exhaustivo: " + str(time() - time_ex)
#
# algoritmo greedy
# evaluo una funcion fitness para cada elemento y voy poniendo los elementos que tengan mayor fitness

time_greedy = time()

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
for i in (fitnessOnly):
    combinacionesGreedy.append(0)

volumenAcumuladoGreedy = 0
valorAcumuladoGreedy = 0

for i in fitnessOnly:
    if volumenAcumuladoGreedy + objetos[i]["volumen"] <= mochila_volumen:
        volumenAcumuladoGreedy += objetos[i] ["volumen"]
        #agrega un 1 donde habia un 0, en la posicion del objeto agregado
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

print "tiempo de proceso de greedy: " + str(time() - time_greedy)
