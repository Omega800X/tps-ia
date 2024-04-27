# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 18:16:33 2024

@author: Antonella
"""

'''
El algoritmo implementado corresponde a una búsqueda local
first-choice hill climbing. Ya que no importa el camino tomado
para llegar a la solución, genera un estado siguiente y se fija
si la valoración del estado generado es mejor que la actual y en
caso positivo pasa el estado generado a ser el estado actual sin
importar si el estado generado es el estado siguiente con mejor valoración.
'''

import random

def generar_solucion_inicial():
    numeros = list(range(10))
    random.shuffle(numeros)
    solucion = {}
    for letra in 'SENDMORY':
        solucion[letra] = numeros.pop()
    return solucion

def evaluar_solucion(solucion):
    send = solucion['S'] + solucion['E'] + solucion['N'] + solucion['D'] #completar código
    more = solucion['M'] + solucion['O'] + solucion['R'] + solucion['E'] #completar código
    money = solucion['M'] + solucion['O'] + solucion['N'] + solucion['E'] + solucion['Y'] #completar código
    if (send + more) == money: #completar código
        return 0  # Suma válida, costo = 0
    else:
        return abs((send + more) - money) #completar código  # Costo es la diferencia entre la suma y MONEY

'''
La función generar tiene por objetivo generar una asignación de valores de las variables
a partir de otra asignación existente.
Para ello: 
-realiza una copia de la asignación pasada por parámetro y la guarda en ejerL
-obtiene las claves de la asignación ejerL y las guarda en letras
-posteriormente toma 4 claves al azar de letras y las guarda en las variables a, b, c y d
-intercambia los valores de las claves tomadas al azar en la asignación guardada en ejerL
-retorna la nueva asignación ejerL
'''
def generar(solucion):
    ejerL = solucion.copy()
    letras = list(solucion.keys())
    a, b, c, d = random.sample(letras, 4)
    ejerL[a], ejerL[b], ejerL[c], ejerL[d] = ejerL[d], ejerL[c], ejerL[b], ejerL[a]
    return ejerL

def busqueda():
    solucion_actual = generar_solucion_inicial()
    costo_actual = evaluar_solucion(solucion_actual)

    iteracion = 0
    while True:
        ejerL = generar(solucion_actual)
        costo_ejerL = evaluar_solucion(ejerL)

        if costo_ejerL == 0:
            print("Solución encontrada:")
            return ejerL

        if costo_ejerL < costo_actual:
            solucion_actual = ejerL
            costo_actual = costo_ejerL
            print("ejerL mejor")
            
        iteracion += 1
        if iteracion % 10000 == 0:
            print(f"Iteración {iteracion}: Costo actual {costo_actual}")
            return None

    

solucion = busqueda()
print(solucion)

'''
Los problemas que se presentan con el algoritmo de búsqueda son:
- Puede no encontrar la configuración objetivo, quedándose en un máximo local.
- En caso de quedarse en un máximo local, el algoritmo no cuenta con una condición de corte,
  por lo que quedará en un bucle infinito.
- En caso de no encontrar una solución, el algoritmo no contempla qué debe retornar la función.

Para solucionar el bucle infinito, se puede seleccionar un límite de iteraciones para el algoritmo
y en caso de que este llegue a ese límite romper el bucle y retornar None para indicar que no se
encontró la solución óptima.
'''