# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 18:16:33 2024

@author: Antonella
"""

import random

def generar_solucion_inicial():
    numeros = list(range(10))
    random.shuffle(numeros)
    solucion = {}
    for letra in 'SENDMORY':
        solucion[letra] = numeros.pop()
    return solucion

def evaluar_solucion(solucion):
    send = #completar código
    more = #completar código
    money = #completar código
    if #completar código:
        return 0  # Suma válida, costo = 0
    else:
        return abs(#completar código)  # Costo es la diferencia entre la suma y MONEY


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
            break

        if costo_ejerL < costo_actual:
            solucion_actual = ejerL
            costo_actual = costo_ejerL
            print("ejerL mejor")
        #else:
         #   print("Solución no optima")
            
        iteracion += 1
        if iteracion % 10000 == 0:
            print(f"Iteración {iteracion}: Costo actual {costo_actual}")

    

solucion = busqueda()
#print("Solución:")
print(solucion)
