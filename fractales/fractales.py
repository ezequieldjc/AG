import re

primerLinea = "_" * 243
def conjuntoDeCantor(linea):
    print linea
    lineaParticion = re.match('\_+', linea)
    if(len(lineaParticion.group(0)) == 1):   return
    numeroParticion = len(lineaParticion.group(0)) / 3
    
    lineaNueva = "_" * numeroParticion + " " * numeroParticion + "_" * numeroParticion 
    conjuntoDeCantor(re.sub('\_+', lineaNueva, linea))


conjuntoDeCantor(primerLinea)
