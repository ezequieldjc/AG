from tabla_distancias_viajante import distancias
#aca va a estar el menu de opciones
print "elija metodo de resolucion: 1-heuristica, 2-genetico"
seleccion = raw_input()
if(seleccion == "1"):
    import viajante_heuristica
else:
    import viajante_genetico