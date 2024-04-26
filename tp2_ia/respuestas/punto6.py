# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 18:16:33 2024

@author: Antonella
"""

'''
El algoritmo implementado corresponde a una búsqueda local
first-choice hill climbing.
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
        else:
            print("Solución no optima")
            
        iteracion += 1
        if iteracion % 10000 == 0:
            print(f"Iteración {iteracion}: Costo actual {costo_actual}")

    

solucion = busqueda()
print(solucion)

'''
Los problemas que se presentan con el algoritmo de búsqueda son:
- Una instrucción break que nunca se ejecutará porque se encuentra precedidad por un return.
- Un else y su instrucción que se encuentran comentados.
- Un comentario con una instrucción print que sobra.
'''