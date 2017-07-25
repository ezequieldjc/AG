import math

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

num_elementos = 10

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


combinaciones = []

for i in range(int(math.pow(2, num_elementos))):
    combinacion = int2bin(i, num_elementos)
    combinaciones.append(combinacion)

print combinaciones

pos_mayor = 0
valor_mayor = 0
for i in range(len(combinaciones)):
    if(volumen_total(combinaciones[i]) <= mochila_volumen):
        if(valor_total(combinaciones[i]) > valor_mayor):
            pos_mayor = i
            valor_mayor = valor_total(combinaciones[i])


print combinaciones[pos_mayor]
print volumen_total(combinaciones[pos_mayor])
print valor_mayor